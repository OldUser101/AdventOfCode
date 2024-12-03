lines = []

f = open("2.txt", "rt")
lines = f.readlines()
f.close()

#lines = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]

def isSafe(nums):
    mode = NONE
    if int(nums[0]) > int(nums[1]):
        mode = DECREASING
    elif int(nums[0]) < int(nums[1]):
        mode = INCREASING
    else:
        return False
    
    safe = True
    for i in range(len(nums) - 1):
        if mode == INCREASING:
            diff = int(nums[i + 1]) - int(nums[i])
            if diff < 1 or diff > 3:
                safe = False
                break
        elif mode == DECREASING:
            diff = int(nums[i]) - int(nums[i + 1])
            if diff < 1 or diff > 3:
                safe = False
                break
    return safe

NONE = 0
INCREASING = 1
DECREASING = 2

safeLines = 0
for s in lines:
    nums = s.split(" ")
    if isSafe(nums):
        safeLines += 1
        continue

    for i in range(len(nums)):
        mNums = nums[:i] + nums[i + 1:]
        if isSafe(mNums):
            safeLines += 1
            break

print(f"There are {safeLines} safe levels.")
                
