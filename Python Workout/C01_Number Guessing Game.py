from random import randint

def validate(userInput):
    # take off the 
    userInput = userInput.strip()
    try:
        userInput = int(userInput)
        if userInput >= 0:
            return True
        else:
            print("You need to enter a positive integer!")
            return False
    except:
        print("You need to enter a positive integer!")
        return False

def main():
    target = randint(0, 100)
    guess = input("Guess a number!")
    while guess != target:
        if validate(guess):
            guess = int(guess)
            if guess == target:
                print("Right On!")
                break
            elif guess > target:
                print("Too high!")
            elif guess < target:
                print("Too low!")

        guess = input("Guess a number!")



if __name__ == "__main__":
    main()