import copy

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3

f = open("6.txt", "rt")
ilines = f.read()
f.close()

"""
ilines = ....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


ilines = [line for line in ilines.split("\n") if line.strip()]

lines = []
initLines = []

for l in ilines:
    lines.append(list(l))
    initLines.append(list(l))

def getLocs(guard, guardDir, lines):
    locs = []
    inloop = False

    while (guard[0] >= 0 and guard[0] < len(lines[0]) and guard[1] >= 0 and guard[1] < len(lines)):
        nextPos = [0, 0]
        if guardDir == DIR_UP:
            nextPos[0] = guard[0]
            nextPos[1] = guard[1] - 1
        elif guardDir == DIR_RIGHT:
            nextPos[0] = guard[0] + 1
            nextPos[1] = guard[1]
        elif guardDir == DIR_DOWN:
            nextPos[0] = guard[0]
            nextPos[1] = guard[1] + 1
        elif guardDir == DIR_LEFT:
            nextPos[0] = guard[0] - 1
            nextPos[1] = guard[1]

        if nextPos[0] < 0 or nextPos[0] >= len(lines[0]) or nextPos[1] < 0 or nextPos[1] >= len(lines):
            loc = [guard[0], guard[1]]
            locs.append(loc)
            lines[guard[1]][guard[0]] = "X"
            break

        if lines[nextPos[1]][nextPos[0]] == "." or lines[nextPos[1]][nextPos[0]] == "X":
            lines[guard[1]][guard[0]] = "X"
            loc = [guard[0], guard[1]]
            locs.append(loc)
            guard[0], guard[1] = nextPos[0], nextPos[1]
        else:
            guardDir += 1
            guardDir %= 4
    return locs

def isInLoop(guard, guardDir, lines):
    locs = []
    inloop = False

    while (guard[0] >= 0 and guard[0] < len(lines[0]) and guard[1] >= 0 and guard[1] < len(lines)):
        nextPos = [0, 0]
        if guardDir == DIR_UP:
            nextPos[0] = guard[0]
            nextPos[1] = guard[1] - 1
        elif guardDir == DIR_RIGHT:
            nextPos[0] = guard[0] + 1
            nextPos[1] = guard[1]
        elif guardDir == DIR_DOWN:
            nextPos[0] = guard[0]
            nextPos[1] = guard[1] + 1
        elif guardDir == DIR_LEFT:
            nextPos[0] = guard[0] - 1
            nextPos[1] = guard[1]

        if nextPos[0] < 0 or nextPos[0] >= len(lines[0]) or nextPos[1] < 0 or nextPos[1] >= len(lines):
            lines[guard[1]][guard[0]] = "X"
            break

        loc = [guard[0], guard[1], guardDir]
        if locs.count(loc) > 0:
            inloop = True
            break

        if lines[nextPos[1]][nextPos[0]] == "." or lines[nextPos[1]][nextPos[0]] == "X":
            lines[guard[1]][guard[0]] = "X"
            loc = [guard[0], guard[1], guardDir]
            locs.append(loc)
            guard[0], guard[1] = nextPos[0], nextPos[1]
        else:
            guardDir += 1
            guardDir %= 4
    return inloop

x_len = len(lines[0])
y_len = len(lines)

guard = [0, 0]
guardDir = DIR_UP

for l in range(len(lines)):
    if lines[l].count("^") > 0:
        guard[0] = lines[l].index("^")
        guard[1] = l
        break

guardInit = [guard[0], guard[1]]
guardInitDir = guardDir

locs = getLocs(guard, guardDir, lines)

count = 0
for i in range(y_len):
    for j in range(x_len):
        print(f"Testing ({j}, {i})...")

        if locs.count([j, i]) == 0:
            print("No Location")
            continue

        lines = copy.deepcopy(initLines)
            
        guard = copy.deepcopy(guardInit)
        guardDir = guardInitDir
            
        if lines[i][j] == ".":
            lines[i][j] = "#"
            if isInLoop(guard, guardDir, lines):
                count += 1
                print("Loop")
            else:
                print("No Loop")
        else:
            print("Occupied")

print(f"Total Positions: {count}")
