# test
Python Easy Revision Practice

This project contains basic Python practice exercises designed to help reinforce core programming concepts before tests or coding assessments.

The exercises focus on:

Conditional statements

Functions

Basic loops

Simple algorithms

Unit testing with unittest

The goal of this project is to practice problem-solving and writing clean Python functions.

Files in This Project
easy_revision.py

This file contains 10 functions that need to be implemented. Each function solves a small programming problem.

Examples of tasks include:

Checking if a number is even

Adding two numbers

Counting characters in a string

Reversing a string

Working with lists

Each function includes a docstring explaining what needs to be done.

Example:

def is_even(num):
    """
    Return True if number is even, otherwise False.
    Example:
    is_even(4) -> True
    is_even(3) -> False
    """

Students must implement the logic inside each function.

test_easy_revision.py

This file contains unit tests using Python's unittest framework.

The tests check whether each function behaves correctly.

Example test:

def test_is_even(self):
    self.assertTrue(is_even(4))
    self.assertFalse(is_even(3))

Running the tests helps confirm that the functions are working properly.

Example Problems

Some of the problems included in the project:

Example 1 — Even Number Check

Input:

is_even(4)

Output:

True
Example 2 — Add Numbers

Input:

add_numbers(2,3)

Output:

5
Example 3 — Reverse a String

Input:

reverse_string("abc")

Output:

"cba"
Example 4 — Count Numbers

Input:

count_to_n(4)

Output:

[1,2,3,4]
How to Run the Program

Navigate to the project folder:

cd Desktop/practice1

Run the Python file:

python3 easy_revision.py
Running the Unit Tests

To run the tests, use:

python3 -m unittest test_easy_revision.py

If all functions are correct, you will see something like:

Ran 10 tests in 0.001s

OK
Skills Practiced

This project helps practice:

Writing Python functions

Using conditional statements

Using loops

Solving small algorithmic problems

Writing and running unit tests

Basic command line usage

Purpose

This project is meant for practice and revision before coding tests or programming exercises. It helps build confidence with basic Python problem solving.