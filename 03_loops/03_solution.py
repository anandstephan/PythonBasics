table_num = int(input("Enter the Number\n"))

for i in range(1,11):
    if(i==5):
        continue
    print(table_num," * ",i," = ",i*table_num)