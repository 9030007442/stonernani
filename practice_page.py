def fun (a,b,out=0):
    if len(a)==len(b):
        for i,j in zip(a,b):
            if i!=j:
                out+=1
        return out
    return 'string length is not same'
print(fun('pil','lip'))
