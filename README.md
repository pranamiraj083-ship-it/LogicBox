# LogicBox

LogicBox is a beginner-friendly Python console application that combines pattern generation and number analysis in a simple menu-driven program. It demonstrates the use of loops, conditional statements, and the `match-case` statement introduced in Python 3.10+.

---

## Description

This project allows users to:

- Generate a star (`*`) pattern.
- Analyze numbers in a given range.
- Check whether each number is even or odd.
- Calculate the sum of all numbers in the selected range.
- Exit the program through a simple menu.

This project is designed for beginners who want to practice Python fundamentals.

---

## Features

- Menu-driven interface
- Star pattern generator
- Even and odd number checker
- Sum of numbers in a range
- Simple and clean Python code
- Easy to understand for beginners

---

## Project Structure

```
LogicBox/
│── logicbox.py
│── README.md
```

---

## Requirements

- Python 3.10 or above

Check your Python version:

```bash
python --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pranamiraj083-ship-it/LogicBox.git
```

Move into the project folder:

```bash
cd LogicBox
```

Run the program:

```bash
python logicbox.py
```

---

## Program Menu

```
Welcome to the Pattern Generator and Number Analyzer!

1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

---

## Option 1: Pattern Generator

The program asks the user for the number of rows and prints a star pattern.

### Example

Input

```
Enter the number of rows: 5
```

Output

```
*
**
***
****
*****
```

---

## Option 2: Number Analyzer

The program asks the user for a starting number and an ending number.

It then:

- Checks whether each number is Even or Odd.
- Calculates the total sum of the range.

### Example

Input

```
Start: 1
End: 5
```

Output

```
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

---

## Option 3: Exit

Selecting this option closes the program.

```
Exiting the program. Goodbye!
```

---

## Concepts Used

- Variables
- User Input
- while Loop
- for Loop
- if-else Statement
- match-case Statement
- range() Function
- Arithmetic Operators
- String Multiplication
- Formatted Strings (f-strings)

---

## Sample Output

```
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 2

Enter the start of the range: 1
Enter the end of the range: 5

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

---

## Future Improvements

- Number guessing game
- Prime number checker
- Fibonacci series generator
- Multiplication table generator
- Additional pattern designs
- Input validation and error handling
- Save results to a text file

---

## Author

**Pranami Raj**

GitHub: https://github.com/pranamiraj083-ship-it

Repository: https://github.com/pranamiraj083-ship-it/LogicBox

---

## License

This project is intended for educational and learning purposes.

You are free to use, modify, and share this project.
