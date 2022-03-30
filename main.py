import random
print("You have to choose the num from 1 to 10")

def choose():
    a = int(random.randint(1, 10))
    x=input("Your num: ")

    if x!=a:
        print("Oh, you lose.")
        print("Your num was: ", a)
        b = input("Play again? (y/n) ")

    else:
        print("Cool, you guess it")
        b = input("Play again? (y/n) ")

    if b == "y":
        choose()
    if b == "n":
        print("okay:(")
choose()
