import random


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print("Question:", number)
        user_answer = input("Your answer: ").lower()

        if (user_answer == 'yes' and is_prime(number)) or (user_answer == 'no' and not is_prime(number)):
            print("Correct!")
            correct_answers_count += 1
        else:
            print("Wrong answer ;(. The number is {}prime.".format("" if is_prime(number) else "not "))
            print("Let's try again, {}!".format(name))
            break

    if correct_answers_count == 3:
        print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    main()