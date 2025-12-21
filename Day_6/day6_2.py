
#8 Sort characters by frequency
"""
Sorting by value (lambda magic)
sorted(freq.items(), key=lambda x: x[1])

What does lambda x: x[1] mean?

x → one tuple like ('a', 2)

x[1] → value (2)

Python sorts using this value


Key Rule to Remember
sorted(iterable, key=HOW_TO_COMPARE)
Lambda answers:HOW_TO_COMPARE?
"""

s8= input("enter string8:")

if not s8:
    print("Empty String")
else:
    freq8={}
    for ch in s8:
        if ch in freq8:
            freq8[ch]+=1
        else:
            freq8[ch]=1

    def get_key(item):
        return item[1]

    sorted_chars = sorted(freq8.items(), key=get_key, reverse=True)

    for ch in sorted_chars:
        for i in range(0,ch[1]):
            print(ch[0],end="")

    """
    res=""
    for ch,count in sorted_characters:
        res+= ch*count

    print(res)
    """