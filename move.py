"""
move.py
Josh Schmitz
Machine Learning
HW7

Implements very basic Move() class that represents a move as two integer values: self.row (the row to remove from) and self.num (the number of stones to remove).
"""

class Move():
    """
    Basic class that represents a move as two integer values.
    
    attributes:
        self.row: integer - the row to remove from
        self.num: integer - the number of stones to remove
    """
    
    
    def __init__(self, row, num):
        """
        DVC sets the self.row and self.num values to the values provided.
        
        paramaters:
            row: int - the row to remove from
            self.num - the number of stones to remove
        """
        self.row = row
        self.num = num


    def print(self, outputFile=None):
        """
        Prints the move to the command line and, if given, the outputFile.
        
        paramaters
            outputFile: file - the file to write to; leave empty for no output file
        """
        print("row: %s; num: %s" % (self.row, self.num))
        if outputFile:
            outputFile.write("row: %s; num: %s\n" % (self.row, self.num))