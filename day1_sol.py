'''
with open("aoc22_1.txt") as f:
    inpt = f.read().split("\n\n")

a = sorted(map(lambda x: sum(map(int, x.split("\n"))), inpt))
print(a[-1])
print(a[-1] + a[-2] + a[-3])
'''


with open("aoc22_1.txt") as f:
    inp = f.read()
    

## PART 1
calories = [sum(map(int, i.split("\n"))) for i in inp.strip().split("\n\n")]

# AoC takes 1-indexed elf numbers
print(f"The highest number of calories carried by an elf is {max(calories)}")

## PART 2
sorted_calories = sorted(calories)
print(sum(sorted_calories[-3:]))