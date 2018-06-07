file = open(r"word.txt", "r")

content = file.read()
words = content.split("\n")
f = open('output.txt','w')
for i in words:
    f.write(i + "," + str(len(i)))
    f.write("\r")

f.close()

file.close()