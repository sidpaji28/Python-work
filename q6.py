l=[]
n=int(input('enter how many numbers.'))
for i in range(n):
    o=int(input('enter numbers'))
    l.append(o)
print(l)
def DELETE_LIST():
    for i in l:
        l.remove(3)
    print(l)
DELETE_LIST()
