import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()
	cropped = frame[int(frame.shape[0]/2):frame.shape[0]]

	gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

	template = cv2.imread('match.png', 0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where(res >= threshold)
	for pt in zip(*loc[::-1]):
		cv2.rectangle(cropped, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

	cv2.imshow("test", lines_edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# kernel_size = 5
	# blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

	# low_threshold = 50
	# high_threshold = 150
	# edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

	# rho = 1
	# theta = np.pi / 180
	# threshold = 15
	# min_line_length = 50
	# max_line_gap = 20
	# line_image = np.copy(cropped) * 0

	# lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

	# for line in lines:
	# 	for x1, y1, x2, y2 in line:
	# 		cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)
	
	# lines_edges = cv2.addWeighted(cropped, 0.8, line_image, 1, 0)

	# cv2.imshow("test", lines_edges)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break


cap.release()
cv2.destroyAllWindows()