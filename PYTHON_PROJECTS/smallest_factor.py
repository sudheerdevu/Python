n=int(input("enter:"))
flag=True
for i in range(2 , n//2):
    if n%i==0:
        print(f"{i} is a factor")
        flag=False
        break
if(flag==True):
    print(n)
