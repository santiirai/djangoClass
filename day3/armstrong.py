#153
num = int(input("Enter a number: "))

def ArmstrongNum(num):
    sum = 0
    temp = num
    digits = len(str(num))

    while temp>0:
        digit = temp % 10
        sum += digit ** digits
        temp = temp // 10

    if sum == num:
        return True
    else:
        return False
if ArmstrongNum(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")