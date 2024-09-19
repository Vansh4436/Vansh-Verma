#WAPP TO CHECK WEATHER GIVEN NUMBER IS PERFECT OR NOT

#INPUT SECTION
num = int(input("Enter Any Number:"))
sm = 0

#Logic Section
for i in range(1,num):
    if num % i == 0:
        sm = sm + i
if sm == num:
    print('The Given Number Is Perfect.')
else:
    print('The Given Number Is Not Perfect.')