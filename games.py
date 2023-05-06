

class games:
    def __init__(self):
        self.rep = print(input("Start the game (y/n):"))
        self.guess = 0
        self.word = "animal"
        if self.rep == "y":
            self.startGame()
        else:
            print("ok bye")


#fucntion to play the game
    def startGame(self):

        self.drawGraph()
        print(input("\nentrer une lettre:"))





#fucntion to draw the graph
    def drawGraph(self):

        if self.guess == 0:
            print("|------|\n"
                  "|      |\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|========\n")
            for i in range(len(self.word)):
                print("_", end=" ")


    # def graphPrinter(self):
    #     #nmMot = main.nmMot here we gonna get the word choosed randomly by the main
    #     print("|----|")
    #     print("|    |")
    #     print("|    o")
    #     print("|    |"
    #           "|  --|--"
    #           "|   / \ ")









# start by priting the graph (hangman), then we dispaly the
# spot where the word should be placed, we give to the user the categorie
# of the word so he could have a clue, if the user guess one
# lette we dispaly the word:
#
# categorie : animal(example)
#
# |----|
# |    |
# |    o
# |    |
# |  --|--
# |   / \
# |
# |---------
#
# word : _______
#


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = games()
    print(game.startGame())

