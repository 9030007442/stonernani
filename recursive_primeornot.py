def prime(a,i=2):
    if a==i:
        return ' prime'
    elif a%i==0:
        return 'not prime'
    return prime(a,i+1)
print(prime(6))
