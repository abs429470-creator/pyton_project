def inventory_summary(**kwargs):
    sumOfitems = 0
    for i in kwargs:
         sumOfitems = sumOfitems + kwargs[i][0]
    return sumOfitems

print(inventory_summary(bread=(2,8),milk=(7,5)))
def print_args_kwargs(*args, **kwargs):
    for i in range(len(args)):
        print(args[i])
    for x, y in kwargs.items():
            print(x, y)



print_args_kwargs(4, 6, 7, bread=3, choc=4)
