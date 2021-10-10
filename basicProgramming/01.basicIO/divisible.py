n = int(input())
num = ''
l = input().split()
for i in range(n//2):
    num = num+l[i][0]
for i in range(n//2, n):
    num = num+l[i][-1]
if(int(num) % 11 == 0):
    print("OUI")
else:
    print("NON")
