print('banglore to \n 1--->chennai \n 2--->delhi \n 3--->mumbai \n 4--->hyderabad')
des=input('select destination in above :' )
km={'1':350,'2':2000,'3':800,'4':500}
acc={'adult':10,'child':5}
nonacc={'adult':5,'child':3}
a=int(input('adult :'))
b=int(input('child :'))
c=eval(input('ac/nonac:'))
if des=='1':
    if c is 'ac':
    print(km[1]*(a*acc['adult']+b*acc['child']))
elif c is'nonac':
    print(km[1]*(a*nonacc['adult']+b*nonacc['child']))
    if des=='2':
        if c is'ac':
            print(km[1]*(a*acc['adult']+b*acc['child']))
    elif c is 'nonac':
        print(km[1]*(a*nonacc['adult']+b*nonacc['child']))
