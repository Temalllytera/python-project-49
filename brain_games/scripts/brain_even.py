def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = input("Enter a number: ")

        if not number.isdigit():
            print('Invalid input. Please enter a valid number.')
            continue

        number = int(number)
        user_answer = input("Answer: ").strip().lower()

        if user_answer in ('yes', 'no'):
            if (user_answer == "yes" and is_even(number)) or (user_answer == "no" and not is_even(number)):
                print("Correct!")
                correct_answers_count += 1
            else:
                correct_answer = "yes" if is_even(number) else "no"
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
