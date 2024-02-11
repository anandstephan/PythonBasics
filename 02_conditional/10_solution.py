pet_name=input("Enter the Pet Name")
pet_age = int(input("Enter the Pet Age"))
if pet_name == "Dog" and pet_age<2:
    print("Puppy Food")
elif pet_name == "Dog" and pet_age>=2:
    print("Adult Dog Food")
elif pet_name == "Cat" and pet_age<5:
    print("Junior Cat Food")
elif pet_name == "Cat" and pet_age>=5:
    print("Senior Cat Food")