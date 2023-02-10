from array import *
first=[int(i) for i in input("Enter a value: ").split(',')]
marks=array('i',first)
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total Marks:',sum)
n=len(marks)
percent=sum/n
print('Percentage: ',percent)








output:
    Enter value:10 25 14 269 45
10
25
14
269
45
Total marks: 363
percentage: 72.6
