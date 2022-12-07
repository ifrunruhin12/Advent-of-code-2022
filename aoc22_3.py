#Advent of code
#Problem 2
#--- Day 3: Rucksack Reorganization ---


import string 

with open("day3inp.txt") as f:
    inp = f.read()

li1 = [list(map(str, i.split("\n"))) for i in inp.strip().split("\n\n")]

alphabet_string = string.ascii_letters

#PART 1

letter_sum = 0
for i in li1[0]:
    half_length_item = len(i)//2
    first_half = i[:half_length_item]
    second_half = i[half_length_item:]
    common_item = ''.join(set(first_half).intersection(second_half))
    #find out the common letter between them
    letter_sum += (alphabet_string.index(common_item)+1)

print(letter_sum)


#PART 2

total_common_itemType_sum = 0
for i in range(len(li1[0])):
    if i%3==0:
        elf_group = li1[0][i:i+3]
        common_item_2 = ''.join(set(elf_group[0]).intersection(elf_group[1]))
        common_item_3 = ''.join(set(common_item_2).intersection(elf_group[2]))
        total_common_itemType_sum += (alphabet_string.index(common_item_3)+1)
    else:
        pass 

print(total_common_itemType_sum)