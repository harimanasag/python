class Sentence:

    def middle(s):
        words = s.split(" ")
        cenWord = []
        center = int(len(words) / 2)

        if len(words) % 2 == 0:
            cenWord.append(words[center - 1])
            cenWord.append(words[center])
        else:
            cenWord = words[center]
            print("Middle words are:")
            print(cenWord)

    def Maxlength(s):
        longWord = ""
        words = s.split(" ")


        for word in words:
            if (len(word) > len(longWord)):
                longWord = word
        print("Longest word is:")
        print(longWord)


    def reverse(s):
        words = s.split(" ")
        rS = " "
        for i in range(len(words)):
            for word in reversed(words[i]):
                rS = rS + word
                rS = rS + " "
        print("Reversed sentence:")
        print(rS)

print("Enter your sentence:")
s = input()
Sentence.middle(s)
Sentence.Maxlength(s)
Sentence.reverse(s)