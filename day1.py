
# a ="santi"
# print(a[: : -1]) #reversing a string
# print(a[1:3]) #slicing a string
# #pmdas rules

'''a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
totalBill = a + b
result = totalBill / 2
print(result)'''

a = int(input("Enter a number: ")).lower()
if(a==0):
    print("It is 0")
elif(a%2==0):
    print("It is Even")
else:
    print("Odd")

#samosa 1plate = 50
# full = 100, achar = yes -> add 10 if no then print bill
# use multiple statement 
#a = 0 at first

#research gold
#three way, straight->khola parkhine->dead, tairine-> three trees -> first= end, second= win, third = khanirakhyo
# , left or right -> dead/end


achar = int(print("Do you want achar?"))
if achar==1:
    fullPlate += 10
    print("Your bill is: ", fullPlate)
else:
    print("Your bill is Rs.100")
