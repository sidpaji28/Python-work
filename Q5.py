l=[]
n=int(input('enter how many numbers.'))
for i in  range(n):
    o=int(input('enter numbers'))
    l.append(o)
k=[]
def ADD_LIST():
    for i in range(n):
        x=l[i]+3
        k.append(x)
    print(k)
ADD_LIST()
