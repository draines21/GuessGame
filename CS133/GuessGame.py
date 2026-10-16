import random
user_name = input("Please enter name: ")

print(f"Welcome, {user_name}! Try to guess the number.")

def guessgame(answer):
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
        return True
    else:
        print("You reached the guess limit. Thank you for playing.2")
        return False


def main():
    answers = [50, 15, 25, 64, 99]

    for number in answers:
       if guessgame(number):
           break
main()
        


