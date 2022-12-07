#Advent of code day 2
#Problem 2
#--- Day 2: Rock Paper Scissors ---

with open("day2inp.txt") as f:
    inp = f.read()


li1 = [list(map(str, i.split("\n"))) for i in inp.strip().split("\n\n")]

opponent_li = ['A','B','C']
my_li = ['X','Y','Z']

#Rock beats Scissors... X beats C... A beats Z... 1-3
#Paper beats Rock... Y beats A... B beats X...2-1
#Scissors beats Paper... Z beats B... C beats Y...3-2

#PART 1
score = 0
for i in li1[0]:
    first_card = opponent_li.index(i[0])
    last_card = my_li.index(i[2])
    if first_card == last_card:
        score +=  (last_card+1) + 3
    elif (i == 'C X') or (i == 'A Y') or (i=='B Z'):
        score += (last_card+1) + 6
    else:
        score += (last_card+1) + 0

print(score)

#PART 2

win_li = ['C','A','B']
lose_li = ['B','C','A']

score2 = 0
for i in li1[0]:
    if i[2] == 'X':
        score2 += (lose_li.index(i[0])+1) + 0
    elif i[2] == 'Z':
        score2 += (win_li.index(i[0])+1) + 6
    else:
        score2 += (opponent_li.index(i[0])+1) + 3

print(score2)