document = open('day4/day4input.txt','r').read().split('\n')
class scratchcard:
    def __init__(self,winning,mynumbers):
        self.mynumbers = mynumbers
        self.winning = winning
        self.value = 1

    def check(self):
        winners = 0
        for num in self.mynumbers:
            if num in self.winning:
                winners += 1
        return winners


scratchcards = []
for line in document:
    line = line.split('|')
    line = [line[0].split(':')[0],line[0].split(':')[1],  line[1]]

    winning = line[1].split(' ')
    
    mynumbers = line[2].split(' ')

    while '' in mynumbers:
        mynumbers.remove('')
    while '' in winning:
        winning.remove('')
    scratchcards.append(scratchcard(winning,mynumbers))

pos = 0

for card in scratchcards:
    winners = card.check()
    if winners > 0:
        for i in range(winners):
            scratchcards[pos + i + 1].value += card.value

    pos += 1


total = 0
for card in scratchcards:
    total += card.value
print(total)
