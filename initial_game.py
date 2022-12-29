import random
import  sqlite3

def new_user():
    data = sqlite3.connect("database.db")
    csr = data.cursor()
    csr.execute("""CREATE TABLE IF NOT EXISTS users(
        nickname DATATYPE text PRIMARY KEY,
        first_name DATATYPE text,
        last_name DATATYPE text,
        age DATATYPE integer
        )""")

    data.commit()
    data.close()

    data = sqlite3.connect("database.db")
    csr = data.cursor()
    user_items = []

    nick_name = input("Please insert nickname: ")
    first_name = input("Please insert first name: ")
    last_name = input("Please insert last name: ")
    age = int(input("Please insert your age: "))
    if age<18:
        print("You have to be over 18 to play this game!")
        return False
    user_items.append((nick_name, first_name, last_name, age))

    csr.executemany(""" INSERT OR IGNORE INTO users VALUES(?,?,?,?)""", user_items)
    print("Your registration is successful!")
    data.commit()
    data.close()
    return nick_name

def number_guesses():
    username=user()
    if username:
        guessing_number = input(f"How many times you would like to guess {username} ?(max 10):")
        while not guessing_number.isdigit() or int(guessing_number) > 10:
            print("WRONG Input!.Maximum 10 guesses.\nPlease enter again", end=" ")
            guessing_number = input("how many time you would like to guess?:")
        return int(guessing_number)
    else:
        return False
def money():
    my_money = int(input("Please enter your bid $:"))

    return my_money
def user():

    print("Have you play before?")
    ansewer=input()
    if ansewer=="no":
        username=new_user()

    else:
        print("Please enter your user name:", end=" ")
        username=input()
    return username

def guessing():
    computer_number = random.randint(1, 100)
    number_of_guesses=0
    is_guessed = False
    guessing_number = number_guesses()
    if guessing_number:
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