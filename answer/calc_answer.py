def greetUser():
    print("Hello! Thank you for using Ad(just) the Tip, my free tip-calculating service. \n \n")
    input('press enter to continue...')

def promptForBill():
    while 1:
        try:
            pretax = float(input("What was the total amount before tax: "))
            return pretax
        except ValueError as v:
            print("ERROR: Amount must be a number.")

def promptForService():
    serv = -1
    while 1:
        try:
            print("What service are you using?")
            print("     - Select 1 for Rideshare")
            print("     - Select 2 for Retaurant")
            print("     - Select 3 for Deliverie")
            serv = int(input("Your selection: "))
            if(serv != 1 and serv != 2 and serv != 3):
                raise ValueError
            break
        except ValueError as e:
            print("ERROR: Input must be 1, 2 or 3.")
            
    # chose the tip amount
    if(serv == -1):
        raise ValueError

    return selectServiceTip(serv)

def selectServiceTip(serv):
    if(serv == 1):
        return .1
    elif(serv == 2):
        return .15
    elif(serv == 3):
        return .2
    else:
        raise ValueError

def promptQualityOfService():
    qual = -1
    while 1:
        try:
            qual = int(input ("on a scale from 1-5, what was the quality of service you recieved \n \n"))
            if(qual < 1 or qual > 5):
                raise ValueError
            break
        except ValueError as v:
            print("ERROR: Quality must be an integer from 1-5.")
    
    if(qual == -1):
        raise ValueError

    if qual == 1:
        return .25
    elif qual == 2:
        return .5
    elif qual == 3:
        return 1.0
    elif qual == 4:
        return 1.25
    elif qual == 5:
        return 1.5

def flow():
    #Greet the user
    greetUser()

    #prompt for the amount
    pretax = promptForBill()
    
    #prompt for the type of service
    base_tip_amount = promptForService()

    #Prompt for quality of service
    quality_factor = promptQualityOfService()

    #Present tip percent
    factored_tip = int(quality_factor*base_tip_amount*100)
    print("Your calculated tipping percent is: {}%".format(factored_tip))

    #Print the amount in dollars for tip
    tip_in_dollars = factored_tip*.01*pretax 
    print("Your tip in dollars is: ${0:.2f}".format(tip_in_dollars))

    #Print the total (base + tip)
    total = tip_in_dollars + pretax
    print("Your total including tax is: ${0:.2f}".format(total))

if __name__ == "__main__":
    while 1:
        flow()
        runagain = input("Would you like to calculate a new tip? (y/N): ")
        if(runagain != 'y'):
            break
