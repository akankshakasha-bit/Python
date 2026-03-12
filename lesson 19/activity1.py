import random
playing = True
number = random.randint(10,20)
while playing:
    guess = int(input("Give me your best guess \n"))
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right, try again. \n")