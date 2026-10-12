# Python Learning Journey

This page turns the repository into a reviewable learning path. It is a suggested order based on the files currently available, not a claim that every concept has been mastered.

## Stage 1 — Fundamentals

Review variables, data types, operators, string operations, type conversion, input, and output.

Repository work: [Class Work](Class%20Work/README.md)

Self-check: Can I explain the difference between assignment and comparison, integer and floating-point division, membership and identity, and common type conversions?

## Stage 2 — Conditions and Loops

Practise branching, ranges, nested loops, for, while, and loop else. Use billing, triangle, and Snake and Ladders examples to trace the state after each iteration.

Repository work: [Practice](practice/README.md) and [Class Work](Class%20Work/README.md)

Self-check: Have I tested boundary values, invalid input, and the case where a loop runs zero times?

## Stage 3 — Collections and Strings

Work through strings, lists, tuples, sets, dictionaries, sorting, membership, and counting.

Self-check: Can I choose an appropriate collection and explain its behaviour for duplicates, ordering, and lookup?

## Stage 4 — Functions and Reusable Logic

Review functions, lambda expressions, map, filter, reduce, recursion, generators, modules, math, and collections.Counter.

Self-check: Can I describe each function's inputs, outputs, side effects, and edge cases? Prefer a named function over a lambda when it improves readability.

## Stage 5 — Object-Oriented Programming

Review constructors, instance attributes, inheritance, polymorphism, and abstraction. Practise explaining which state belongs to an object and how its public interface should be used.

Self-check: Can I write a small class from scratch and use it without relying on undocumented internal attributes?

## Stage 6 — Combine Concepts

Attempt the numbered [assignments](Assignments/README.md) and [weekly exercises](Weeklytests/README.md). First solve without copying, then compare with the existing solution and write down what could be improved.

Self-check: Can I break a larger problem into small functions and handle empty input, invalid input, and unexpected values?

## Stage 7 — Build Engineering Habits

Use Git, meaningful commit messages, readable naming, comments that explain why, syntax checks, and small tests. A useful next step is to extract pure functions from interactive scripts so they can be tested automatically.

## Personal Review Checklist

Mark a line complete only after you can explain the concept and solve a fresh exercise without following the original file.

- [ ] Explain and use common Python data types and operators.
- [ ] Write conditions and loops, including boundary cases.
- [ ] Use strings, lists, tuples, sets, and dictionaries confidently.
- [ ] Write functions with clear inputs and return values.
- [ ] Explain and use modules, exceptions, and file handling.
- [ ] Explain constructors, inheritance, and polymorphism with a small example.
- [ ] Solve the assignments again from a blank file.
- [ ] Add automated tests for a few reusable functions.
- [ ] Review mistakes and record how they were fixed.

## Learning Reflection Template

Copy and complete this section when recording a milestone:

    ### Review date: YYYY-MM-DD
    - Concepts studied:
    - What I implemented:
    - What I understood well:
    - What confused me or failed:
    - How I fixed it:
    - One exercise to retry without notes:
    - Next topic:

## Suggested Next Improvements

1. Turn reusable calculations into small functions with return values.
2. Add tests for those functions before testing interactive input and output.
3. Add input validation for values such as amounts, ages, and menu choices.
4. Refactor duplicated logic only after preserving the original exercise's purpose.
