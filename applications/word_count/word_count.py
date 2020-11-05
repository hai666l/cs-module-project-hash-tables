def word_count(s):
    s = s.lower()
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&' ]

    for c in ignore:
        s = s.replace(c, '')
    words = s.split()

    d = {}
    for w in words:
        d[w] = words.count(w)

    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
