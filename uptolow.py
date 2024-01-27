f=str(input('enter:-'))
i=0
out=" "
while i<len(f):
    if 'a'<=f[i]<='z':
        out+= chr(ord(f[i])-32)
    else:
        out+=f[i]
    i+=1
print(out)