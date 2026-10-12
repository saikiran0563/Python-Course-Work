# 🐍 My Python Learning Journey

This repository records my progress while learning Python through class examples, assignments, weekly assessments, and independent practice. It is a **learning journal and exercise archive**: the aim is to understand concepts, practise them independently, revisit mistakes, and gradually write clearer code.

For application-style projects, see my separate [Task Manager](https://github.com/saikiran0563/Task-Manager) and [Job Application Tracker](https://github.com/saikiran0563/Job-Application-Tracker) repositories.

[![Python syntax checks](https://github.com/saikiran0563/Python-Course-Work/actions/workflows/python-checks.yml/badge.svg?branch=main)](https://github.com/saikiran0563/Python-Course-Work/actions/workflows/python-checks.yml)

## Start Here

1. Read [Learning Journey](LEARNING_JOURNEY.md) for a suggested path through the repository.
2. Review the numbered examples in [Class Work](Class%20Work/README.md).
3. Try the exercises in [Practice](practice/README.md) before looking at previous solutions.
4. Use [Weekly Tests](Weeklytests/README.md) to revisit concepts and check your understanding.
5. Review the [Assignments](Assignments/README.md) as small programs combining several concepts.

## How the Repository Is Organized

| Area | What it contains | Start here |
|---|---|---|
| Class Work | Numbered concept examples, from operators and collections to functions and OOP | [Class Work README](Class%20Work/README.md) |
| Practice | Short problem-solving exercises such as triangles, billing, BMI, grades, and number problems | [Practice README](practice/README.md) |
| Weekly Tests | Assessment exercises and helper functions | [Weekly Tests README](Weeklytests/README.md) |
| Assignments | Three larger interactive programs | [Assignments README](Assignments/README.md) |
| Learning Journey | Suggested sequence, review checklist, and reflection template | [LEARNING_JOURNEY.md](LEARNING_JOURNEY.md) |

## Concepts Represented So Far

- **Python fundamentals:** variables, data types, operators, input, output, and type conversion
- **Control flow:** if / elif / else, for, while, nested loops, and loop else
- **Core data structures:** strings, lists, tuples, sets, and dictionaries
- **Functions and problem solving:** reusable functions, lambda expressions, recursion, and generators
- **Useful built-ins and modules:** map, filter, reduce, Counter, math, and modules
- **Object-oriented programming:** constructors, inheritance, polymorphism, and abstraction
- **Exception handling:** handling common runtime errors and validating input
- **NumPy (studied after exception handling):** numerical arrays, array dimensions and shape, indexing and slicing, vectorized operations, and aggregations
- **pandas (studied after NumPy):** Series and DataFrames, inspecting tabular data, selecting and filtering rows and columns, sorting, missing-value handling, and summary statistics
- **Working with data:** basic file and structured-data exercises
- **Small programs:** movie information, chat-message analysis, a Python interview quiz, games, and everyday calculations

Runnable NumPy and pandas examples are available in [27.numpy.py](Class%20Work/27.numpy.py) and [28.pandas.py](Class%20Work/28.pandas.py). Their dependencies can be installed with `python -m pip install numpy pandas`. This list records study topics; it does not claim that every topic is mastered.

## How I Practise

For each concept, the goal is to:

1. Understand the idea and explain it in my own words.
2. Predict the output before running the example.
3. Change inputs or requirements and observe the result.
4. Solve a related exercise without copying the original.
5. Review edge cases and record what I learned.

Use [LEARNING_JOURNEY.md](LEARNING_JOURNEY.md) to record milestones and review weak areas.

## Run an Example

Install Python 3.12 or a compatible newer version. Most basic exercises use only the Python standard library. The NumPy and pandas lessons require additional packages: run `python -m pip install numpy pandas` in your active environment.

From the repository root in PowerShell, quote paths that contain spaces:

    python "Class Work/1.Operators in Python.py"
    python "Class Work/17.lambda.py"
    python "Class Work/27.numpy.py"
    python "Class Work/28.pandas.py"
    python "practice/3.bmi.py"
    python Assignments/assignment-1.py

Some programs are interactive and wait for input in the terminal.

## Automated Check

GitHub Actions compiles the Python source files to detect syntax errors. This is a **syntax check**, not a guarantee that every interactive exercise behaves correctly or every assessment question has been tested.

## Good Repository Habits

- Keep generated files such as __pycache__/ and *.pyc out of commits.
- Never put real passwords, PINs, API keys, or personal data in example files.
- Use clearly synthetic data for practice datasets.
- Keep original classroom filenames for traceability; improve names when doing so will not break references.
- Make focused commits with messages that explain the change.

## Author

**Sai Kiran Buska**

- GitHub: https://github.com/saikiran0563
- LinkedIn: https://www.linkedin.com/in/sai-kiran-buska-127866403
