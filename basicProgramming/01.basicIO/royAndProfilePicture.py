# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

n = int(input())
for t in range(int(input())):
    l = list(map(int, input().split()))
    if(l[0] == l[1] and l[0] >= n):
        print("ACCEPTED")
    elif(l[0] >= n and l[1] >= n):
        print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
