s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

common_characters = []

for char in s1:
    if char in s2 and char not in common_characters:
        common_characters.append(char)

print("Characters ", ''.join(common_characters))
