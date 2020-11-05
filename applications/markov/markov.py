import random

d = dict()
with open("input.txt") as f:
    words = f.read().split()
    for i in range(0, len(words)):
        w = words[i]
        if w not in d.keys():
            if i+1 != len(words):
                d[w] = [words[i+1]]
            else:
                d[w] = [random.choice(words)]
        else:
            if i+1 != len(words):
                d[w].append(words[i+1])
            
# construct random sentence
start = random.choice(list(d.keys()))
stop = random.choice(list(d.keys()))

randomWord = start
while randomWord != stop:
    print(randomWord, end=' ')
    randomWord = random.choice(d[randomWord])
print(stop)
