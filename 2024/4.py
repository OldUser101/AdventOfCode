def checkForXmas(l, i, j):
    c = 0
    t = "XMAS"
    s = ""

    if j <= len(l[i]) - 4:
        for x in range(4):
            if l[i][j + x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if j >= 3:
        for x in range(4):
            if l[i][j - x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if i <= len(l) - 4:
        for x in range(4):
            if l[i + x][j] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if i >= 3:
        for x in range(4):
            if l[i - x][j] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if j <= len(l[i]) - 4 and i <= len(l) - 4:
        for x in range(4):
            if l[i + x][j + x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if j >= 3 and i >= 3:
        for x in range(4):
            if l[i - x][j - x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if j <= len(l[i]) - 4 and i >= 3:
        for x in range(4):
            if l[i - x][j + x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""

    if j >= 3 and i <= len(l) - 4:
        for x in range(4):
            if l[i + x][j - x] == t[x]:
                s += t[x]
        if s == "XMAS":
            c += 1
    s = ""
    return c

def checkForMas(l, i, j):
    if i == 0 or i == len(l) - 1 or j == 0 or j == len(l[i]) - 1:
        return False

    c1 = []
    c2 = []

    for x in range(-1, 2):
        c1.append(l[i + x][j + x])

    for x in range(-1, 2):
        c2.append(l[i - x][j + x])

    c1.sort()
    c2.sort()

   # print(c1)
   # print(c2)

    if c1 == ["A", "M", "S"] and c2 == ["A", "M", "S"]:
        return True
    
    return False

f = open("4.txt", "rt")
lines = f.readlines()
f.close()

#lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            if checkForMas(lines, i, j):
      #          print(f"Found at ({i}, {j})")
                count += 1
      #      n = checkForXmas(lines, i, j)
      #      print(f"Found {n} at ({i}, {j})")
      #      count += n

print(f"Total: {count}")
            
