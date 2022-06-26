

number = input("Please put in a number.\n")
#print(number)
line = ""
for n in range(1,int(number)+1):
    #print("#")
    # method 2:
    line = ""
    #for n2 in range(int(n),int(number)+1):
    for n2 in range(0,int(number)+1-n):
        line = line + "*"
    print(line)


