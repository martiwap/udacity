def factorial(number):
    result = 1

    if (number == 1):
        return result

    if (number > 0):
        for i in range(number):
            result = result * (i+1)
        return result
        
    return False


print('6! is equal to : ' + str(factorial(6)))
print('15! is equal to : ' + str(factorial(15)))
