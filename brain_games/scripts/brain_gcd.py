import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0
    rounds = 3

    for _ in range(rounds):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        user_answer = int(input("Your answer: "))
        correct_answer = gcd(num1, num2)

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            break

    if correct_answers == rounds:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()