x=input("Input:")
num=0
alp=0
l=len(x)
for i in range(0,l):
    if(x[i].isdigit()):
        num=num+1
    elif(x[i].isalpha()):
        alp=alp+1
print(num)
print(alp)
if (num>0)and (alp>0):
    print("yes")
else:
    print("No")