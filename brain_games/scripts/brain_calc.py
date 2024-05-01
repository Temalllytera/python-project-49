def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answers_count = 0

    while correct_answers_count < 3:
        expression = input("Enter a mathematical expression: ")
        user_answer = input("Your answer: ")

        correct_answer = calculate(expression)

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
