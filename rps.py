print('enter \n 1---> rock \n 2--->paper \n 3--->scossor' )
p1=input('player 1 :')
p2=input('player 2 :')
if p1==p2:
    print('match tie')
elif p1 == '1' and p2 == '3':
    print('player 1 won')
elif p1 == '2' and p2 == '1':
    print('player 1 won')
elif p1 == '3' and p2 == '2':
    print('player 1 won1')
else:
    print('plater 2 won')