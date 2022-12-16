import random


def number_guesses():
    username=user()
    guessing_number = input(f"How many times you would like to guess {username} ?(max 10):")
    while not guessing_number.isdigit() or int(guessing_number) > 10:
        print("WRONG Input!.Maximum 10 guesses.\nPlease enter again", end=" ")
        guessing_number = input("how many time you would like to guess?:")
    return int(guessing_number)
def money():
    my_money = int(input("Please enter your bid $:"))

    return my_money
def user():
    username_dat={}
    print("Have you play before?")
    ansewer=input()
    while ansewer=="yes":
        print("Please enter your user name:",end=" ")
        username=input()
        if username not in username_dat.keys():
            print(f"The user name doesn't exist")
            print("Do you want to create username?")
            answer=input()
            if answer=="yes":
                break



    print("Please create username:",end=" ")
    username=input()
    # if username in username_dat.keys:
    #     print("The user name is taken")
    #     username=input()

    print(f"How much money you are ready to deposit in your account {username}?")
    momey_account = input()
    username_dat[username]=momey_account

    return username

def guessing():
    computer_number = random.randint(1, 100)
    number_of_guesses=0
    is_guessed = False
    guessing_number = number_guesses()
    my_money=money()
    my_money_profit = my_money
    my_number = input("Please guess a number between 1 and 100:")
    if my_number == str(computer_number):
        is_guessed = True
    else:

        while not my_number.isdigit() or int(my_number) > 100 or int(my_number) < 1:
            number_of_guesses += 1
            print("WRONG Input!. Please guess again:", end=" ")
            if number_of_guesses == guessing_number:
                break
            my_number = input()

        for current_guess in range(1, guessing_number):

            if number_of_guesses >= guessing_number:
                break
            number_of_guesses += 1
            my_number = int(my_number)
            my_money_profit = (my_money / guessing_number) * 10 * 1.2

            if my_number > computer_number:

                if my_number - computer_number > 50:
                    print("Your number is much higher!\nPlease guess again:", end=" ")
                else:
                    print("Your number is higher!\nPlease guess again:", end=" ")

            elif my_number < computer_number:

                if computer_number - my_number > 50:
                    print("Your number is much lower!\nPlease guess again:", end=" ")
                else:
                    print("Your number is low!\nPlease guess again:", end=" ")
            else:
                print()
                print(f"Congratulation!You won ${my_money_profit}")
                is_guessed = True
                break
            my_number = input()
            while not my_number.isdigit() or int(my_number) > 100 or int(my_number) < 1:
                number_of_guesses += 1
                print("WRONG Input!. Please guess again:", end=" ")
                if number_of_guesses >= guessing_number:
                    break
                my_number = input()

    if not is_guessed:
        print("Game Over!")
        print(f"You LOST ${my_money}")
        print(f"Winning number is {computer_number}")

    elif is_guessed and guessing_number == 1:

        print(f"Congratulation!You won ${my_money_profit * 10}")

guessing()