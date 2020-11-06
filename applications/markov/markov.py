import random

# Helpers
def isStartWord(w):
    if w != "":
        if w[0] == '"': return True
        if w[0].isupper(): return True
    return False

def isStopChar(char):
    for c in ".?!":
        if char == c:
            return True
    return False

def isStopWord(w):
    if len(w) >= 2:
        if isStopChar(w[-1]) or (w[-1] == '"' and isStopChar(w[-2])):
            return True
    return False

# Open and read input text
d = dict()
with open("input.txt") as f:
    words = f.read().split()
    for i in range(0, len(words)):
        w = words[i]
        # Add word to dictionary
        if w not in d.keys():
            # If end of text not reached
            if i+1 != len(words):
                d[w] = [words[i+1]]
            # End of text reached, add a random word as follower
            else:
                d[w] = [random.choice(words)]
        # Word already in dictionary
        else:
            # Add the word following to array
            if i+1 != len(words):
                d[w].append(words[i+1])
            
# construct random sentence
start = ""
while isStartWord(start) != True:
    start = random.choice(list(d.keys()))
randomWord = start
i = 0
while i != 5:
    print(randomWord, end=' ')
    randomWord = random.choice(d[randomWord])
    if isStopWord(randomWord):
        i += 1
        print(f'{randomWord}\n')
        while isStartWord(randomWord) != True:
            randomWord = random.choice(list(d.keys()))
