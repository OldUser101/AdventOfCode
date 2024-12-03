import re

def regexMatch(memory):
    regex = "(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
    muls = re.findall(regex, memory)
    return muls

def stripStr(s):
    return s[4:][:-1]

f = open("3.txt", "rt")
memory = f.read()
f.close()

#memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

muls = regexMatch(memory)
total = 0
mulsApplied = True
for s in muls:
    for x in range(len(s)):
        if x == 1 and s[x] == "do()":
            mulsApplied = True
        elif x == 2 and s[x] == "don't()":
            mulsApplied = False
        elif mulsApplied and x == 0 and s[x] != "":
            n = stripStr(s[x]).split(",")
            total += int(n[0]) * int(n[1])

print(f"Total is {total}.")
