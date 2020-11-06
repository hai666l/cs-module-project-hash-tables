from word_count import word_count

def histogram(filename):
    with open(filename) as f:
        contents = f.read().lower()
        d = word_count(contents)
        # Sort dict by values, highest to lowest
        d = { k: v for k, v in sorted(d.items(), key=lambda ele: ele[1], reverse=True) }

        # Find longest word and use its length+2 as padding
        padding = 1
        for w in d.keys():
            if len(w) > padding:
                padding = len(w) + 2

        for word in d.keys():
            print(word , end="")
            print(' ' * (padding-len(word)), end="")
            print('#' * d[word])

histogram("robin.txt")
