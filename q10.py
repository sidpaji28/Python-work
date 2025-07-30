x=input('enter sting')
l=[]
for i in range(len(x)):
    l.append(x[i])
z=[]
f=0
for i in range(len(l)):
    if x[i] not in z:
        z.insert(0,x[i])
        f=f+1
str=''
str=str.join(z)
print(str)
