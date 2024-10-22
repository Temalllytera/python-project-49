from brain_games.cli import welcome_user
import random


def generate_progression(length):
    start = random.randint(1, 20)
    diff = random.randint(1, 10)
    return [start + i * diff for i in range(length)]


def hide_element(progression):
    missing_index = random.randint(0, len(progression) - 1)
    hidden_progression = progression[:]
    hidden_progression[missing_index] = '..'
    return hidden_progression, progression[missing_index]


def show_progression(progression):
    print("Question:", " ".join(map(str, progression)))


def get_user_answer():
    try:
        return int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return None


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
    print("What number is missing in the progression?")

    correct_answers_count = 0

    while correct_answers_count < 3:
        progression_length = random.randint(5, 10)
        progression = generate_progression(progression_length)
        hidden_progression, correct_answer = hide_element(progression)

        show_progression(hidden_progression)
        user_answer = get_user_answer()

        if user_answer is not None\
                and check_answer(user_answer, correct_answer, name):
            correct_answers_count += 1
        else:
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
