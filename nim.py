"""
nim.py
Josh Schmitz

Implements Nim class which is used as the main game driver. Keeps track of the current state while allowing the user and bot to take turns making moves. This class
is also in charge of getting the user input to make moves.
"""

import random
from nim_player import NimPlayer
from state import State
from move import Move


class Nim():
    """
    Keeps track of the current game state and gets input from user and bot to make their moves.
    
    attributes
        self.state: State() object representing the current number of stones in each row.
    """
    

    def __init__(self, goesFirst=None, outputFile=None):
        """
        Default value constructor initializes the state and determines who goes first. Calls self.main() which actually starts the game.
        
        paramaters
            goesFirst: "Bot" or "Player" will determine who goes first; leave blank for random choice
            outputFile: the output file to write to; leave blank for no output file
        """
        self.state = State()
        if goesFirst in ["Player", "Bot"]:
            self.main(goesFirst, outputFile)
        else:
            self.main(random.choice(["Player", "Bot"]), outputFile)
    

    def main(self, goesFirst=random.choice(["Player", "Bot"]), outputFile=None):
        """
        Main game loop. Let the bot and player take turns modifying the game state until the game is over. Outputs the current state to the console and outputFile.
        
        paramaters
            goesFirst: "Bot" or "Player" will determine who goes first; leave blank for random choice
            outputFile: the output file to write to; leave blank for no output file
        """
        turn = goesFirst
        while not self.state.isFinished():
            self.state.print(outputFile)
            if turn == "Player":
                move = self.getInput()
                self.state.remove(move)
                if not self.state.isFinished():
                    turn = "Bot"
            else:
                self.state = State(NimPlayer.smartMove(self.state))
                if not self.state.isFinished():
                    turn = "Player"
        self.state.print(outputFile)
        print("%s wins!" % turn)
        if outputFile:
            outputFile.write("%s wins!" % turn)


    def getInput(self):
        """
        Gets and validates user input specifying what move to make.
        
        return
            Move() object: describes the move that the user chose.
        """
        moveStr = input("Your turn: ")
        while not self.isValidMoveStr(moveStr):
            print("Invalid remove. Choose a row in which to remove from and the number of stones to remove.")
            print("Format as: row num")
            print("ie to remove 3 stones from row 0 you would type: 0 3")
            moveStr = input("Your turn: ")
        row = int(moveStr.split()[0])
        num = int(moveStr.split()[1])
        return Move(row, num)

    
    def isValidMoveStr(self, moveStr):
        """
        Determines if a move (specefied as the user entered string) is valid. This method just checks to make sure that the string is the right format for a move,
        then calls State.isValidMove() to determine if the specefied move is actually possible on the current board.

        paramaters
            moveStr: string specifying the desired move; should look like 'row num' where row is the row to remove from and num is the num to be removed
        
        return
            bool: represents whether or not the move is valid
        """
        if len(moveStr.split()) != 2:
            return False
        elif not (moveStr.split()[0].isdigit() and moveStr.split()[1].isdigit()):
            return False
        else:
            return self.state.isValidMove(Move(int(moveStr.split()[0]), int(moveStr.split()[1])))

