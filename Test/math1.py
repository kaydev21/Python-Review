"""
task: find out all the number between 10 and 100 can be divided by 3 and 7

Hint: loop through all the numbers between 10 to 100, check each number divided by 3 and with a 
remainder of 0. Also the number divided by 7 is also has the remainder of 0. You will use a condition check 
if statement. If statements need to statisfy both conditions. 
"""

count = 0
for x in range(10,1000):
    if x % 3 == 0 and x % 7 == 0 and x % 5 == 0: 
        count = count + 1
        print(x)
        

if count == 0:
    print("No numbers avalible...")
else:
    print("We found total of " + str(count) + " numbers able to be divided by 3,7, or 5!")

