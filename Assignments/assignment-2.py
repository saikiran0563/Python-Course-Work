# ------------------ INPUT SECTION -----------------------
n = int(input("Enter the no. of messages: "))
data = {}

messages = []        # stores all messages in order (name, msg)


for i in range(n):
    name, msg = input().split(':', 1)
    msg = msg.strip()

    messages.append((name, msg))

    if name in data:
        data[name].append(msg)
    else:
        data[name] = [msg]

# ------------------ FUNCTION DEFINITIONS -----------------------

def count_total_messages():
    return len(messages)

def unique_users():
    return list(data.keys())

def count_total_words():
    return sum(len(msg.split()) for _, msg in messages)

def average_words_per_message():
    return count_total_words() / len(messages)

def longest_message():
    return max(messages, key=lambda x: len(x[1]))

def most_active_user():
    return max(data, key=lambda user: len(data[user]))

def message_count_for_user(user):
    return len(data.get(user, []))

def most_frequent_word_user(user):
    words = []
    for msg in data.get(user, []):
        words.extend(msg.lower().split())

    if not words:
        return None

    from collections import Counter
    return Counter(words).most_common(1)[0]

def first_word_used_by_user(user):
    if user not in data or not data[user]:
        return None
    return data[user][0].split()[0]

def check_user_present(user):
    return user in data

def commonly_repeated_words():
    all_words = []
    for _, msg in messages:
        all_words.extend(msg.lower().split())

    from collections import Counter
    freq = Counter(all_words)
    return [w for w, c in freq.items() if c > 1]

def user_longest_avg_msg_length():
    return max(data, key=lambda user: sum(len(m) for m in data[user]) / len(data[user]))

def count_mentions(user):
    return sum(1 for _, msg in messages if user.lower() in msg.lower())

def remove_duplicates():
    seen = set()
    unique = []

    for pair in messages:
        if pair not in seen:
            unique.append(pair)
            seen.add(pair)

    return unique

def sort_messages_alpha():
    return sorted([msg for _, msg in messages])

def extract_questions():
    return [msg for _, msg in messages if msg.endswith('?')]

def reply_ratio(user1, user2):
    c1 = len(data.get(user1, []))
    c2 = len(data.get(user2, []))
    if c2 == 0:
        return "Undefined (division by zero)"
    return c1 / c2

def check_deleted_messages():
    # We assume a message is "deleted" if the user typed an empty message
    return [pair for pair in messages if pair[1].strip() == ""]


# ------------------ MENU SECTION -----------------------

choices = {
    1: 'Count total number of messages',
    2: 'Identify unique users in the chat',
    3: 'Count total number of words in the chat',
    4: 'Calculate average words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by specific user',
    9: 'Retrieve the first used word by a specific user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages',
    19: 'Exit'
}

while True:
    print("\n---------- MENU ----------")
    for i in choices:
        print(f"{i}. {choices[i]}")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Total messages:", count_total_messages())

    elif ch == 2:
        print("Unique users:", unique_users())

    elif ch == 3:
        print("Total words:", count_total_words())

    elif ch == 4:
        print("Average words/message:", average_words_per_message())

    elif ch == 5:
        print("Longest message:", longest_message())

    elif ch == 6:
        print("Most active user:", most_active_user())

    elif ch == 7:
        user = input("Enter user name: ")
        print("Message count:", message_count_for_user(user))

    elif ch == 8:
        user = input("Enter user name: ")
        print("Most frequent word:", most_frequent_word_user(user))

    elif ch == 9:
        user = input("Enter user name: ")
        print("First word:", first_word_used_by_user(user))

    elif ch == 10:
        user = input("Enter user name: ")
        print("User present?", check_user_present(user))

    elif ch == 11:
        print("Common repeated words:", commonly_repeated_words())
  
    elif ch == 12:
        print("User with longest average message:", user_longest_avg_msg_length())

    elif ch == 13:
        user = input("Enter user name: ")
        print("Mentions:", count_mentions(user))

    elif ch == 14:
        print("After removing duplicates:", remove_duplicates())

    elif ch == 15:
        print("Sorted messages:", sort_messages_alpha())

    elif ch == 16:
        print("Questions asked:", extract_questions())

    elif ch == 17:
        u1 = input("Enter user 1: ")
        u2 = input("Enter user 2: ")
        print("Reply ratio:", reply_ratio(u1, u2))

    elif ch == 18:
        print("Deleted messages:", check_deleted_messages())

    elif ch == 19:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")