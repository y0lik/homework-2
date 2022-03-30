import random
print("You have to choose the num from 1 to 10")
def choose():
    a = random.randint(1, 10)
    x=input(Your num: )
    if x=a:
        print("Cool, you guess it")
    else:
        b=input(Play again? y/n)
    if b="y":
        choose()
    if b="n":
        break