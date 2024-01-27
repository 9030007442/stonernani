def fib(a,b=1,c=1,out=()):
    if c>=a:
        return out
    elif b==0:
        out+=(b,c)
    else:
        out+=(c,)
    return fib(a,c,b+c,out)
print(fib(100))
print(fib(1000))
print(fib(1000))
print(fib(300))
print(fib(100))