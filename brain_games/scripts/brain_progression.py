import random
from brain_games.engine import game_loop

rules = 'What number is missing in the progression?'


def generate_question():
    start = random.randint(1, 20)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)
    missing_index = random.randint(0, length - 1)

    progression = [start + i * diff for i in range(length)]
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'

    question = " ".join(map(str, progression))
    return question, correct_answer


def validate_answer(user_answer, correct_answer):
    try:
        return int(user_answer) == int(correct_answer)
    except ValueError:
        return False


def main():
    game_loop(rules, generate_question, validate_answer)


if __name__ == "__main__":
    main()
