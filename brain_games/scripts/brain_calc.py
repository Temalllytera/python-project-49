import random
import operator


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    correct_answers_count = 0

    while correct_answers_count < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        op = random.choice(list(operators.keys()))

        question = f"{num1} {op} {num2}"
        correct_answer = operators[op](num1, num2)

        print(f"Question: {question}")
        try:
            user_answer = int(input("Your answer: ").strip())
        except ValueError:
            user_answer = None

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