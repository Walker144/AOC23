document = open('day4/day4input.txt','r').read().split('\n')
total = 0

for line in document:
    line = line.split('|')
    line = [line[0].split(':')[0],line[0].split(':')[1],  line[1]]

    winning = line[1].split(' ')
    
    mynumbers = line[2].split(' ')

    while '' in mynumbers:
        mynumbers.remove('')
    while '' in winning:
        winning.remove('')

    print(winning,mynumbers)

    score = 0.5

    for num in mynumbers:
        if num in winning:
            score = score * 2

    if score != 0.5:
        total += score
        score = 0.5

    
print(total)