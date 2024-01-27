a=int(input('enter marks'))
if a > 90 and a<=100:
    print('A+')
elif a>80 and a<=90:
    print('A')
elif a>70 and a<=80:
    print('B+')
elif a>60 and a<=70:
    print('B')
elif a>50 and a<=60:
    print('c')
elif a>=35 and a<=50:
    print('pass')
elif a<35:
    print('=fail')
else:
    print('invalid marks')