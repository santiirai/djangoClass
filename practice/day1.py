#Add 5 numbers from user input and print the list
# i = []
# for list in range(5):
#     userInput = "Add any five numbers " + str(list+1) +":"
#     output = input(userInput)
#     i.append(output)
# print(i)


#Print square of numbers from 1 to 5
# for i in range(1, 5):
#     square = i*i
#     print(square)

#Ask user 3 favorite colors and store them in a list
# favouriteColors = []
# for i in range(3):
#     addList = "Enter your favourite color"+ str(i+1)+":"
#     finalList = input(addList)
#     favouriteColors.append(finalList)
# print(favouriteColors)

#Count how many numbers are greater than 10 in a list
# nums = [2,1,5,77,4,56]
# count = 0
# for i in nums:
#     if(i>10):
#         count +=1
# print(count)

# #Count how many numbers are even in a list
# list = [12,34,21,1,9,7,2]
# count = 0
# for i in list:
#     if(i%2==0):
#         count +=1
# print(count)

#Count how many strings in a list have more than 5 characters
# str = ["antiii","apple", "orange", "pineapple","banana"]
# finalCount = 0
# for i in str:
#     count = len(i)
#     if(count>5):
#         finalCount += 1
# print(finalCount)

#Find the sum of all numbers greater than 50
# num = [2,1,55,66,2,3,45]
# sum = 0
# for i in num:
#     if(i>50):
#         sum += i
#         i += 1
# print(sum)

#Count how many names start with the letter 'A'
str = ["Ant","Banana","apple","Anu"]
count = 0
for i in str:
    if(i[0]=="a"):
        count += 1
print(count)