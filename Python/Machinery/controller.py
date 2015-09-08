

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

    def __init__(self):
        self.transitions = {  }
        self.datapath = None

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

        if from_state in self.trantions.keys():
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


class State(object):

    def __init__(self):
        pass


class FSMD(object):

    def __init__(self):
        pass
