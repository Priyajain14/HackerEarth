# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

l = list(map(int, input().split()))
n = 0
for i in range(l[0], l[1]+1):
    if(i % l[2] == 0):
        n = n+1
print(n)
