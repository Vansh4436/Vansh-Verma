#Input Section
age=int(input("Enter Your Age: "))
ticket_price=int(input("Enter Ticket Price: "))
is_3d_movie=input("Have you 3d Ticket: ")
#Logical Section
if age<12:
    out=ticket_price-(ticket_price*.5)
    if is_3d_movie=="Yes":
        out=out+5
        print("Your Total Ticket Price",out)
    else:
        print("Your Total Ticket Price",out)
elif age>=65:
    out=ticket_price-(ticket_price*30/100)
    if is_3d_movie=="Yes":
        out=out+5
        print("Your Total Ticket Price",out)
    else:
        print("Your Total Ticket Price",out)
else:
    out = ticket_price
    if is_3d_movie=="Yes":
        out = ticket_price+5
        print("Your Total Ticket Price",out)
    else:
        print("Your Total Ticket Price",out)