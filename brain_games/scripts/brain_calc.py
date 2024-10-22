from brain_games.cli import welcome_user
import random
import operator


def generate_question(operators):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(list(operators.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = operators[op](num1, num2)
    return question, correct_answer


def get_user_answer():
    try:
        return int(input("Your answer: ").strip())
    except ValueError:
        return None


def main():
    name = welcome_user()
    print('What is the result of the expression?')

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    correct_answers_count = 0

    while correct_answers_count < 3:
        question, correct_answer = generate_question(operators)

        print(f"Question: {question}")
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

