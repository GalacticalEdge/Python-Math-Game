import random
running = True
score = 0
while running:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num2moddiv = random.randint(1, 10)
    operation = random.randint(0, 4)
    if operation == 0:
        addanswer = num1 + num2
        addition = int(input(f"What is {num1} + {num2}?: "))
        if addition == addanswer:
            score += 1
            continue
        else:
            print("That was not the correct answer.")
            print(f"Your score was {score} points!")
            exit()
    if operation == 1:
        subanswer = num1 - num2
        subtraction = int(input(f"What is {num1} - {num2}?: "))
        if subtraction == subanswer:
            score += 1
            continue
        else:
            print("That was not the correct answer.")
            print(f"Your score was {score} points!")
            exit()
    if operation == 2:
        multanswer = num1 * num2
        multiplication = int(input(f"What is {num1} x {num2}?: "))
        if multiplication == multanswer:
            score += 1
            continue
        else:
            print("That was not the correct answer.")
            print(f"Your score was {score} points!")
            exit()
    if operation == 3:
        divanswer = num1 / num2moddiv
        divanswer = round(divanswer)
        division = int(input(f"What is {num1} / {num2moddiv}?: "))
        if division == divanswer:
            score += 1
            continue
        else:
            print("That was not the correct answer.")
            print(f"Your score was {score} points!")
            exit()
    if operation == 4:
        modanswer = num1 % num2moddiv
        modanswer = round(modanswer)
        modulus = int(input(f"What is the remainder of {num1} and {num2moddiv}?: "))
        if modulus == modanswer:
            score += 1
            continue
        else:
            print("That was not the correct answer.")
            print(f"Your score was {score} points!")
            exit()