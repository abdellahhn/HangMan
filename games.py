

class games:
    def __init__(self):
        self.rep = print(input("Start the game (y/n):"))
        self.guess = 6
        self.word = "animal"
        self.finalWord = ""

        self.startGame()
        # if self.rep == "y":
        #     self.startGame()
        # else:
        #     print("ok bye")


#fucntion to play the game
    def startGame(self):
        self.drawGraph()
        for i in range(len(self.word)):
            print("_", end=" ")


        word = "animal"
        gues = len(word)
        print(word, gues)
        for i in range(len(self.word)):
            lettre = str(input("Entrez une lettre:"))

            if lettre in self.word:
                print("val")
                self.finalWord += lettre
                print(self.finalWord)
                self.drawGraph()
            elif lettre != self.word:
                self.guess -= 1
                self.drawGraph()
                print("ressayer")







#fucntion to draw the graph
    def drawGraph(self):

        if self.guess == 6:
            print("|------|\n"
                  "|      |\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|========\n")
        elif self.guess == 5:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "|========\n")
        elif self.guess == 4:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "|      |\n"
                  "| \n"
                  "| \n"
                  "|========\n")
        elif self.guess == 3:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "|     /|\n"
                  "| \n"
                  "| \n"
                  "|========\n")
        elif self.guess == 3:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "|     /|\ \n"
                  "|"
                  "|"
                  "|========\n")
        elif self.guess == 2:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "|     /|\ \n"
                  "|     / \n"
                  "| \n"
                  "|========\n")
        elif self.guess == 3:
            print("|------|\n"
                  "|      |\n"
                  "|      0\n"
                  "|     /|\ \n"
                  "|     / \ \n"
                  "| \n"
                  "|========\n")



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
    print(game.__init__())

