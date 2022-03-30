import random
print("You have to choose the num from 1 to 10")
a = int(random.randint(1, 10))
def choose():
    x=input("Your num: ")
    if x==a:
        print("Cool, you guess it")
    else:
        b=input("Oh, you lose. Play again? y/n ")
    if b=="y":
        return a
        choose()
    if b=="n":
        print("okay:(")
choose()
