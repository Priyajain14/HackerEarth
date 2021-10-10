# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

s = input()
for i in range((len(s)+1)//2):
    if(s[i] != s[len(s)-i-1]):
        print("NO")
        break
else:
    print("YES")
