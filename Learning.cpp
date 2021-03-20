// This is a comment
/*
multi line
g++ -std=c++11 Learning.cpp
*/

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main() {
	cout << "Hello world" << endl;

	const double PI = 3.14;
	char myChar = 'a';
	boolean isBool = true;
	int myInt = 19;
	float num = 3.14

	cout << "myInt" << myInt << endl;

	cout << "4/5" << (float)4/5 << endl;

	int nums[5];
	int othernums[5] = {4,13,14,24,34};
	char name[5][6] = {{'J','o','s','h','u','a'},
						{'S','t','e','p','h','a'}};
	cout << "2nd letter in 1st array" << name[0][1] << endl;

	for (int i = 1; i <= 10; i++) {

	}

	string guessed;
	int guess = 0;
	do {
		cout << "Guess 1-10: ";
		getline(cin, guessed);

		guess = stoi(guessed);
		cout << guess << endl;
	} while (guess != 4);

	return 0;
}