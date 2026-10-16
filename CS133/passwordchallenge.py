name = input("What is your name?")
print(f'Welcome {name}, please enter user information below.')


correct_username = "Dustin"
correct_password = "Oregon Ducks"


logged_in = False

while not logged_in:
    user_name = input("Please enter username: ")
    user_password = input("Please enter password: ")

    if user_name == correct_username and user_password == correct_password:
        print("You have logged in successfully.")
        logged_in = True

    else:
        print("Incorrect login, Im not mad just disappointed.")
        user_name = input("Please enter username again: ")
        user_password = input("Please enter password again: ")