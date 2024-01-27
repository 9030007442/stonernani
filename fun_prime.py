def prime():
    num=int(input('enter number:-'))
    i=1
    count=0
    while i<=num:
        if num %i==0:
            count+=1
        i+=1
    if count==2:
         print('prime')
    else:
         print('not prime')
prime()
prime()
prime()
prime()
prime()