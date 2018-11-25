def factorial(number):
    if (number > 0):
        result = 1
        for i in range(number):
            result = result * (i+1)
        return result
    return False


print('6! is equal to : ' + str(factorial(6)))
print('15! is equal to : ' + str(factorial(15)))