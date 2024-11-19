import random
from brain_games.engine import game_loop

rules = 'Answer "yes" if given number is prime.' \
        ' Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    question = f"{number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def validate_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    game_loop(rules, generate_question, validate_answer)


if __name__ == "__main__":
    main()
