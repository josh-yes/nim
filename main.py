#!/Users/joshuaschmitz/opt/anaconda3/bin/python3
"""
main.py
Josh Schmitz
Machine Learning
HW7

Starts a game of nim using the Nim class in nim.py. Takes command line arguments to determine whether the player or bot should go first. The user can specify
whether they want to go first or whether the bot should go first by entering the command line arg of Bot or Player.
"""


from nim import Nim
from nim_player import NimPlayer
import sys


outputFile = open("output.txt", "w")
if len(sys.argv) > 1 and sys.argv[1] in ["Bot", "Player"]:
    nim = Nim(sys.argv[1], outputFile)
else:
    nim = Nim(outputFile=outputFile)
outputFile.close()