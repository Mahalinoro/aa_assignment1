# Basic module to track time taken by an algorithm
import timeit

def first_numbers(n):
    sum=0
    # Loop through the range  n+1
    # Increment the sum by the number i
    for i in range(n+1):
        sum += i 

    return sum

# Test Cases
print(first_numbers(10))
print(first_numbers(10000))
print(first_numbers(1000000))
print(first_numbers(1000000000))

# Uncomment the lines below to check for execution time
# n1 = 10
# n2 = 10000
# n3 = 1000000
# n4 = 1000000000

# def first_numbers_time():
#     t1_timer = timeit.Timer("n1, first_numbers(n1)", setup="from __main__ import first_numbers, n1")
#     # t2_timer = timeit.Timer("n2, first_numbers(n2)", setup="from __main__ import first_numbers, n2")
#     # t3_timer = timeit.Timer("n3, first_numbers(n3)", setup="from __main__ import first_numbers, n3")
#     # t4_timer = timeit.Timer("n4, first_numbers(n4)", setup="from __main__ import first_numbers, n4")
#     t1 = t1_timer.timeit(number=1)
#     # t2 = t2_timer.timeit(number=1)
#     # t3 = t3_timer.timeit(number=1)
#     # t4 = t4_timer.timeit(number=1)

#     print(t1, t2, t3, t4)

# first_numbers_time()
