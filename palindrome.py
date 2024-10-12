def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is not a palindrome.')
