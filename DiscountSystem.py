"""Online Shopping Discount System
problem: Design a discount system for an online shopping platform. The discount rules are:
If the customer is a premium member, they get an additional 5% discount on top of 
Input: purchase_amount, is_premium_member
Example:
Input: purchase_amount = 250, is_premium_member = True
Output: Total amount after discount = $195.75
Input: purchase_amount = 180, is_premium_member = False
Output: Total amount after discount = $162."""

#Input Section
purchase_amount = int(input("Enter the purchase amount: "))
is_premium_member = eval(input("Are You Premium Member:True or False : "))

#Logical Section
if purchase_amount > 200:
    out = purchase_amount-purchase_amount*(15/100)
    if is_premium_member:
        out=out-purchase_amount*(5/100)
        print("Your Bill After Discount Apply:",out)
    else:
        print(out)
elif  purchase_amount > 100 and purchase_amount < 200 :
    out = purchase_amount-purchase_amount*(10/100)
    if is_premium_member:
        out = out-purchase_amount*(5/100)
        print("Your Bill After Discount Apply:",out)
    else:
        print("Your Bill After Discount Apply:",out)

else:
    print("Your Bill :",purchase_amount)



