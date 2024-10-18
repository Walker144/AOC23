document = open('day2/day2in.txt','r').read().split('\n')
dic = {'blue':14,'red':12,'green':13}
total = 0

for line in document:
    line = line.split(':')
    id = line[0].split(' ')[1]

    gameset = line[1]

    gameset = gameset.split(';')
    valid = True
    minred = 0
    minblue = 0
    mingreen = 0

    for game in gameset:
        parts = game.split(',')
        
        for part in parts:
            part = part.split(' ')

            
            if part[2] == 'red' and int(part[1]) > minred:
                minred = int(part[1])
            elif part[2] == 'blue' and int(part[1]) > minblue:
                minblue = int(part[1])
            elif part[2] == 'green' and int(part[1]) > mingreen:
                mingreen = int(part[1])    
                    
    if valid:
        print(minred,minblue,mingreen)
        total += minred * minblue * mingreen

print(total)

        
