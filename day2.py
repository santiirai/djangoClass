#for loop
# a = 1
# b = 21
# c = 2
# for a in range(a, b):
#     print(c*a)
# a = 2
# b = 10
# for a in range(a, a*(b+1),a):
#     print(a)

# d = "shanti"
# for s in d:
#     print(d)

# a = int(input("Enter a number: "))

# while(a!=0):
#     a = int(input("Enter a nummber: "))
#     if(a == 0):
#         print("Exit")
#         break

#list --> []
#tuple -->() //doesnot allow to insert data but can access
#set --> {}--all three 
# works in index 
#dict --> {} --key value means different from others

# list = ["apple","mango", "banana"]
# list.reverse()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)


# list = ["ant", "horse", "elephant"]
# list.insert(1,"fox")
# print(list)
# list.append("Mouse")
# print(list)
# list.pop()
# print(list)
# list.remove("ant")
# print(list)

# a = "shanti"
# b = "rai"
# print(f"My name is {a} {b}")

#Tuple
# a = (1,2,3,5)
# a = list(a)
# a.append("9")
# print(a)

#set
# b = {1,4,5,2,4,5}
# b.add(23)
# b.remove(4)
# print(b)

#dictionary --doesnot work on index and doesnot support duplicate key, will override
d = {
    'name' : "Shanti",
    'name' : "ShaSanti",
    'caste' : "Rai",
    'List' : ["2,3,2,3,5,45"],
    "e" : {
        'fruit' : "Apple",
        'Animal' : "Cat"
    }
}
print(d['name'])
d["gender"] = 'Female'
# d["age"] = 21
# del(d["age"])
# d.pop("name")
# d[list.append(90)]
f = d["e"]
f["fruits"] = "Mango"
# print(type(d["list"]))
print(d)

#three diff dictionary should be accesse by a single dictionary e.g. insert 