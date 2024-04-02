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
    print("4. Admin Log-in")
    print("5. Exit")

def available_games():
    print("Available Games: {game_library}")

def register():
    print("Register")
    while True:
        try:
            username = input("Enter a username")
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
            username = input("Enter a username")
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
                    user_account[username]['points'] -= 1

        if choice == 2:
            if user_account[username]['points'] -= game_library[game_library]['cost']

def return_game():
    

main()