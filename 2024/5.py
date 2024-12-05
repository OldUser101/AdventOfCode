import re

def doesPrecede(n, x, y):
    if n.count(x) == 0 or n.count(y) == 0:
        return True
    return (n.index(x) < n.index(y))

def checkValidity(u, r):
    for n in u:
        rules = re.findall(f"{n}\|\d*", r)
        for rule in rules:
            x = int(rule.split("|")[0])
            y = int(rule.split("|")[1])
            
            if doesPrecede(u, x, y) == False:
                return False
    return True

def fixOrdering(u, r):
    newU = u
    modified = False
    while True:
        modified = False
        for n in u:
            rules = re.findall(f"{n}\|\d*", r)
            for rule in rules:
                x = int(rule.split("|")[0])
                y = int(rule.split("|")[1])
                        
                if doesPrecede(newU, x, y) == False:
                      newU.remove(y)
                      idx = newU.index(x)
                      newU.insert(idx + 1, y)
                      modified = True
        if not modified:
            break
    return newU
                

f = open("5.txt", "rt")
ruleInput = f.read()
f.close()

ruleInput = ruleInput.strip()

"""
ruleInput = 47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

rules = ruleInput.split("\n\n")[0]
updates = ruleInput.split("\n\n")[1].split("\n")

middleTotal = 0
for u in updates:
    pages = list(map(int, u.split(",")))
    b = checkValidity(pages, rules)
    if not b:
        newOrder = fixOrdering(pages, rules)
        print(f"Old: {pages} New: {newOrder}")
        middleTotal += newOrder[int(((len(newOrder) + 1) / 2) - 1)]

print(f"Total: {middleTotal}")


