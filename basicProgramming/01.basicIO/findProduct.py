# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

n = input()
l = list(map(int, input().split()))
answer = 1
for i in l:
    answer = answer*i
print(answer % ((10**9)+7))
