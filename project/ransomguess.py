import random
Cnumber=random.randrange(1,100)

while True:
    userInput = int(input("Enter your number:"))

    if userInput>Cnumber:
        print("your number is too high")
    elif userInput<Cnumber:
        print("yout number is too low")
    else :
        print("you are right")
        break