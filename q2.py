l=[]
for i in range(1,21):
    l.append(i)
print(l)

for i in l:
    if i%3==0:
        print('*'*i)
    else:
        print(i)
