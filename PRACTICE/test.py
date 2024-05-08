s=input()
s2=""
for c in s:
    id=s.find(c)
    count=1
    if c.isupper():
        s1=s[id+1:len(s)]
        if(c in s1):
                id=s.find(c)
                if(id==-1):
                    break
                if(id>-1):
                 count+=1
        print(c,count)
        