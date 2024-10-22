from brain_games.cli import welcome_user
import random


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    return number


def get_user_answer():
    return input("Your answer: ").lower().strip()


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        prime_status = "prime" if correct_answer == "yes" else "not prime"
        print(f"Wrong answer ;(. The number is {prime_status}.")
        print(f"Let's try again, {name}!")
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = generate_question()
        user_answer = get_user_answer()

        correct_answer = "yes" if is_prime(number) else "no"

        if check_answer(user_answer, correct_answer, name):
            correct_answers_count += 1
        else:
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
