def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print_kwargs(power="Web Swings",name="Spider Man")
print_kwargs(name="IronMan")
print_kwargs(name="Captain America",power="belive")