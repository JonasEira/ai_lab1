class FSM(object):
    def __init__(self, states=[]):
        self._states=states
        self.currentState = None

    def start(self,startState=None):
        """ Start the finite state machine
        """
        if not startState or not (startState in [x[0] for x in self._states]):
            raise ValueError("Not a valid start state")
        self.currentState = startState

    def stop(self):
        """ Stop the finite state machine
        """
        self.startState = None

    def printStates(self):
        for state in self._states:
            print('State transition: ' + state[0] + ' : ' + state[1] + " : " + str(state[2]));
    
    def addTransition(self,fromState, toState, testFunc):
        """ Add a state transition to the list, order is irellevant, loops are undetected 
            Can only add a transition if the state machine isn't started.
        """
        if not self.currentState:
            raise ValueError("StateMachine already Started - cannot add new transitions")

        # add a transition to the state table
        self._states.append( (fromState, toState,testFunc))

    def event(self, value):
        """ Trigger a transition - return a tuple (<new_state>, <changed>)
            Raise an exception if no valid transition exists.
            Callee needs to determine if the value should be consumed or re-used
        """
        if not self.currentState:
            raise ValueError("StateMachine not Started - cannot process event")

        # get a unique list of next states which are valid       
        self.nextState = list(set( \
                    [ x[1] for x in self._states\
                    if x[0] == self.currentState \
                            and (x[2]==value)] ) ) 
        if not self.nextState: 
            raise ValueError("No Transition defined from state {0} with value '{1}'".format(self.currentState, value))
        elif len(self.nextState) > 1:
            raise ValueError("Ambiguous transitions from state {0} with value '{1}' ->  New states defined {2}".format(self.currentState, value, self.nextState))
        else:
            self.lastState = self.currentState;
            self.currentState, ret = (self.nextState[0], True) \
                if self.currentState != self.nextState[0] else (self.nextState[0], False)
            return self.currentState, self.lastState, ret

    def runFunction(self, value):
        for state in self._states:
            if(state[0] == self.lastState and state[2] == value):
                return state[3];
        return 0;

    def getValidActions(self, state):
        allActions = list(x[2] for x in self._states if(state == x[0]));
        return allActions;
    
    def currentState(self):
        """ Return the current State of the finite State machine
        """
        return self.currentState
