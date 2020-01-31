
def isDivisible(num):
    sumOfEvenDigits = 0
    sumOfOddDigits = 0
    txt1 = " is a multiple of 11."
    txt2 = " is not a multiple of 11."

    for index in range(len(num)):

        if (index % 2) is 0:
                sumOfEvenDigits += int(num[index])
        else:
            sumOfOddDigits += int(num[index])

    if ((sumOfEvenDigits - sumOfOddDigits) % 11) is not 0:
        return num + txt2
    else:
        return num + txt1

while(1):
    num = str(input("Enter a number:"))
    if num is "0":
        break
    else:
        print(isDivisible(num))
