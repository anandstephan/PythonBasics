input_str = input("Enter the String")

for char in input_str:
    if input_str.count(char) == 1:
        print(char)
        break