game_library = {
    "Donkey Kong": {"quantity" : 3, "cost" : 2},
    "Super Mario" : {"quantity" : 5, "cost": 3},
    "Tetris" : {"quantity": 2, "cost": 1}
}

user_account = {}

admin_username = "admin"
admin_password = "adminpassword"

def main():
    print("Welcome to the Game Rental System")
    print("1. Display Available Game")
    print("2. Register User")
    print("3. Log In")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    while True:
        try:
            if choice == 1:
                available_games()
            if choice == 2:
                register()
            if choice == 3:
                log_in()
            if choice == 4:
                print("Exiting..")
                break
        except ValueError as e:
            print(e)


def available_games():
    print(game_library)

def register():
    print("Register")
    while True:
        try:
            username = input("Enter a username: ")
            balance = 0
            points = 0
            if not username:
                main()
            if username in user_account:
                print("Username already exist. Try another username")
                continue
            while True:
                try:
                    password = input("Enter a password (at least 8 characters): ")
                    if len(password) < 8:
                        print("Password too short")
                        continue
                    if len(password) > 8:
                        user_account[username] = {"password": password, "balance": balance}
                        print("Sign Up Successfully!")
                        main()
                    else:
                        print("Invalid Output!")
                        continue
                except ValueError as e:
                    print(e)
                    register()
        except ValueError as e:
            print(e)

def log_in():
    print("Log_in")
    while True:
        try:
            username = input("Enter a username: ")
            if not username:
                main()
            password = input("Enter a password (at least 8 characters): ")
            if user_account.get(username) and user_account[username]['password': password] == password:
                print("Log-In Successfully!")
                rentmain(username)
            else:
                print("Invalid username or password!")
        except ValueError as e:
            print(e)
            main()

def rentmain(username):
    print(f"Welcome to the Rental Game Store {username}")
    print("1. Rent Game")
    print("2. Return Game")
    print("3. Top-Up Account")
    print("4. Display Inventory")
    print("5. Redeem Free Game Rental")
    print("6. Check Points")
    print("7. Log-Out")
    choice = int(input("Enter your choice: "))

    while True:
        try:
            if choice == 1:
                rent(username)
            if choice == 2:
                return_game(username)
            if choice == 3:
                top_up(username)
            if choice == 4:
                display_inventory(username)
            if choice == 5:
                free_game(username)
            if choice == 6:
                check_points(username)
            if choice == 7:
                print("Exiting..")
                break
        except ValueError as e:
            print(e)


def rent(username):
    print("Rent a Game")
    print("Available Games: {game_library}")

    game_name = str(input("Select a Game: "))
    if not game_name:
        rentmain(username)
    if game_library[game_name]['quantity'] <= 0:
        print("Can't be rent!")
    if game_library[game_name]['quantity'] >= 0:
        print("1. Using Balance")
        print("2. Using Points")
        choice = int(input("Choose how to pay: "))

        if choice == 1: 
            if user_account[username]['balance'] <= 0:
                print("Not enough balance!")
                rent(username)
            else:
                user_account[username]['balance'] -= game_library[game_name]['cost']
                if game_library[game_name]['cost'] >= 2:
                    user_account[username]['points'] += 1
                    game_library[game_name]['quantity'] -= 1
                    print("You've successfully rented a game!")
        if choice == 2:
            if user_account[username]['points'] <= 0:
                print("Insufficient Balance!")
                rentmain(username)
            else:
                user_account[username]['points'] -= game_library[game_name]['cost']
        else:
            print("Invalid Output")
def return_game(username):
    print("Return Game")
    game_name = input("Enter the item you want to return: ")
    item_quantity = int(input("Enter the quantity you want to return"))
    game_library [game_name]['quantity']=item_quantity+game_library[game_name]['quantity']
    print("You've successfully returned the game")

def top_up(username):
    while True:
        try: 
            print("Top Up")
            print(f'Username: {username}, Current Balance: {user_account[username]}')

            amount = float(input("Enter the amount you want to top-up: "))
            user_account[username]['balance'] += amount
            print("Top Up was successful")
            print(f"New Balance: {user_account[username]['balance']}")
        
        except ValueError as e:
            print(e)



            


    

main()

