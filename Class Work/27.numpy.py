"""NumPy fundamentals: arrays, shapes, indexing, vectorized math, and aggregation.

Install the library if needed:
    python -m pip install numpy

Run from the repository root:
    python "Class Work/27.numpy.py"
"""
import numpy as np


def main() -> None:
    print("=== 1. Creating arrays ===")
    scores = np.array([78, 92, 85, 67, 90])
    print("Scores:", scores)
    print("Zeros:", np.zeros(3, dtype=int))
    print("Range:", np.arange(0, 10, 2))

    print("\n=== 2. Array properties ===")
    print("Shape:", scores.shape)
    print("Dimensions:", scores.ndim)
    print("Number of elements:", scores.size)
    print("Data type:", scores.dtype)

    print("\n=== 3. Indexing and slicing ===")
    print("First score:", scores[0])
    print("Last score:", scores[-1])
    print("First three scores:", scores[:3])
    print("Scores from index 1 to 3:", scores[1:4])

    print("\n=== 4. Vectorized operations ===")
    bonus_scores = scores + 5
    print("Add 5 to every score:", bonus_scores)
    print("Scores doubled:", scores * 2)
    print("Scores >= 85:", scores >= 85)
    print("Scores at least 85:", scores[scores >= 85])

    print("\n=== 5. Two-dimensional arrays ===")
    marks = np.array([[78, 82, 91], [88, 76, 95], [69, 84, 80]])
    print("Marks table:\n", marks)
    print("Shape (rows, columns):", marks.shape)
    print("First student's marks:", marks[0])
    print("Second subject for every student:", marks[:, 1])
    print("Reshaped array (1 row, 9 columns):\n", marks.reshape(1, 9))

    print("\n=== 6. Aggregations ===")
    print("Total of all marks:", marks.sum())
    print("Overall mean:", marks.mean())
    print("Minimum mark:", marks.min())
    print("Maximum mark:", marks.max())
    print("Mean for each student (axis=1):", marks.mean(axis=1))
    print("Mean for each subject (axis=0):", marks.mean(axis=0))


if __name__ == "__main__":
    main()
