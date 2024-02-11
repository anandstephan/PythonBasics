order_size = "Medium"
extra_shot = bool(input("enter the extra short"))

if extra_shot:
    coffee = order_size+" coffee with an extrashot"
else:
    coffee = order_size+" coffee"


print("order",coffee)