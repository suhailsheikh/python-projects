def check_palindrome(word):
    word = word.lower()
    reverse = word[::-1]

    if word == reverse:
        print(f'The word "{word}" is a palindrome!')
    else:
        print('This is not a palindrome.')