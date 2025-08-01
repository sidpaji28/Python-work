str=''
x=input('enter valid 8 digit password')
for i in range(0,7):
    if len(x[i])<8:
        print('enter 8 digit number')
    if x[i].isupper() == False:
        print('password need to have a upperacse char')
    if x[i].islower() == False:
        print('password need to have a lowercase char')
    if x[i] != '!' or x[i] != '@' or x[i] != '#' :
        print('password need to have a special char')
    else:
        print('valid password')
        
            

def PWD_CHECK(n):
    if i in n:
        n[i]==x[i]
        print('correct passwrod')
    else:
        print('invalid password')
        
PWD_CHECK(n=input('confirm password') )

        
