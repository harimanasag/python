heightinput= int(input("Enter the height of the board: "))
widthinput= int(input("Enter the width of the board: "))


def board_draw(heightinput, widthinput):
    for i in range(0,heightinput):
        for j in range(0, widthinput):
            print(" ---", end=" ")
        print("\r")
        for j in range(0,widthinput+1):
            print("|   ", end= " ")
        print("\r")
    for j in range(0, widthinput ):
        print(" ---", end=" ")

board_draw(heightinput,widthinput)