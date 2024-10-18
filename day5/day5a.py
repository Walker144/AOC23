class mapping:
    def __init__(self, destinationstart, sourcestart, rangelength):
        self.destinationstart = destinationstart
        self.sourcestart = sourcestart
        self.rangelength = rangelength
    def insidesource(self, value):
        return self.sourcestart <= int(value) <= self.sourcestart + self.rangelength
    def calculatedestination(self, value):
        return self.destinationstart + value - self.sourcestart
    def __repr__(self):
        return f'{self.destinationstart} {self.sourcestart} {self.rangelength}'

class mappingset:
    def __init__(self):
        self.mappings = []

    def addmapping(self, mapping):
        self.mappings.append(mapping)
    def __repr__(self):
        return str(self.mappings)






document = open('day5/day5input.txt','r').read().split('\n\n')

seeds = document[0].split(':')[1].split(' ')[1::]
seedlist = []


for i in range(len(seeds)//2):
    for j in range(int(seeds[i*2]),int(seeds[i*2+1])+1):
        seedlist.append(j)

mappingsets = []

for i in range(1,8):
    settoadd = mappingset()
    line = document[i].split('\n')[1::]


    for m in line:
        m = m.split(' ')

        settoadd.addmapping(mapping(int(m[0]),int(m[1]),int(m[2])))
    mappingsets.append(settoadd)



newseeds = []
i = 0
for seed in seeds:
    for mappingset in mappingsets:
        part = True
        for mapping in mappingset.mappings:
            if mapping.insidesource(seed) and part:
                seed = mapping.calculatedestination(seed)
                part = False
    if i % 1000 == 0:
        print(i)
    newseeds.append(seed)
print(min(newseeds))




    


