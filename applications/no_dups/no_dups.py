def no_dups(s):
    words = s.split()
    s = ""
    for w in words:
        if s.find(w) == -1:
            s += w
            s += ' '
    return s[:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
