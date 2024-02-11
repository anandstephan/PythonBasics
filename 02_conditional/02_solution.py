age = int(input("Enter the age"))
day = input("Enter the day")

ticket_price=0
discount = 0

if age<18:
    ticket_price=8
elif age>=18:
    ticket_price = 12

if day=="Wed":
    ticket_price-=2

print(ticket_price)