f = open(r"C:\Users\sreenaga sayana\Downloads\Python_Lesson1\Python_Lesson1\program3.txt", "r")

content = f.read()
line = content.split("\n")

for n in line:
    word = n.split(" ")
    print( " ".join(word), len(word))
f.close()