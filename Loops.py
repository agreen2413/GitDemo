# In Python there is no {} open and close brackets unlike C# and Java. It is ":" instead on If statement.
#Example of If/else statement code below
language = "Python"
a = 4

if a > 2:
    print("condition match")
else:
    print("condition do not match")
print("This code is valid")       #This will always print cause it is not part of the if/else block

print("*****************************************************")

#Example of For Loops code below

obj = [4, 5, 6, 7]  #iterate each values in the list
for i in obj:
    print(i*2)      #multiply each values of i by 2   so output is 8, 10, 12 and 14

print("*****************************************************")

#another For Loop example below
summation = 0
for j in range(1, 7):
    summation = summation + j
    print(summation)


print("******************************************************")

for k in range (1, 10, 2): #The 2 at the end means increment by 2 each time e.g 1, 3, 5, 7, 9 and index starts a 1
    print(k)

print("*****************************************************")
for m in range (10): #Index here starts at 0, output will be e.g 0,1,2,3,4,5,6,7,8,9
    print(m)
