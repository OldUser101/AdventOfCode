def bubbleSort(list1):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                swap = True
    return list1

list1 = []
list2 = []

f = open("1.txt", "rt")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    s = lines[i].split("   ")
    list1.append(int(s[0]))
    list2.append(int(s[1]))

#list1 = [3, 4, 2, 1, 3, 3]
#list2 = [4, 3, 5, 3, 9, 3]

list1 = bubbleSort(list1)
list2 = bubbleSort(list2)

diff = 0
for i in range(len(list1)):
    diff += abs(list1[i] - list2[i])

print(f"Difference is {diff}.")

sim_score = 0
for i in range(len(list1)):
    sim_score += abs(list1[i] * list2.count(list1[i]))

print(f"Similarity score is {sim_score}.")