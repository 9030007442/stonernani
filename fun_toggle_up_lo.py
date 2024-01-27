def toggle():
    a=input('enter :-')
    i=0
    out=" "
    while len(a)>i:
        if 'a'<=a<='z':
            out+=chr(ord(a[i])-32)
        elif 'A'<=a<='Z':
            out+=chr(ord(a[i])+32)
        else:
            out+=a[i]
        i+=1
    return out
print(toggle())

