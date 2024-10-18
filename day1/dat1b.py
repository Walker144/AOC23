
import string
alphabet = string.ascii_lowercase
total =  0
document = open('day1/day1in.txt','r').read().split('\n')
print(document)
dic = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,'zero':0}


for line in document:
    
    linecache = ''

    for character in line:
        if character not in alphabet:
            linecache += character
        else:
            linecache += character

            for word in ['one','two','three','four','five','six','seven','eight','nine','zero']:
                if word in linecache:
                    linecache = linecache.replace(word, str(dic[word]) + word[-1]  )

    line = list(linecache)
    
    for i in range(10):
        for letter in alphabet:
            if letter in line:
                line.remove(letter)

    

            

    print(line)
    linecache = line
    
    total += int(linecache[0] + linecache[-1])








print(total)