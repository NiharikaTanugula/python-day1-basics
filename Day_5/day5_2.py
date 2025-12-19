#Count frequency of each character

string = input("enter a string:")


def freq(string,processed):
    for ch1 in string:
        if ch1 not in processed:
            count=0
            for ch2 in string:
                if ch1==ch2:
                    count+=1
            print(f'{ch1}:{count}')
            processed += ch1


freq(string,"")

"""
1️⃣ You don’t need processed as a parameter

(keep it inside the function — cleaner design)

def freq(string):
    processed = ""
    for ch1 in string:
        if ch1 not in processed:
            count = 0
            for ch2 in string:
                if ch1 == ch2:
                    count += 1
            print(f"{ch1}:{count}")
            processed += ch1

2️⃣ Handle spaces (optional enhancement)
if ch1 != " " and ch1 not in processed:
"""


"""
These two topics are the CORE of problem-solving. Once you understand them, many interview problems will feel familiar instead of scary.

I’ll explain clearly, step by step, with patterns you can reuse everywhere.

🔑 PART 1: A UNIVERSAL THINKING PATTERN (Works for 70% Problems)

Whenever you see a string or array problem, follow this 5-question checklist.

🪜 The 5-Question Problem-Solving Checklist
1️⃣ What am I ITERATING over?

String → characters

Array → elements

for each element in input

2️⃣ What is the MAIN TASK?

Examples:

Count?

Compare?

Reverse?

Remove?

Find first?

👉 Be very specific.

3️⃣ What should NOT happen?

This is the most important question.

Examples:

Duplicate output ❌

Re-counting ❌

Order changing ❌

Infinite loop ❌

If something must NOT happen → you need control logic.

4️⃣ Do I Need MEMORY?

Ask:

“Do I need to remember past elements?”

If yes → introduce:

processed

seen

result

visited

💡 This single question leads you to the correct extra variable almost every time.

5️⃣ When Do I UPDATE MEMORY?

Critical mistake beginners make:

Updating too early or too late

Rule:

Update memory only after the element is fully processed.

🧠 Apply Pattern to Your Problem (Character Frequency)
Question	Answer
Iterate	Characters
Main task	Count occurrences
Should NOT happen	Duplicate printing
Need memory?	Yes
Memory type	String (processed)

That’s it.
No guessing. No magic.

🔁 PART 2: APPLY THE SAME THINKING TO ARRAYS

Let’s reuse the same logic, just change the data type.

Example 1️⃣: Count Frequency in an Array
Input: [1, 2, 2, 3, 1]
Output:
1:2
2:2
3:1

Thinking (same questions):

Iterate → numbers

Main task → count

Should NOT happen → duplicate printing

Need memory → yes (processed list)

Pseudocode:
processed = []

for each element:
    if not in processed:
        count occurrences
        print
        add to processed


🔥 SAME pattern as string problem.

Example 2️⃣: Remove Duplicates from Array
Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]

Thinking:

Iterate → elements

Main task → keep first occurrence

Should NOT happen → duplicates

Need memory → yes (result list)

Pseudocode:
result = []

for each element:
    if not in result:
        add to result

Example 3️⃣: First Non-Repeating Character
Input: "swiss"
Output: w

Thinking:

Iterate → characters

Main task → find unique

Should NOT happen → stop too early

Need memory → count info (nested loop or dict later)

🧠 KEY REALIZATION (VERY IMPORTANT)

Strings and arrays are the same logically.

Only difference:

Strings	Arrays
Characters	Elements
Immutable	Mutable

Logic patterns are identical.
"""


#First non repaeting characters i/p:swiss, o/p:w
string1 = input("enter a string1:")

def nr(string1,viewed):
    for ch1 in string1:
        if ch1 not in viewed:
            c=0
            for ch2 in string1:
                if ch1==ch2:
                    c+=1
            viewed+=ch1
            if c==1:
                print(f'{ch1}')
                break

nr(string1,"")

"""
def first_non_repeating(s):
    viewed = ""

    for ch1 in s:
        if ch1 not in viewed:
            count = 0
            for ch2 in s:
                if ch1 == ch2:
                    count += 1

            viewed += ch1

            if count == 1:
                return ch1

    return None


string1 = input("enter a string: ")
result = first_non_repeating(string1)

if result:
    print(result)
else:
    print("No non-repeating character")

"""




