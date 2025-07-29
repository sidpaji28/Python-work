 n=int(input("enter how many elements in l1"))
m=int(input("enter how many elements in l2"))
l1=[]
l2=[]
l3=[]
for i in range(n):
    a=int(input('enter numbers'))
    l1.append(a)
for i in range(m):
    b=int(input('enter numbers'))
    l2.append(b)
for i in range(n):
    l3.append(l1[i]+l2[i])

print(l3)

    


