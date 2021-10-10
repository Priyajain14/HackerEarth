# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

s = input()
for i in s:
    ch = ord(i)
    if(ch < 91):
        print(chr(ch+32), end='')
    else:
        print(chr(ch-32), end='')
