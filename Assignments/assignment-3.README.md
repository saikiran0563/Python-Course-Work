# Assignment 3 — Python Interview Prep Quiz Game

## Overview

A terminal-based multiple-choice quiz that tests Python concepts related to execution, objects, memory management, the GIL, garbage collection, and mutability.

## Concepts Practiced

- Functions
- Lists and dictionaries
- Loops
- `enumerate()`
- Conditional statements
- User input validation at the basic CLI level
- Score calculation
- Reusable function design

## Program Structure

### `welcome()`
Displays the quiz introduction.

### `run_quiz(questions)`
Iterates through the question set, displays options, accepts answers, checks correctness, and calculates the score.

### `show_result(score, total)`
Displays the final score and a feedback message based on the result.

## Topics Covered by the Quiz

- Dynamic typing
- Python's execution model
- Bytecode and the Python Virtual Machine
- Reasons Python can be slower than compiled languages
- Global Interpreter Lock (GIL)
- Object references and object identity
- Integer caching
- String interning
- Python memory management
- Reference counting
- PyMalloc
- Circular references
- Garbage collection
- Mutable vs. immutable objects
- The `None` singleton

## Run

```bash
python Assignments/assignment-3.py
```

## Learning Outcome

This assignment combines Python programming practice with interview-oriented theory and demonstrates how to build a reusable command-line quiz application using core Python constructs.
