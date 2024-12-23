list1=[1,2,3,4]
list2=[1,2,3 ,4,5]
a=[]
b = min(len(list1),len(list2))
c = max(len(list1),len(list2))
for i in range(c):
    if i<b:
        a.append(list1[i]+list2[i])
    else:
        a.append(0+list2[i])
print(a)
