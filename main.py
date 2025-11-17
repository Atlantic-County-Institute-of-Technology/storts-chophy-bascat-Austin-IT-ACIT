import random
import inquirer3
import os

WORD_LENGTH = 5
WORD_LIST = []
change_liv = 5
password_correct = False
temp_liv = change_liv


# creaters all the avalible words in the txt file and make them there own string
def generate_number_list():
    global WORD_LIST
    global WORD_LENGTH
    WORD_LIST = []
    with open('assets/words_alpha.txt', 'r') as dictionary:
        for word in dictionary.readlines():
            if len(word.strip()) == WORD_LENGTH:
                WORD_LIST.append(word.strip())
    return WORD_LIST


# DEV MODE is to help fix issues with code
def dev_mode():
    # checks the password for dev mode from a txt file
    with open('assets/password.txt', 'r') as password:
        content = password.read()

        # ask the user for the password
    password_guess = input("What is the admin password - ")

    # if the password is correct it will let you in dev mode
    if password_guess == content:
        global password_correct
        print("Right password")
        password_correct = True
        os.system('cls' if os.name == 'nt' else 'clear')
        return password_correct
        
    # if the password is wrong it will give you the option to try again or go back to the main menu``
    else:
        print("Wrong password")
        diff = prompt_list_message("Please choose an option:", [" [-] Try Password Again", " [-] Back to Main Menu"])
        match diff:
            case " [-] Try Password Again":
                dev_mode()
            case " [-] Back to Main Menu":
                main()


# have the ability to change the amount of letters per word for the wordle
def change_diff():
    global target
    global WORD_LENGTH

    # prompt the user to choose a difficulty
    diff = prompt_list_message("Please choose an option:", [" [-] Easy - 3 letter words", " [-] Medium - 5 letter words"
                               , " [-] Hard - 10 letter words"])
    match diff:

        # set the word length based on the users choice
        case " [-] Easy - 3 letter words":
            WORD_LENGTH = 3
            return WORD_LENGTH
        case " [-] Medium - 5 letter words":
            WORD_LENGTH = 5
            return WORD_LENGTH
        case " [-] Hard - 10 letter words":
            WORD_LENGTH = 10
            return WORD_LENGTH


# change how many lives you have when doing the worlde
def change_lives():
    global WORD_LENGTH
    global change_liv
    global temp_liv

    # prompt the user to choose how many lives they want
    diff = prompt_list_message("Please choose an option:", [" [-] 3 lives", " [-] 5 lives", " [-] 10 lives", " [-] Custom"])
    match diff:
        case " [-] 3 lives":
            change_liv = 3
            temp_liv = change_liv
            return change_liv
        case " [-] 5 lives":
            change_liv = 5
            temp_liv = change_liv
            return change_liv
        case " [-] 10 lives":
            change_liv = 10
            temp_liv = change_liv
            return change_liv
        case " [-] Custom":
            # ask the user for a custom amount of lives
            change_liv = int(input("Input custom amount of lives"))
            temp_liv = change_liv
            return change_liv


# code when playing the game wordle
def play_code():
    global WORD_LIST
    global change_liv
    global temp_liv
    global lives
    global target

    # start the game loop
    while lives > 0:
        print(f"You have {lives} lives")
        if password_correct:
            print(f"the word is {target}")
        print(f"Please enter your {WORD_LENGTH} letter guess")
        guess = input(f"")
        while len(guess) < len(target) or len(guess) > len(target):
            print("You have entered a word with more or less then 5 letters")
            print(f"Please enter your {WORD_LENGTH} letter guess")
            guess = input(f"")
        else:
            response = ["Bascat" for i in range(len(target))]

            # check if the guess is correct, if it is then the user wins
            if guess == target:
                print("you have got the 3 digit number")
                print(" [-] You have Won!")

                # give the user the option to try again, go to the main menu, or exit the code
                response = prompt_list_message("Please choose an option:",
                                               [" [-] Try Again", " [-] Main Menu", " [-] Exit Code"])
                match response:
                    case " [-] Try Again":
                        lives = temp_liv
                        target = WORD_LIST[random.randint(0, len(WORD_LIST))]
                        play_code()
                    case " [-] Exit Code":
                        exit()
                    case " [-] Main Menu":
                        main()

            # if the guess is incorrect, check each letter and give feedback
            else:
                lives -= 1
                for g_digit in range(len(guess)):
                    for t_digit in range(len(target)):
                        if guess[g_digit] == target[t_digit]:
                            if g_digit == t_digit:
                                response[g_digit] = "Chophy"
                            else:
                                response[g_digit] = "Storts"
            print(response)

    # if the user runs out of lives code runs
    if lives == 0:
        print(" [-] You have lost")
        print(f"The Word was {target}")
        # give the user the option to try again, go to the main menu, or exit the code
        response = prompt_list_message("Please choose an option:",
                                       [" [-] Try Again", " [-] Main Menu", " [-] Exit Code"])
        match response:
            case " [-] Try Again":
                lives = temp_liv
                target = WORD_LIST[random.randint(0, len(WORD_LIST))]
                play_code()
            case " [-] Exit Code":
                exit()
            case " [-] Main Menu":
                main()


# for inquirer3, when switching to a selected option
def prompt_list_message(in_message, in_choices):
    # prompt question from input
    question = [
        inquirer3.List(
            "choice",
            message=in_message,
            choices=in_choices,
        ),
    ]
    # parse and return the response
    answer = inquirer3.prompt(question)
    # clears the terminal on both windows and linux
    os.system('cls' if os.name == 'nt' else 'clear')
    return answer["choice"]


# the main code for the main menu
def main():
    global password_correct
    global change_liv
    global WORD_LIST
    global lives
    global target
    
    WORD_LIST = generate_number_list()
    target = WORD_LIST[random.randint(0, len(WORD_LIST))]

    # main menu loop
    while True:
        # set the lives to the changed lives
        lives = change_liv
        # debugging info for dev mode
        if password_correct:
            print(f"the word is {target}")
        print(f"you have {lives} lives")
        # prompt the user to choose an option from the main menu
        response = prompt_list_message("Please choose an option:",
                                       [" [-] Exit", " [-] DEV MODE", " [-] Change Word", " [-] Change lives",
                                        " [-] Change Difficulty", " [-] PLAY"])
        match response:
            case " [-] Exit":
                print("Goodbye!")
                exit()
            case " [-] Change Difficulty":
                # enable changing the difficulty menu
                change_diff()
                # regenerate the word list and pick a new target word
                WORD_LIST = generate_number_list()
                target = WORD_LIST[random.randint(0, len(WORD_LIST))]
            case " [-] Change Word":
                # regenerate the word list and pick a new target word
                WORD_LIST = generate_number_list()
                main()
            case " [-] Change lives":
                # enable changing the lives menu
                change_liv = change_lives()

            case " [-] DEV MODE":
                # enable dev mode
                if password_correct:
                    # toggle dev mode off if already enabled
                    password_correct = not password_correct
                else:
                    dev_mode()
            case " [-] PLAY":
                # start the game
                play_code()




if __name__ == '__main__':
    main()
