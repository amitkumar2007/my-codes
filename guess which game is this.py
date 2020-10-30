import random

print ("this is made by amit kumar jha")
b = random.randint(1, 100)
while(True):
    a = (int(input("enter a number")))

    if a<b :
        print("you guessed small")

    elif a>b:
        print("you guessed large")

    elif a == b:
        print("you win congratulations!")
        continue














