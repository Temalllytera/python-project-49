import random
import math


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')

    correct_answers_count = 0

    while correct_answers_count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ").strip()

        try:
            user_answer = int(user_answer)
        except ValueError:
            user_answer = None

        correct_answer = math.gcd(num1, num2)

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
