import random
import math
from brain_games.engine import game_loop


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer


def validate_answer(user_answer, correct_answer):
    try:
        return int(user_answer) == int(correct_answer)
    except ValueError:
        return False


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    game_loop(rules, generate_question, validate_answer)


if __name__ == "__main__":
    main()
