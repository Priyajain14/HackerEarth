# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

def factorial(n):
    product = 1
    for i in range(2, n+1):
        product = product*i
    return product


print(factorial(int(input())))
