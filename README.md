##  Acronym Generator
#  Overview

The Acronym Generator is a simple Python program that takes a phrase as input from the user and generates an acronym by extracting the first letter of each word in the phrase. The acronym letters are displayed in uppercase.

##  Features
1.  Takes a phrase as input from the user.
2.  Automatically split the phrase into words.
3.  Extract the first letter of each word and convert it to uppercase.
4.  Combine the letters to form the acronym.

Example Used

$ python acronym_generator.py
Enter a Phrase: Random Access Memory
RAM

##  Contributing
Feel free to fork the repository and submit pull requests if you want to contribute.

##  Code Walkthrough:
1.  The user is prompted to input a phrase using input("Enter a Phrase: ").
2.  The phrase is split into individual words using the split() method, which creates a list where each element is a word from the phrase.
3.  The script initializes an empty string acronym to store the final result.
4.  A for loop iterates through each word in the list, retrieves the first letter, converts it to uppercase, and appends it to the acronym.
5.  The generated acronym is printed on the console.
