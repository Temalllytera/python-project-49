from brain_games.cli import welcome_user


def game_loop(rules, generate_question, validate_answer):
    name = welcome_user()
    print(rules)

    correct_answers_count = 0

    while correct_answers_count < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if validate_answer(user_answer, correct_answer):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
