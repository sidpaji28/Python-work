x=input('eneter stirng')
b=0
for i in x:
    if i.isdigit():
        b=b+int(i)

    else:
        if i.isalpha():
            print('zero')

print(b)
