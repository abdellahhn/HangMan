# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import random
#
# import games
# from wordsDict import words
#
# class Main:
#     def __init__(self, nmbMot, mot):
#         self.nmbMot = nmbMot
#         self.mot = mot
#
#
#     def wordChooser(self):
#         print(words)
#         lol = random.randint(0, 3)
#         print(lol)
#         for index, item in enumerate(words):
#             if index == lol:
#                 print(index)
#                 print(item)
#                 return item
#             self.mot = item
#
#     def getMot(self):
#         return self.mot
#
#     def graphPrinter(self):
#         #nmMot = main.nmMot here we gonna get the word choosed randomly by the main
#         print("|----|")
#         print("|    |")
#         print("|    o")
#         print("|    |\n"
#               "|  --|--\n"
#               "|   / \ \n")
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#     print("|----|")
#     print("|    |")
#     print("|    o")
#     print("|    |\n"
#           "|  --|--\n"
#           "|   / \ \n")
#
#
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     print("categorie :", words.keys())
#     mot = print(input("choisisez une categorie: "))
#     for i in words.keys():
#         print(i)
#         # if i == mot:
#             # print(mot)
#         # print(mot)
#     #     here well call the draw function
#     # main = Main()
#     # print(main.getMot())
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
