import random




#while i < 6:

def getless_pair():

    number1 = []
    number2 = []
    for n in range(10,99):
        number1.append(n)

    for z in range(10,99):
        number2.append(z)

    resultLess = True
    while resultLess:
        mynum1 = random.choice(number1)
        mynum2 = random.choice(number2)

        if mynum1 >= mynum2:
            resultLess = False
            print(str(mynum1) + " - " + str(mynum2) + " = ")
        else:
            print("wrong: " + str(mynum1) + " - " + str(mynum2) + " = ")

    
getless_pair()
