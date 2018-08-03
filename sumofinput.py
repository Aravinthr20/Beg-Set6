x=0
a=int(input())
while(a>0):
    i=a%10
    x=x+i
    a=a//10
print(x)