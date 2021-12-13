    
# """ Recursive function to find the super digit of a number """
def superDigit(n, k):
    # If the input n is less than 1 digit, return that number
    if len(str(n)) <= 1:
        return int(n)
    else:
        # Calculating the sum of the digits in n
        s = 0
        for x in str(n):
            s += int(x)
        # Calling the function with the sum * k with key 1 time
        return superDigit(s*k, 1)


print(superDigit('9875', 4))
print(superDigit('148', 3))
print(superDigit('123', 3))
print(superDigit('861568688536788', 1000))
print(superDigit('3546630947312051453014172159647935984478824945973141333062252613718025688716704470547449723886626736', 1000))

# print(sum(861568688536788))