import random
user_name = input("Please enter name: ")

answer = random.randint(1,100)
guesses_allowed = 5
guesses = 0


while True:
    guess_number = input("Please guess a number: ")
    try:
        guess_number = int(guess_number)
        guesses += 1
        break
    except:
        print("Please enter an integer.")
   


while guess_number != answer and guesses < guesses_allowed:
    if guess_number > answer:
        print("Too High")
        guesses += 1
   
    elif guess_number < answer:
        print("Too Low")
        guesses += 1

    while True:
        new_guess = input("Guess Again: ")
        try:
            guess_number = int(new_guess)
            break
        except:
            print("Please enter integer.")
    
if guess_number == answer:
    print("You got it!")
else:
    print("You reached the guess limit.")

print(f'You have reach {guesses} guesses. Thanks for trying.')
        


