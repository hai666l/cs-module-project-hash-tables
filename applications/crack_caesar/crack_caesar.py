from string import ascii_uppercase

def crack_caesar(filename):
    # Most -> Least
    commonLetters = [ 'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z' ]

    # Amount of each letter found
    letterCounts = dict()
    for c in ascii_uppercase:
        letterCounts[c] = 0

    # Open file
    with open(filename) as f:
        # Count amount of times each letter is found
        cipherText = f.read()
        for c in cipherText:
            if c in ascii_uppercase:
                letterCounts[c] += 1

        # Sort letters by count, Most -> Least, into a list
        letterCounts = list({k: v for k, v in sorted(letterCounts.items(), key=lambda ele: ele[1], reverse=True)}.keys())

        # Map Cipher char to commonLetters char
        keyMap = dict()
        for i in range(0, len(ascii_uppercase)):
            keyMap[letterCounts[i]] = commonLetters[i]

        # Now have our KeyMap, create new file for decoded output
        with open('decoded.txt', 'w') as output:
            for cipherChar in cipherText:
                if cipherChar in ascii_uppercase:
                    output.write(keyMap[cipherChar])
                else:
                    output.write(cipherChar)
            output.close()

if __name__ == '__main__':
    crack_caesar('ciphertext.txt')
