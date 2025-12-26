def welcome():
    print("🧪 Welcome to the Python Interview Prep Quiz Game!")
    print("-" * 50)


def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        print(f"a) {q['options']['a']}")
        print(f"b) {q['options']['b']}")
        print(f"c) {q['options']['c']}")
        print(f"d) {q['options']['d']}")

        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'")

    return score


def show_result(score, total):
    print("\n" + "🎯" * 10)
    print(f"🎯 Your Final Score: {score}/{total}")

    if score >= 15:
        print("🎉 Excellent! You are interview ready!")
    elif score >= 10:
        print("👍 Good job! Keep practicing!")
    else:
        print("📘 Needs more practice. Don’t give up!")


questions = [
    {
        "question": "Why is Python called dynamically typed?",
        "options": {
            "a": "Variables need explicit type declaration",
            "b": "Type is decided at runtime",
            "c": "It runs very fast",
            "d": "It uses bytecode"
        },
        "answer": "b"
    },
    {
        "question": "Why is Python considered an interpreted language?",
        "options": {
            "a": "It does not compile",
            "b": "It executes line by line source code",
            "c": "Bytecode is executed by PVM",
            "d": "It uses only C compiler"
        },
        "answer": "c"
    },
    {
        "question": "What best describes Python’s execution model?",
        "options": {
            "a": "Only compiled",
            "b": "Only interpreted",
            "c": "Compiled to bytecode then interpreted",
            "d": "Direct machine execution"
        },
        "answer": "c"
    },
    {
        "question": "Why is Python slower than C/C++?",
        "options": {
            "a": "Uses dynamic typing",
            "b": "Runs on virtual machine",
            "c": "Interpreted at runtime",
            "d": "All of the above"
        },
        "answer": "d"
    },
    {
        "question": "What is the Global Interpreter Lock (GIL)?",
        "options": {
            "a": "Locks files",
            "b": "Allows only one thread to execute Python bytecode",
            "c": "Improves multithreading",
            "d": "Manages memory"
        },
        "answer": "b"
    },
    {
        "question": "Why are Python variables references to objects?",
        "options": {
            "a": "For faster execution",
            "b": "For memory efficiency and flexibility",
            "c": "To avoid garbage collection",
            "d": "To reduce syntax"
        },
        "answer": "b"
    },
    {
        "question": "How does Python handle small integers internally?",
        "options": {
            "a": "Creates new object every time",
            "b": "Caches small integers",
            "c": "Deletes immediately",
            "d": "Stores on disk"
        },
        "answer": "b"
    },
    {
        "question": "Why is everything an object in Python?",
        "options": {
            "a": "To simplify language design",
            "b": "To support OOP features",
            "c": "For consistency",
            "d": "All of the above"
        },
        "answer": "d"
    },
    {
        "question": "What does the id() function return?",
        "options": {
            "a": "Object value",
            "b": "Memory address of object",
            "c": "Type of object",
            "d": "Object size"
        },
        "answer": "b"
    },
    {
        "question": "How does Python handle a = b = c = 5?",
        "options": {
            "a": "Creates three objects",
            "b": "Creates one object with three references",
            "c": "Causes error",
            "d": "Copies value three times"
        },
        "answer": "b"
    },
    {
        "question": "What is string interning?",
        "options": {
            "a": "Encrypting strings",
            "b": "Reusing immutable string objects",
            "c": "Deleting unused strings",
            "d": "Converting to bytes"
        },
        "answer": "b"
    },
    {
        "question": "What executes Python bytecode?",
        "options": {
            "a": "CPU directly",
            "b": "Python Compiler",
            "c": "Python Virtual Machine",
            "d": "Operating System"
        },
        "answer": "c"
    },
    {
        "question": "How is memory managed in Python?",
        "options": {
            "a": "Manual allocation",
            "b": "Using malloc only",
            "c": "Private heap space",
            "d": "Stack memory only"
        },
        "answer": "c"
    },
    {
        "question": "What is reference counting?",
        "options": {
            "a": "Counting variables",
            "b": "Tracking object references",
            "c": "Tracking memory blocks",
            "d": "Counting threads"
        },
        "answer": "b"
    },
    {
        "question": "What is PyMalloc?",
        "options": {
            "a": "Garbage collector",
            "b": "Python memory allocator",
            "c": "Thread manager",
            "d": "Compiler"
        },
        "answer": "b"
    },
    {
        "question": "What can cause memory leaks in Python?",
        "options": {
            "a": "Circular references",
            "b": "Global variables",
            "c": "C extensions",
            "d": "All of the above"
        },
        "answer": "d"
    },
    {
        "question": "How does GC detect cyclic references?",
        "options": {
            "a": "Reference counting",
            "b": "Generational algorithm",
            "c": "Stack scanning",
            "d": "Manual cleanup"
        },
        "answer": "b"
    },
    {
        "question": "What is the role of gc module?",
        "options": {
            "a": "Control garbage collection",
            "b": "Free memory manually",
            "c": "Optimize code",
            "d": "Debug syntax"
        },
        "answer": "a"
    },
    {
        "question": "How do mutable and immutable objects differ?",
        "options": {
            "a": "Mutable objects change memory location",
            "b": "Immutable objects cannot change",
            "c": "Mutable objects allow in-place modification",
            "d": "Both b and c"
        },
        "answer": "d"
    },
    {
        "question": "Why is None a singleton in Python?",
        "options": {
            "a": "To save memory",
            "b": "To represent absence of value",
            "c": "For consistency",
            "d": "All of the above"
        },
        "answer": "d"
    }
]


welcome()
score = run_quiz(questions)
show_result(score, len(questions))