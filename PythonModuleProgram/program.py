print("Math module 0.1")
import mathproblems
running = True
while running:
    userchoice = input("Would you like to do Addition, Subtraction, Multiplication, or Division?: ")
    if userchoice == "Addition":
        mathproblems.addition()
        yesorno = input("Would you like to try another problem? Yes or No?: ")
        if yesorno == "Yes":
            continue
        else:
            exit()
    elif userchoice == "Subtraction":
        mathproblems.subtraction()
        yesorno = input("Would you like to try another problem? Yes or No?: ")
        if yesorno == "Yes":
            continue
        else:
            exit()
    elif userchoice == "Multiplication":
        mathproblems.multiplication()
        yesorno = input("Would you like to try another problem? Yes or No?: ")
        if yesorno == "Yes":
            continue
        else:
            exit()
    elif userchoice == "Division":
        mathproblems.division()
        yesorno = input("Would you like to try another problem? Yes or No?: ")
        if yesorno == "Yes":
            continue
        else:
            exit()
    else:
        print("Enter a valid operator")
        continue