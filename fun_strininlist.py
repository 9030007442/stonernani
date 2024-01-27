def vowels(a):
    i=0
    count=0
    while i<len(a):
        if a[i] in'aeiouAEIOU':
            count+=[i] 
        i+=1
    return count
print(vowel('hello rohit'))
