def sum_all_num(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(sum_all_num(1,2,3,4,5))