import random
randNumber = random.randint(1, 100)
print(randNumber)
guesses = 0
userGuess = None


while(userGuess != randNumber):
    userGuess = int(input("Enter your guess : "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it Right .!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong ! Enter a smaller number")
        else:
            print("You guessed it wrong ! Enter a larger number ")

print(f"You got the right answer in {guesses} guesses")

with open("GuessgameScore.txt", 'r') as f:
    hiscore = int(f.read())


if (guesses < hiscore):
    print("You have just broken the highscore of this Game.!")
    with open("GuessgameScore.txt", 'w') as f:
        f.write(str(guesses))
