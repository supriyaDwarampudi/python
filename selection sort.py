list1=[58,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    min_value=min(list1[i:])
    min_ind=list1.index(min_value)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)



output:
[58, 3, 2, 78, 6, 0]
[0, 2, 3, 6, 58, 78]
