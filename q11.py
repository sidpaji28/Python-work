String = str(input("enter the string"))
dis={}
for i in String:
    dis[i]=String.count(i)
a=sorted(dis.items(),key=lambda y: y[1],reverse=True)

print(a[1][0])
