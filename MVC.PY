a=eval(input('a massege'))
if type(a) in (bool,int,float,complex):
    print(a**2)
else:
    print(3*len(a)+1)