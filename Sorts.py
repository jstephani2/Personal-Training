######################################################################
# Implementing various sorting algorithms for practice
# 1. Selection sort
# 2. Bubble sort
# 3. Insertion sort
# 4. Shell sort
# 5. Merge sort
# 6. Quicksort
######################################################################
import copy

# 1. Selection sort
def selection_sort(arr):
	# Find smallest element in array and swap it with the first element
	# Repeat until array is sorted
	for i in range(len(arr)):
		i_of_min = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i_of_min]:
				i_of_min = j
		# Swap value into place
		arr[i], arr[i_of_min] = arr[i_of_min], arr[i]
	print(arr)

# 2. Bubble sort
def bubble_sort(arr):
	# iterate over every index for start of "bubbling"
	for i in range(len(arr)):
		swap_happened = False
		for j in range(i, len(arr)-1):
			if arr[j+1] < arr[j]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap_happened = True
		if not swap_happened:
			print(arr)
			return

# 3. Insertion sort
def insertion_sort(arr):
	for i in range(len(arr)-1):
		if (arr[i+1] < arr[i]):
			arr[i], arr[i+1] = arr[i+1], arr[i]
			j = i
			while j > 0:
				if (arr[j-1] > arr[j]):
					arr[j], arr[j-1] = arr[j-1], arr[j]
				j = j-1
	print(arr)

# 4. Shell sort
def shell_sort(arr):
	length = len(arr)
	gap = length // 2
	
	while gap > 0:
		for i in range(gap, length):
			temp = arr[i]
			j = i

			while j >= gap and arr[j-gap] > temp:
				arr[j] = arr[j-gap]
				j -= gap

			arr[j] = temp

			print('Gap: ', gap)
			print(arr)
			gap = gap // 2

	print(arr)

array = [2,1,4,8,3]
selection_sort(copy.deepcopy(array))
bubble_sort(copy.deepcopy(array))
insertion_sort(copy.deepcopy(array))
shell_sort(copy.deepcopy(array))