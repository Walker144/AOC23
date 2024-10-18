document = open('day3/day3input.txt','r').read().split('\n')
snakes = []
total = 0

class Snake():
    def __init__(self, positions, value):
        self.positions = positions
        self.value = value
        self.hit = False
    def check_if_hit(self, position):
        if position in self.positions and not self.hit:
            self.hit = True
            return self.value
        return 0
    def __repr__(self):
        return f'{self.positions} {self.value}'
    def reset(self):
        self.hit = False

#creating the snakes

y = 0
part = ''
for line in document:
    print(line)
    line = list(line)

    if part != '':
                snakes.append(Snake(positions, int(part)))
                part = ''
                positions = []



    part = ''
    positions = []
    x = 0

    for i in range(len(line)):
        if line[i] in ['1','2','3','4','5','6','7','8','9','0']:
            part += line[i]
            positions.append([x,y])
        else:
            if part != '':
                snakes.append(Snake(positions, int(part)))
                part = ''
                positions = []
        x += 1
    y += 1



#checking if the snakes hit

y=0
for line in document:
    line = list(line)
    x = 0
    for element in line:
        if element not in ['1','2','3','4','5','6','7','8','9','0','.']:
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    for snake in snakes:
                        total += snake.check_if_hit([x+dx,y+dy]) 
                    

        x += 1
                            
    y += 1

print(total)