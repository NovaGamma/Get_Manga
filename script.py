import json

reads = []
with open('read.txt','r') as file:
    for line in file:
        line = line.rstrip('\n')
        if line != '':
            line = line.split('/')
            if len(line) > 1:
                for name in line:
                    reads.append(name)
            else:
                reads.append(line[0])

with open('read.json','w') as save:
    json.dump(reads, save)
