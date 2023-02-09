from array import *
arr1=array('d',[1.3,1.5,3.4,2.5])
arr2=array(arr1.typecode,(a*7 for a in arr1))
print('The elements are: ')
for i in arr2:
    print(i)