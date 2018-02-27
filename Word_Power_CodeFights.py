def wordPower(word):
    num = dict(zip(list(map(chr, range(97, 123))),[ i+1 for i in range (26)]))
    return sum([num[ch] for ch in word])
