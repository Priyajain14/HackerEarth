s = input()
c1 = 0
c2 = 0
for i in s:
    if(i == 'z'):
        c1 += 1
    elif(i == 'o'):
        c2 += 1
if(2*c1 == c2):
    print("Yes")
else:
    print("No")
