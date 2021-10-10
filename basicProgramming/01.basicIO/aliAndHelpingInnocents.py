# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

n = input()
result = "valid"
vowel = ['A', 'E', 'I', 'O', 'U', 'Y']
for i in range(8):
    if(i == 1 or i == 5):
        continue
    elif(i == 6):
        if(n[i] != '-'):
            result = "invalid"
            break
    elif(i == 2):
        if(n[i] in vowel):
            result = "invalid"
            break
    else:
        a = int(n[i])
        b = int(n[i+1])
        if((int(n[i]) + int(n[i+1])) % 2 != 0):
            result = "invalid"
            break
print(result)
