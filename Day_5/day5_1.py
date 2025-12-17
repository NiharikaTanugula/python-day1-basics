#Reverse a String

s1= input("enter str1:")
s2=""
for ch in s1:
    s2= ch+s2

print(s2)

if s1==s2:
    print("Palindrome")
else:
    print("Not Palindrome")

"""
Improvement (case & spaces safe):
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


🧠 Interview tip: mention string slicing ([::-1])
"""


#Vowels Count in a String
s3= input("enter str3:")
c=0
for ch in s3:
    if ch=='a'or ch== 'e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' :
        c +=1

print("Count of Vowels",c)

"""
✅ Cleaner Version (Recommended):
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

#one line code:
count = sum(1 for ch in s if ch.lower() in "aeiou")

"""

#Count frequency of each character


