#1 What is a Dictionary? A dictionary stores data as key : value pairs.
student = {
    "name": "Ram",
    "age": 22,
    "branch": "CSE"
}
#Keys-> unique, immutable   Values-> anything

#2 Creating dictionaries
dl= {}
d2 = dict()
#3 Accessing Values
print(student["name"]) # Ram, ⚠️ If key doesn’t exist → KeyError
print(student.get("marks","not found")) 
#4 Adding or updating
student["age"]= 23
student["college"] = "ABC"
#5 Removing Items
student.pop("age")
print(student) #{'name': 'Ram', 'branch': 'CSE', 'college': 'ABC'}
del student["branch"]
print(student) #{'name': 'Ram', 'college': 'ABC'}
#student.clear() #clear whole dictionary
print(student) #{}

#Looping through Dictionary
#keys:
for k in student:
    print(k)
#values:
for v in student.values():
    print(v)
# Key-values
for k,v in student.items():
    print(k,v)


# Count Frequency of Characters:
s= input("enter a string:")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
#Advance - using get()
freq1={}
for ch in s:
    freq1[ch]= freq1.get(ch,0)+1

#First Non-repeating character (Dictionary way)
freq2 = {}
for ch in s:
    freq2[ch] = freq2.get(ch,0)+1
for ch in s:
    if freq2[ch]==1:
        print(ch)
        break
else:
        print("No Non repeating character")



"""
!!!!!!!!!!!!Interview Explanation (Memorize This)

“Dictionaries are ideal for frequency-based problems because they provide O(1) average lookup time.”
"""

#1 Count frequency of words in a sentence

sen = input("enter a sentence:")
words = sen.lower().split()
freq11={}

for word in words:
    if word in freq11:
        freq11[word]+=1
    else:
        freq11[word]=1

print(freq11)
print(words)

#2 Find duplicate characters in a string

s2= input("enter a string2:")
res=[]
freq={}
for ch in s2:
    if ch in freq:
        freq[ch]+=1
        if freq[ch]==2:
            res.append(ch)
    else:
        freq[ch]=1

print("".join(res))

#3 Find unique characters using dictionary
s3= input("enter a string3:")
freq3={}
for ch in s3:
    if ch in freq3:
        freq3[ch]+=1
    else:
        freq3[ch]=1
"""
for k,v in freq3.items():
    if v==1:
        print(k,end=" ")
"""
for ch in s3:
    if freq3[ch]==1:
        print(ch,end=" ")

#4 First repeating character in string
s4= input("enter a string4")
freq4={}
for ch in s4:
    if ch in freq4:
        freq4[ch]+=1
        if freq4[ch]==2:
            print(ch)
            break
    else:
        freq4[ch]=1
else:
    print("No repeating charcater")

#5 Character with maximum frequency
s5 = input("enter a string5:")

if not s5:
    print("empty string")
else:
    freq5={}

    for ch in s5:
        if ch in freq5:
            freq5[ch]+=1
        else:
            freq5[ch]=1

    m= max(freq5.values())
    for ch in s5:
        if freq5[ch]==m:
            print(ch)
            break