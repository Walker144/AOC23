import string
alphabet = string.ascii_lowercase
total =  0
document = open('day1/day1in.txt','r').read().split('\n')
print(document)


for line in document:
    print(line)
    line = list(line)
    
    for i in range(10):
        for letter in alphabet:
            if letter in line:
                line.remove(letter)
    total += int(line[0] + line[-1])
    print(line)


print(total)
