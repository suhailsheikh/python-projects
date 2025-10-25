questions = {
    1: 'Who directed the Titanic?',
    2: 'Which actor plays the character Neo in The Matrix?',
    3: 'What year does Marty McFly travel to in Back to the Future?',
    4: 'What is the name of the fictional wizarding school in Harry Potter?',
    5: 'Which actor played the character Forrest Gump?',
    6: 'In which movie does the quote "May the Force be with you" originate?',
    7: 'What is the name of the fictional African country in Black Panther?',
    8: 'Who directed The Dark Knight?',
    9: 'What is the name of the island where Jurassic Park is located?',
    10: 'Which movie won the Oscar for Best Picture in 1994?'
}

answers = {
    1: ['James Cameron', 'Steven Spielberg', 'Ron Howard'],
    2: ['Will Smith', 'Laurence Fishburne', 'Keanu Reeves'],
    3: ['1985', '1955', '2015'],
    4: ['Beauxbatons', 'Durmstrang', 'Hogwarts'],
    5: ['Robin Williams', 'Tom Hanks', 'Matthew McConaughey'],
    6: ['Star Wars', 'Star Trek', 'Battlestar Galactica'],
    7: ['Wakanda', 'Zamunda', 'Elbonia'],
    8: ['Tim Burton', 'Christopher Nolan', 'Sam Raimi'],
    9: ['Isla Isla', 'Isla de los Muertos', 'Isla Nublar'],
    10: ['Pulp Fiction', 'The Shawshank Redemption', 'Forrest Gump'],
}

question_answer_mappings = {
    1 : 1,
    2 : 3,
    3 : 2,
    4 : 3,
    5 : 2,
    6 : 1,
    7 : 1,
    8 : 2,
    9 : 3,
    10: 3
}

score = 0
answer_choice = ''

for question_number, question in questions.items():
    print(question)

    # Display all answers for this question
    for i, answer in enumerate(answers[question_number], start=1):
        print(f'{i}. {answer}')

    # Continuously prompt the user until they enter a valid answer
    while True:
        answer_choice = input('Enter the number (1, 2, or 3) corresponding to your answer choice: ')

        # Check if the input is valid (either 1, 2, or 3)
        if answer_choice.isdigit() and int(answer_choice) in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter either 1, 2, or 3.")

    # Check if the answer is correct
    actual_answer = question_answer_mappings[question_number]

    if int(answer_choice) == actual_answer:
        score += 1
        print('Correct answer!')
    else:
        index = question_answer_mappings[question_number]
        selected_answer = answers[question_number][index - 1]
        print(f'Wrong! The actual answer is: {selected_answer}')

print(f'Your final score: {score}/{len(questions)}'.upper())