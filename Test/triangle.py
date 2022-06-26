"""
task: print out a triangle like the following, once command execute, ask for an input of a number. 

*
**
***
****
...
***********n

Hint: first, get the input as a variable, loop through number from 1 to the input variable and print out the *
character. pay attention to 2 dimension.

"""
number = input("Please put in a number.\n")
#print(number)
line = ""
for n in range(1,int(number)+1):
    #print("#")
    # method 2:
    line = ""
    for n2 in range(1,int(n)+1):
        line = line + "*"
    print(line)

    # method 1:
    #line = line + "*"
    #print(line)