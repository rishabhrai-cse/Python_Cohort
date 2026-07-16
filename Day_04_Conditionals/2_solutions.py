age=input("Enter your age:")
age=int(age)
day=input("Enter day: ")

price=12 if age>=18 else 8

if day=="Wednesday":
    price=price-2

print ("Ticket price for you is  $",price)