#Alan Ngo
import random
RANGE=10
def main():
#variables
    attempt=0
    number=random.randint(1,1000)
    #print(number)
    guess=int(input("Enter your number between 1-1000 "))
    while guess!=number:
        attempt+=1
#+10 range
        if guess==number+RANGE:
            print("Getting warmer but you're still too High!")
            guess=int(input("Enter your number "))
#-10 range
        elif guess==number-RANGE:
            print("Getting warmer but you're still too Low!")
            guess=int(input("Enter your number "))
        else:
            print("Keep Guessing!")
            guess=int(input("Enter your number "))
    print("You guessed correctly! The number was",number)
    print("You guessed ", attempt, "times")
    goAgain=input("Do you want to play again")
    if goAgain=="yes":
        main()
    else:
        exit()

#
main()
