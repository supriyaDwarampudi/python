n=7
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(a+b)
fib(n)
output:
0
1
2
3
5
8
13



