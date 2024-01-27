a=input('enter a string:')
i=0
out=''
res=''
count=''
while(a[i]<len(a)):
    out=out+a[i]
    if a[i]==out:
        res=res+a[i]
    else:
        count=count+a[i]
        print(count)