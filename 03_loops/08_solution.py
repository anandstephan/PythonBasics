num = int(input("Enter the Number"))
found=False
for i in range(2,num):
    if num%i==0:
        found=True

if found:
    print("Not a Prime Number")
else:
    print("Prime Number ",num)
