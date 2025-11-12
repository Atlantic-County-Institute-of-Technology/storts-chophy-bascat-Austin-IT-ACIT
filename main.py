import random

MIN_VAL = 100
MAX_VAL = 999


def generate_number_list():
    value = random.randint(MIN_VAL, MAX_VAL)
    print(value)
    return str(value)


def main():

    value = generate_number_list()
    x = 0
    y = 0
    guess = input("Please enter your 3 digit number here")
    response = ["Bascat" for i in range(len(value))]

    if guess == value:
        print("you have got the 3 digit number")
    else:
        for g_digit in range(len(guess)):
            for t_digit in range(len(value)):
                print(f" the guess number {guess[g_digit]} || the target number {value[t_digit]}")
                if guess[g_digit] == value[t_digit]:
                    if g_digit == t_digit:
                        response[g_digit] = "Chophy"
                    else:
                        response[g_digit] = "Storts"
    print(response)


if __name__ == '__main__':
    main()