import random
import sys


def generate_progression(length):
    start = random.randint(1, 20)
    diff = random.randint(1, 10)
    progression = [start + i * diff for i in range(length)]
    return progression


def hide_element(progression):
    missing_index = random.randint(0, len(progression) - 1)
    hidden_progression = progression[:]
    hidden_progression[missing_index] = '..'
    return hidden_progression, missing_index


def show_progression(progression):
    print("Question:", end=" ")
    for num in progression:
        print(num, end=" ")
    print()


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print("What number is missing in the progression?")

    correct_answers_count = 0

    while correct_answers_count < 3:
        progression_length = random.randint(5, 10)
        progression = generate_progression(progression_length)
        hidden_progression, missing_index = hide_element(progression)

        show_progression(hidden_progression)
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        correct_answer = progression[missing_index]

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break

    print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    main()
