N=input("N:")
K=input("K:")
n=input("Find:")
num=0
l=len(n)
for i in range(0,l):
    if(n[i]==K):
        num=num+1
if (num>0):
    print("Yes")
else:
    print("No")