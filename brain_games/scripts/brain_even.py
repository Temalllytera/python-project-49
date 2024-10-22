from brain_games.cli import welcome_user
import random


def is_even(number):
    return number % 2 == 0


def ask_question(number):
    print(f"Question: {number}")
    return input("Your answer: ").strip().lower()


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        user_answer = ask_question(number)

        if check_answer(user_answer, correct_answer, name):
            correct_answers_count += 1
        else:
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
