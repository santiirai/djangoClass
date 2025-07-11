#samosa 1plate = 50
# full = 100, achar = yes -> add 10 if no then print bill
# use multiple statement 
#a = 0 at first
print("Customer: What is the cost of full plate and a half?")
fullPlate = 100
halfPlate = 50
print("Seller: ")
print("The cost of full plate is ", fullPlate)
print("The cost of half plate is ", halfPlate)

fullOrhalf = input(print("Seller: Do you want full or half? "))
if(fullOrhalf == "full"):
    achar = input(print("Seller: Do you want achar?"))
    if achar=="yes":
        fullPlate += 10
        print("Seller: Your bill is: ", fullPlate)
    else:
        print("Seller: Your bill is Rs.100")
else:
    print("Seller: Your bill is Rs.", halfPlate)


