n=int(input('enter how many numbers'))
l=[]
for i in range(n):
    o=int(input('enter numbers.'))
    l.append(o)

for i in range(len(l)):
    if l[i]%2==0:
        print(l[i])
