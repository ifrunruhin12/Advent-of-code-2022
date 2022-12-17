#Advent of code
#Problem 4
#--- Day 4: Camp Cleanup ---

with open("day4inp.txt") as f:
    inp = f.read()

li1 = [list(map(str, i.split("\n"))) for i in inp.strip().split("\n\n")]

li2 = []
for i in li1[0]:
    str1 = i.split(",")
    li2.append(str1)

cnt = 0
cnt1 = 0

for j in li2:
    temp_li1 = j[0].split("-")
    temp_li2 = j[1].split("-")
    s1 = int(temp_li1[0])
    e1 = int(temp_li1[1])
    s2 = int(temp_li2[0])
    e2 = int(temp_li2[1])

    if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
        cnt += 1
    if s1 <= e2 >= s2 <= e1:
        cnt1 += 1

print(cnt,cnt1)
