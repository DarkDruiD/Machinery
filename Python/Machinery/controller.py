

class Delta(object):

    """
    Transition Table

    This is the Delta function described in the FSMD and will
    manage how to transition from a certain state to another one
    based in boolean function build from the values of the Datapath.

    This delta function will be defined formally as a function
    [(S_i, Alpha_h, Beta_h) -> S_j] in which:

        *S_i: Is the current state of the FSMD

        *Alpha_h: Is a function that will return a boolean value
         from conditions based out of the datapath variables and
         values

        *Beta_h: Is a function that will generate output values
         based optionally on the datapath values and variables.

        *S_j: Is the state in which will transition to based in
         the previous values

    The transition will have a collection of this delta functions
    in order to transition from any arbitrary state to another state.
    """

    def __init__(self, datapath=None):
        """Initialization of transitions and datapath"""
        self.transitions = {}
        self.datapath = datapath

    def set_datapath(self, datapath):
        """Add datapath instance to the class"""
        self.datapath = datapath

    def add_transition(self, from_state, to_state,
                       trans_func, output_func):

        """
        This function will add one transition to the collection of
        delta functions, logically this will get all the parameters
        needed by the delta function

            *S_i = from_state

            *Alpha_h = trans_func

            *Beta_h = output_func

            *S_j = to_state

        The Alpha_h function must receive a datapath instance in order
        to access to the variables, like this:

            def trans(dp):
                rand_var = dp.get_variable("rand_var")

                if rand_var > 50:
                    return True

                return False
        """

        if from_state in self.transitions.keys():
            self.transitions[from_state].append((
                to_state,
                trans_func,
                output_func
            ))

            return

        self.transitions[from_state] = []
        self.transitions[from_state].append((
            to_state,
            trans_func,
            output_func
        ))

    def transition(self, from_state):
        """
        Given a state this function will calculate if you can
        got to another state given the delta function returning
        True or False respectively.
        """

        transitions = self.transitions[from_state]

        for trans in transitions:
            if trans[1](self.datapath):
                if trans[2]:
                    trans[2](self.datapath)

                return trans[0]

        return None


class State(object):

    """
    State

    This will be an abstraction of a state element of the FSMD
    this is needed in order to simplify the callbacks needed in
    certain events in the status transition cycle.
    """

    def __init__(self, name):
        self.name = name
        self.on_enter = None
        self.on_leave = None


class FSMD(object):

    """
    FSMD

    Is a simple expansion of a normal FSM in which
    you may use values different than a boolean value,
    this is composed by a 7-tuplet <Z, X, Y, V, Delta, Lmabda, Z_0>
    in which:

        *Z is a set of states.

        *X is a set of input values this is represented by
         the datapath object.

        *Y is a set of output values represented by a set of
         variables that may write values to the datapath.

        *Delta is a transition function represented by the state table.

        *Lambda is a function that generates output values.

        *Z_0 is the initial state.
    """

    def __init__(self, state_set, datapath, state_table, initial_state):
        self.init_state = initial_state
        self.state_table = state_table
        self.state_set = state_set
        self.datapath = datapath

        self.curr_state = initial_state

        self.state_table.set_datapath(datapath)

        self.init_state.on_enter()

    def run(self):

        while True:
            new_state = self.state_table.transition(self.curr_state)

            if new_state:
                if self.curr_state.on_leave:
                    self.curr_state.on_leave()

                self.curr_state = new_state

                if self.curr_state.on_enter:
                    self.curr_state.on_enter()
