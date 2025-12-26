def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False

def capitalize_words(text):
    return text.capitalize()