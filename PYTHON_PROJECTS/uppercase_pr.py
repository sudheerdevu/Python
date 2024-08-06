s=input()
'''
l=[]
for i in s:
    if i.isupper():
        l.append(i)
print(l)
'''
l=[i for i in s if i.isupper()]
print(l)