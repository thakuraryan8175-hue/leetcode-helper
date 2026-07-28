"""
AI-LeetCode-Mentor
Example: Palindrome Check Problem
"""


def is_palindrome(text):

    cleaned = text.lower().replace(" ", "")

    return cleaned == cleaned[::-1]


if __name__ == "__main__":

    word = "racecar"

    result = is_palindrome(word)

    print("Input:", word)
    print("Palindrome:", result)
