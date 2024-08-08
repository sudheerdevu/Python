    # 1 st question

dictnry = {"country":"india",
           "state":"telangana",
           "capital_city": "Hyderabad"}

# # cp = dictnry.copy()

print(dictnry)
del dictnry["capital_city"]
dictnry["captital"] = "Hyderabad"
print(dictnry)


# #2  question

strng = """""""Well come to the thundersoft Thundersoft - World leading OS and Intelligent Device Producs and Technology Provuder"""


with open("test.txt","r+") as file:
    file.write(strng)

    file.seek(0)
    content = file.read()
    # print(content)

# pattern = r'^p|^T'

list1 = content.split()
lis2= []

# print(list1)

for letter in list1:
    if letter.startswith(("P","p")) or letter.startswith(("T","t")) :
        a = list1.index(letter)
        
        b = list1[a]
        lis2.append(b)
print(lis2)



    




# 3rd question

list1 = ["fruits","apple","banana",60,22,"apple","banana",60,22]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


#4th question

lis3 = [22,"apple","banana",60,"fruits"]

a = lis3.pop(0)
# print(a)

b = lis3.pop(-1)

lis3.insert(0,b)
lis3.append(a)
print(lis3)


# 5th question
lis5 = [22,"apple",["banana",60],"friuts"]

lis6 = []

for i in lis5:

    


    if type(i) == list:
        for j in i:
            lis6.append(j)
    elif type(i) == int or str:
        lis6.append(i)
    

print(lis6)


# 6th question

class A:
    def __init__(self):
        pass
    def anime(self):
        return "hello from anime A"
class B(A):
    def movie(self):
        return super().anime()
    
obj = B()
x = obj.anime()
print(x)