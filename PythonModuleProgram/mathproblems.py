import random
def addition():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    solution = num1 + num2
    try:
        answer = int(input(f"What is {num1} added by {num2}?: "))
        if answer == solution:
            print("You got the right answer!")
        else:
            print("You got the wrong answer")
    except:
        print("Please enter a number")
        
def subtraction():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    solution = num1 - num2
    try:
        answer = int(input(f"What is {num1} subtracted by {num2}?: "))
        if answer == solution:
            print("You got the right answer!")
        else:
            print("You got the wrong answer")
    except:
        print("Please enter a number")
        
def multiplication():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    solution = num1 * num2
    try:
        answer = int(input(f"What is {num1} multiplied by {num2}?: "))
        if answer == solution:
            print("You got the right answer!")
        else:
            print("You got the wrong answer")
    except:
        print("Please enter a number")
        
def division():
    num1 = round(random.uniform(1, 100), 1)
    num2 = round(random.uniform(1, 100), 1)
    solution = num1 / num2
    solution = round(solution, 1)
    try:
        answer = float(input(f"What is {num1} divided by {num2}?: "))
        if answer == solution:
            print("You got the right answer!")
        else:
            print("You got the wrong answer")
    except:
        print("Please enter a number")