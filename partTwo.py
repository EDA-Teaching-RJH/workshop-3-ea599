import random

def main():
    shh = random.randint(1,10)
    guess = int(input("Guess a random number: "))
    print(hL(guess, shh))

def hL(x, y):
    if x > y:
        return "Too high"
    elif x < y:
        return "Too low"
    else:
        return "You guessed right"
    
main()