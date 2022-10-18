import random
#taking inputs
low = 1
high = 9
x = random.randint(low, high)
guess = None
#guess = int(input("Guess number:-"))
while guess != x:
    guess = int(input("Guess number btw 1 to 9:-"))
    if guess == x:
        print("YOU WON")
        exit(0)
    elif guess < x:
        print("guess is too low")
    elif guess > x:
        print("guess is too high")



