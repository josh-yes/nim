"""
nim_player.py
Josh Schmitz

Implements the NimPlayer() class which is a smart bot that makes optimal moves.
"""

from state import State
from move import Move

class NimPlayer():
    """
    Implements a bot for the game of nim that makes optimal moves.
    """


    def __init__(self):
        """
        Does nothing.
        """
        pass


    def play(self, state):
        """
        Decides what move to make based on the given state. Returns the state that results after the move is made.
        
        paramaters
            state: list or State() object - the current game state

        return
            list - the state after the move is made
        """
        return (NimPlayer.smartMove(State(state))).state


    def getStateVal(state):
        """
        Evaluates the quality of a state based on the number of stones in each row. Based on the idea that an optimal state will have an even number of 1s, 2s, and
        4s when each row is split up into those values. A val of 0 is optimal.
        
        paramaters:
            state: list - the game state to evaluate

        return
            val: int - the value of the given state; is 0 if the number of 1s, 2s, and 4s are all even (ie optimal), otherwise will be a positive number
        """
        val = 0
        numCounts = State(state).getNumCounts()
        for num in numCounts.keys():
            if numCounts[num] % 2 != 0:
                val += 1
        return val


    def smartMove(state):
        """
        Determines what the optimal move is by determining the valuation of all the possible child states and choosing the optimal one if it exists, otherwise
        removing 1 stone from the first possible row.
        
        paramaters
            state: State() object - the current game state
        
        return
            State() object - the state after of the optimal move has been done
        """
        childStates = state.getChildStates()
        for childState in childStates:
            val = NimPlayer.getStateVal(childState)
            if val == 0:
                return childState
        for i in range(state.numRows):
            if state.state[i] > 0:
                return state.remove(Move(i, 1))

