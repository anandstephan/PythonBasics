number = int(input("Enter the Number"))
even_sum=0
for i in range(1,number+1):
    if i%2==0:
        even_sum+=i
print("Even Number sum is ",even_sum)