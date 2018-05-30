# MiniMax-AlphaBeta


# MiniMax
In this project a backtracking algorithm is used to determine the outcome of a decision in a game and searches for the most optimal decision to take. It is similar to going to the future after each play you decide to do and check with each other which was the optimal move to be taken.
There are two main agents (components) to this algorithm which are maximizer (gets highest score possible) and minimizer (gets lowest score possible).

/**
* Beta lowest action
* Alpha highest action
* /


getAction()
-- ( - sys.maxint ) Since we are using Minimax.
-- Loop through the allowed actions pacman agent is allowed to take to determine which node to go through next 
-- Once the best action is determined (when successor is larger than the minmax value we chose)

Value()
-- Returns whether the state of the succesor was for the maximizer or minimizer depending if max or min value was calculated.

Max_Value()
-- Max_Value function: returns the Minmax agent for the maximizer as the value of v is set to sys.maxint (NEGATIVE!!)
-- Then the function goes through the actions that the maximizer is allowed to take at each node.
-- Then loop through these action to determine the minmax root for the maximizer


Min_Value()
-- Min_Value function: returns the Minmax agent for the minimizer as the value of v is set to sys.maxint 
-- Then the function goes through the actions that the minimizer is allowed to take at each node.
-- Then loop through these action to determine the mini root for the minimizer

# Alpha Beta pruning
Main goal of Alpha Beta pruning would be to decrease the number of nodes visited (evaluated). It asks the maximizer or minimizer to use whichever move beleived to be better if it was a better move instead of checking each node before preceding withit. It is similar to MiniMax but has some difference to it as it avoids some of the branches when it reaches the final move or devision.

getAction()
-- ( - sys.maxint ) set Minimax value.
-- set a low action
-- Loop through the allowed actions pacman agent is allowed to take to determine which node to go through next 
-- Once the best action is determined replace the lowest move with it


Value()
-- Returns whether the state of the succesor was for the maximizer or minimizer depending if max or min value was calculated.

Max_Value()
-- Max_Value function: returns the Minmax agent for the maximizer as the value of v is set to sys.maxint (NEGATIVE!!)
-- Then the function goes through the actions that the maximizer is allowed to take at each node.
-- Then loop through these action to determine the minmax root for the maximizer but in this case it compares it to Beta if it actually is a better move alpha passed the max(alpha, v) then the value v is returned as best decision.

Min_Value()
-- Max_Value function: returns the Minmax agent for the maximizer as the value of v is set to sys.maxint 
-- Calculate the amount of minimizer agents
-- Then the function goes through the actions that the maximizer is allowed to take at each node.
-- Then loop through these action to determine the minmax root for the maximizer but in this case it compares it to Alpha if it actually is a better move Beta passed the min(Beta, v) then the value v is returned as best decision.
