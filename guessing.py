import random

def play_guessing():
    print("********************************")
    print("****Welcome to Guessing Game!***")
    print("********************************")

    points = 1000
    secret_number = random.randrange(1,101)
    attempts = 0

    print("Select level:")
    print("(1) Easy (2) Medium (3) Hard")
    level = int(input("Choose level"))

    if(level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5

    for turn in range(1, attempts +1):
        print("Attempt {} of {}".format(turn, attempts))
        guess_str = input("Type a number between 1 and 100:")
        print("You typed ", guess_str)
        guess = int(guess_str)

        if(guess < 1 or guess > 100):
            print("You must type a number bettwen 1 and 100!")
            continue

        hit     = secret_number == guess
        bigger  = secret_number < guess
        smaller = secret_number > guess

        if (hit):
            print("You hit! You done {} points!".format(points))
            break
        else:
            if(bigger):
                print("You Missed! The secret number is smaller")
            elif (smaller):
                print("You Missed! The secret number is bigger")
            missed_points = abs(secret_number - guess)
            points = points - missed_points
        attempts = attempts + 1

    print("End of Game")
if(__name__ == "__main__"):
    play_guessing()

    


