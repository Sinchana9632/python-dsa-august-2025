"""
📌 Program: Check if a string is Palindrome
📌 Date: 2025-08-16
📌 Author: sinchana 
"""

def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# ✅ Example Test
if __name__ == "__main__":
    word = "madam"
    if is_palindrome(word):
        print(f"'{word}' is a palindrome ✅")
    else:
        print(f"'{word}' is NOT a palindrome ❌")
