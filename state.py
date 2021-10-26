"""
state.py
Josh Schmitz
Machine Learning
HW7

Implements the State() class used for storing and modifying nim game states.
"""

import random
from move import Move

class State():
    """
    Stores an integer array specifying the number of stones in each row. Has methods for modifying the state and determining if moves are valid.
    
    attributes
        self.numRows: int - the number of rows in the game
        self.state: list - the number of stones in each row
    """
    
    
    def __init__(self, stateToCopy=None):
        """
        DVC, Copy Constructor (if stateToCopy is a State() obj), or EVC (if stateToCopy is a list).
        
        paramaters
            stateToCopy: State() object - a state to copy; leave blank for DVC
        """
        if not stateToCopy: # DVC
            self.numRows = 4
            self.state = [7, 5, 3, 1]
        elif isinstance(stateToCopy, list): # EVC
            self.numRows = len(stateToCopy)
            self.state = stateToCopy
        else: # copy constructor
            self.numRows = stateToCopy.numRows
            self.state = [stateToCopy.state[i] for i in range(self.numRows)]


    def isFinished(self):
        """
        Determines if all the stones have been removed.
        
        return
            bool: represents whether the game has finished or not
        """
        for row in self.state:
            if row:
                return False
        return True

    
    def isValidMove(self, move):        
        """
        Determines whether a given move is possible on the current game state.
        
        paramaters
            move: Move() object - the move in question
        
        return
            bool: whether or not the given move is possible
        """
        if move.row < 0 or move.row > 3:
            return False
        elif move.num > self.state[move.row]:
            return False
        elif move.num < 1:
            return False
        return True
        

    def randomMove(self):
        """
        make a random move
        
        return
            self - the state of the game after the random move has been done
        """
        validMoves = self.getValidMoves()
        move = random.choice(validMoves)
        return self.remove(move)


    def remove(self, move):
        """
        Remove stones from a row.
        
        paramaters
            move: Move() object - the move to make
        
        return
            self: State() object - the state after the move has been made
        """
        self.state[move.row] -= move.num
        return self


    def getNumCounts(self):
        """
        Gets the number of 1s, 2s, and 4s left on the board.
        
        return
            numCounts: dict - the number of 1s, 2s, and 4s left on the board
        """
        rowCounts = self.getRowCounts()
        numCounts = {1: 0, 2: 0, 4: 0}
        for row in rowCounts:
            for num in row:
                numCounts[num] += 1
        return numCounts


    def getRowCounts(self):
        """
        Gets a list representing the current state where each row is split into 4s, 2s, and 1s. ie [1, 3, 5, 7] will give [[1], [2, 1], [4, 1], [4, 2, 1].
        
        returns
            rowCounts: list - a list representing the current state where each row is a list with some combination of 1, 2, and 4 summing to the total number of 
                stones in the row
        """
        nums = [4, 2, 1]
        rowCounts = [[] for i in range(self.numRows)]
        for i in range(self.numRows):
            remaining = self.state[i]
            for num in nums:
                if remaining >= num:
                    remaining -= num
                    rowCounts[i].append(num)
        return rowCounts


    def print(self, outputFile=None):
        """
        Prints the current state.
        
        paramaters
            outputFile: file - the file to output to; leave blank for no output file
        """
        for i in range(self.numRows):
            print("%s:" % i, end="")
            if outputFile:
                outputFile.write("%s:" % i)
            for j in range(self.state[i]):
                print(" * ", end="")
                if outputFile:
                    outputFile.write(" * ")
            print()
            if outputFile:
                outputFile.write("\n")
        print()
        if outputFile:
            outputFile.write("\n")


    def getChildStates(self):
        """
        Get all the possible child states.
        
        return
            list of State() objects: all the possible child states
        """
        return [State(self).remove(move) for move in self.getValidMoves()]
        

    def getValidMoves(self):
        """
        Gets a list of all the possible moves.
        
        return
            list of Move() objects: all of the possible moves from the current state
        """
        validMoves = []
        for i in range(self.numRows):
            validMoves += [Move(i, j + 1) for j in range(self.state[i])]
        return validMoves