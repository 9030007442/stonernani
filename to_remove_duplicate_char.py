string=input('enter strting =')
out =' '
for char in string:
    if char not in out:
        out+=char
print(out)