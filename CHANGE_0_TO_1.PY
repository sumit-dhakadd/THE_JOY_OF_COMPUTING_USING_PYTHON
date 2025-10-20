def evolve(x):
    import random
    ind = random.randint(0, len(x)-1)
    p = random.randint(1,100)
    print(p)
    if(p == 1):
        if(x[ind] == '0'):
            x[ind] = '1'
        else:
            x[ind] = '0'



with open("Binary.txt") as myfile:
    x = myfile.read()
    x = list(x)
for i in range(0,100):
    evolve(x)
    print("".join(x))