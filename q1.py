l=[]
for i in range(1,21):
    l.append(i)
print(l)

for i in l:
    if int(i%3==0):
        print('***')
    elif int(i%4==0):
        print('$$$$')
    else:
        print(i)
        


