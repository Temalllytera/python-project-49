from brain_games.cli import welcome_user
import random
import math


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"Question: {num1} {num2}")
    correct_answer = math.gcd(num1, num2)
    return correct_answer


def get_user_answer():
    try:
        return int(input("Your answer: ").strip())
    except ValueError:
        return None


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    correct_answers_count = 0

    while correct_answers_count < 3:
        correct_answer = generate_question()
        user_answer = get_user_answer()

        if check_answer(user_answer, correct_answer, name):
            correct_answers_count += 1
        else:
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
