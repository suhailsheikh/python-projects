secret_word = 'castle' # Randomize this
used_letters = ''
guess_limit = 5
count = 0

hidden = ('_' * len(secret_word))
print(f'Your hidden word: {hidden}')

while count < guess_limit:
    user_input = input('Type in a letter: ')

    if user_input not in secret_word.lower():
        count += 1
        if (guess_limit - count) > 0:
            used_letters += user_input + ','
            print(f'Used letters: {used_letters.upper()}')
            print(f'You have {guess_limit - count} guesses remaining')
            print('\n')
    else:
        i = secret_word.index(user_input)
        hidden = hidden[:i] + user_input + hidden[i + 1:]
        print(f'{hidden}')

        if hidden == secret_word:
            print('You win!'.upper())
            break

    if count == guess_limit:
        print('You lost! Please try again.'.upper())
        break