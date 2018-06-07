def LongestWord(wordslist):
    word_len = []

    for n in wordslist:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(LongestWord(["PHP", "Computer", "Science"]))