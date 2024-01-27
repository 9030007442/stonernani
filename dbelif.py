db={'username':'nani123','password':'nani@12'}
username=eval(input('enter user name'))
password=eval(input('enter password'))
if username ==db['username'] and password == db['password']:
    print('login succesfull')
else:
    print('invalid password & username')