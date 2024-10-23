import random
import operator
from brain_games.engine import game_loop

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(list(operators.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = str(operators[op](num1, num2))
    return question, correct_answer


def validate_answer(user_answer, correct_answer):
    try:
        return int(user_answer) == int(correct_answer)
    except ValueError:
        return False


def main():
    rules = 'What is the result of the expression?'
    game_loop(rules, generate_question, validate_answer)


if __name__ == "__main__":
    main()
