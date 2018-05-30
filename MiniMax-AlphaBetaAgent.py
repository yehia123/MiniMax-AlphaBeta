class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 1)
    """

    def getAction(self, game_state):
        """
        Returns the best minimax action from the current game_state using
          self.depth and self.evaluationFunction.
        Here are some method calls that are useful when implementing minimax.
        game_state.getLegalActions(agent):
            Returns a list of legal actions for an agent
            agent=0 means Pacman, ghosts are >= 1
        game_state.generateSuccessor(agent, action):
            Returns the successor game state after an agent takes an action
        game_state.getNumAgents():
            Returns the total number of agents in the game
        game_state.isWin():  Returns True if this is a terminal winning state
        game_state.isLose():  Returns True if this is a terminal losing state
        """
        "*** YOUR CODE HERE ***"
        v = - sys.maxint #low minimax value
        best_action = 'None' #low action
        for action in game_state.getLegalActions(0): #loop thru actoion  find minimax for right node
            suc = self.value(game_state.generateSuccessor(0, action), 1, 1)
            if suc > v:
                v = suc
                best_action = action
        return best_action



    def value(self, game_state, agent, current_depth):
        # type: (object, object, object) -> object
        """ Returns the minimax value of any state"""
        "*** YOUR CODE HERE ***"
        #updates current depth

        if game_state.isWin() or game_state.isLose() or current_depth > self.depth : #checks for terminal state or non
            return self.evaluationFunction(game_state)

        if agent == 0: #checks if agent is pacman to use minimax
            return self.max_value(game_state, current_depth)
        else: #else uses min agent
            return self.min_value(game_state, agent, current_depth)


    def max_value(self, game_state, current_depth):
        # type: (object, object) -> object
        """Returns the minimax value of a state under Pacman's control (max)"""
        "*** YOUR CODE HERE ***"
        v = -sys.maxint
        actions = game_state.getLegalActions(0)
        for action in actions: #loops thru actions to find minimax of root for pacman
            v = max(v, self.value(game_state.generateSuccessor(0, action), 1, current_depth))
        return v


    def min_value(self, game_state, agent, current_depth):
        """Returns the minimax value of a state under a ghost's control (min)"""
        "*** YOUR CODE HERE ***"
        v = sys.maxint
        next_agent = (agent + 1)% game_state.getNumAgents()
        if next_agent == 0:
            current_depth += 1
        actions = game_state.getLegalActions(agent)
        for action in actions:#loops thru actions to find mini of root for ghosts
            v = min(v, self.value(game_state.generateSuccessor(agent, action), next_agent, current_depth))
        return v

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the best minimax action from the current game_state using
          self.depth and self.evaluationFunction.
        """
        "*** YOUR CODE HERE ***"
        v = -sys.maxint
        best_action = 'None'
        alpha = -sys.maxint #updates alpha
        beta = sys.maxint
        for action in gameState.getLegalActions(0): #loops thru actions finds best action related to sucessor
            suc = self.value(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            if suc > v:
                alpha = -sys.maxint
                v = suc
                best_action = action
        return best_action


    def value(self, game_state, agent, current_depth, alpha, beta):
        """ Returns the minimax value of any state"""
        "*** YOUR CODE HERE ***"

        if game_state.isWin() or game_state.isLose() or current_depth > self.depth: #checks if it exceed depths
            return self.evaluationFunction(game_state)

        if agent == 0:
            return self.max_value(game_state, current_depth, alpha, beta)
        else:
            return self.min_value(game_state, agent, current_depth, alpha, beta)


    def max_value(self, game_state, current_depth, alpha, beta):
        """Returns the minimax value of a state under Pacman's control (max)"""
        "*** YOUR CODE HERE ***"
        v = -sys.maxint
        actions = game_state.getLegalActions(0)
        for action in actions: #uses alpha and beta to use pruning
            v = max(v, self.value(game_state.generateSuccessor(0, action), 1, current_depth, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v


    def min_value(self, game_state, agent, current_depth, alpha, beta):
        """Returns the minimax value of a state under a ghost's control (min)"""
        "*** YOUR CODE HERE ***"
        v = sys.maxint
        next_agent = (agent + 1) % game_state.getNumAgents()
        if next_agent == 0:
            current_depth += 1
        actions = game_state.getLegalActions(agent)
        for action in actions:
            v = min(v, self.value(game_state.generateSuccessor(agent, action), next_agent, current_depth, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v