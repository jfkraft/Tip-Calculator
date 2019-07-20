print("Hello! Thank you for using Ad(just) the Tip, my free tip-calculating service. \n \n")
input('press enter to continue...')

pretax = float(input("What was the total amount before tax \n \n"))


serv = float(input("What service are you using? \n \n Select 1 for Rideshare \n Select 2 for Restaurant \n Select 3 for Delivery \n \n"))
if serv == 1:
    T = .10
if serv == 2:
    T = .15
if serv == 3:
    T = .20
elif serv > 3:
    print("Sorry, that is not an accepted value. Please start again.")
    import sys
    sys.exit()      



qual = float(input ("on a scale from 1-5, what was the quality of service you recieved \n \n"))
if qual == 1:
    Q = .25
if qual == 2:
    Q = .5
if qual == 3:
    Q = 1
if qual == 4:
    Q = 1.25
if qual == 5:
    Q = 1.5
    

elif qual > 5:
    print("Sorry, that is not an accepted value. Please start again.")
    import sys
    sys.exit()

    

print("Your calculated tipping percent is....\n")
print(int((Q*T)*100))




X = (Q*T)



chgval = input("Would you like to change it? \n")
if chgval == "yes":
    X = .01 * float(input("what would you like your tipping percent to be (integers only please!) \n"))
elif chgval != "yes":
    print()

        
F = ((X) * pretax) + pretax


print("Your total including tax is")
print(F)
