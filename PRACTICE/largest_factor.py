n=int(input("enter:"))
flag=True
for i in range(n//2,1,-1):
    if n%i==0:
        print(f"{i} is a factor")
        flag=False
        break
if(flag==True):
    print(n)
