Password Strength Checker

Simple interactive Python program that analyses password strength and provides feedback on how to improve it. Checks length, character variety, repetition, sequential patterns, and compares against a list of the most common passwords.


Features:
- Detects common passwords and automatically invalidates them
- Scores password strength as: Weak, Medium, Strong, or Very strong
- Performs the following checks:
 - Length
 - Uppercase letters
 - Lowercase letters
 - Numbers
 - Special characters
 - Sequential characters such as abc or 123
 - Excessive repetition of characters
- Displays running checks as they happen
- Shows total points and points per criterion
- Allows user to test multiple passwords in one session


Requirements:
- Python 3.8 or newer
- No external libraries required


How to Run:
Download or clone the repository, then run the script from a terminal


How it works:
1. The user is prompted to enter a password
2. Empty passwords are rejected
3. The password is checked against common passwords
4. Each rule is evaluated and results are printed as checks run
5. A total strength score and rating are displayed
6. Suggestions are provided to improve the password
7. The user can enter another password or exit


Disclaimer:
This tool is for educational purposes only. It is not a professional security auditing tool and should not be relied upon as the only measure of password security. Do not test real passwords that you actively use.


Educational Purposes:
Displays proper understanding of python through the use of a working and navigable program


Author:
Created by RA-DevProjects

GitHub profile:
https://github.com/RA-DevProjects


Contributions:
Contributions, improvements, and suggestions are very much welcome. Pull requests and issue reports are appreciated since this was quite a simple project.
