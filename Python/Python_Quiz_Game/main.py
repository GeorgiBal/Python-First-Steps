def new_game():
    guesses = []
    correct_guesses = 0
    num_questions = 0

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[num_questions]:
            print(i)
        guess = input("Enter guess(A, B, C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        num_questions += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("Results")
    print("--------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.lower()
    if response == "yes":
        return True
    else:
        return False


questions = {
    "Who is Messi?: ": "A",
    "Man U is a: ": "C",
    "Europe is a: ": "B",
    "Thw biggest animal is: ": "A"
}

options = [
    ["A. Footballer", "B. Builder", "C. Random guy"],
    ["A. Food", "B. Restaurant", "C. Football team"],
    ["A. Country", "B. Continent", "C. Tree"],
    ["A. Whale", "B. Lion", "C. You"]
]

new_game()

while play_again():
    new_game()

print("Bye, bye!")
