a=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
out=0
for b in a:
    if type(b)==int:
        if b%2==0:
            out+=b
        else:
            out-=b
print(out)