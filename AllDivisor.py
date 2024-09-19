#WAPP to display all the divisor of given number

#INPUT SECTION
num=int(input('Enter Any Number: '))

#Logic Section
print("Divisor of number = ",end=" ")
for i in range(1,num+1):
        if num % i == 0:
                print(i,end=",")