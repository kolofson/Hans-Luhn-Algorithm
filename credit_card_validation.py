starting_numbers = ["4", "5", "37", "6"]
single_digits = []

# Return True if the card number is valid
def isValid(number):
    if number[0] not in starting_numbers:
        return False
    elif not len(number) >= 13 and not len(number) <= 16:
        return False
    else:
        sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
        if sum % 10 == 0:
            return True
        else:
            return False

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum = 0
    for i in reversed(range(len(number))):
        if i % 2 == 0:
            val = int(number[i]) * 2
            single_digits.append(int(getDigit(val)))
    # Add all digits together
    for i in range(len(number)):
        sum += int(number[i])
    return sum

# Return this number if it's a single digit, otherwise return the sum of the 2 digits
def getDigit(number):
    number = str(number)
    if getSize(number) == 2:
        x = number[0]
        y = number[1]
        return int(number[0]) + int(number[1])
    else:
        return number

# Return sum of odd-place digits in number
def sumOfOddPlace(number):
    sum = 0
    for i in reversed(range(len(number))):
        if i % 2 != 0:
            sum += int(number[i])
    return sum

# Return the number of digits in d
def getSize(d):
    return len(d)


""" Program Start """
card = input("Enter a credit card number\n")

if isValid(card):
    print("Card is Valid")
else:
    print("Card is Invalid")

