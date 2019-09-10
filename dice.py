#I did this with the original program sheet
from random import choices
ntrials = 10000
limit = 6
player1wins=0
for i in range(ntrials):
    rand1 = choices(range(1,limit+1),k=3)
    rand1.sort(reverse=True)
    rand2 = choices(range(1,limit+1),k=2)
    if rand2[0] == rand2[1]:
        continue
    if rand1[0]+rand1[1] > rand2[0]+rand2[1]:
        player1wins=player1wins+1
print("Fraction=",player1wins/ntrials)