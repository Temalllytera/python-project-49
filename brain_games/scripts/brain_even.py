import random
from brain_games.engine import game_loop


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer


def validate_answer(user_answer, correct_answer):
    return (user_answer in ["yes", "no"] and
            user_answer == correct_answer)


def main():
    rules = 'Answer "yes" if the number is even,' \
            ' otherwise answer "no".'
    game_loop(rules, generate_question, validate_answer)


if __name__ == "__main__":
    main()
