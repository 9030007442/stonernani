print('welcome to my bus...')
dest=input(''' select destination by entering 
           1 for delhi 
           2 for mumbai 
           3 for chennai
           4 forhyderabad 
:--''')
adult_seat=int(input('number of adults    ;- '))
child_seat=int(input('number of childrens ;- '))
category=('enter \n 1 for ac \n 2 for nonac')
distance={'1':2000,'2':800,'3':350,'4':500}
if category == '1':
    adult_price =10
    child_price =5
elif category== '2':
    adult_price =5
    child_price =3
total_price=distance[dest]*(adult_seat* adult_price +child_seat* child_price )

