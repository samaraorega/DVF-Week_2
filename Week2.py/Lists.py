names = ["Denisse", "Alfred", "Margot", "Fred", "Stace"]

#Accessing elements in a list
print(names[0])
print(names[2])
print(names[0:2])
print(names[1:4])

#Changing elements with destructive methods
names.append("Roxanne")
names.pop()
print(names)

names[1] = "Roxanne"
print(names)

#Finding Unique elements and length of lists

names.append("Fred")
unique_names = set(names)
print(names)
print(unique_names)
print(len(names))
print(len(unique_names))
