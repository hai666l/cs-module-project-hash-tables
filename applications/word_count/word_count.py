def word_count(s):
    s = s.lower()
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&' ]

    # Split string by spaces and NULL terminator into a list, remove ignore chars from each word in that list
    words = s.split()
    for i in range(0, len(words)):
        for c in ignore:
            words[i] = words[i].replace(c, '')

    # Prepare a dict count of each word in the list 
    out = {}
    for word in words:
        if word != "":
            out[word] = words.count(word)

    return out

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
