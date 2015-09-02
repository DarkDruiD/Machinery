
"""
Datapath

    The datapath is in charge of dealing with the manipulations
    and readings of the input data
"""


class Datapath(object):

    def __init__(self):
        self.paths = {  }

    def add_variable(self, var_name):
        """
        Adds a variable name in the paths map
        this will allow you to further access the
        variables update functions.
        """

        if var_name in self.keys():
            raise ValueError("The variable with name %r is already in use.", (var_name))

        self.paths[var_name] = (None, None)

    def add_read_function(self, var_name, function):
        """
        This will add the update function to the variable,
        and set the variable value as None.
        """

        if not var_name in self.keys():
            raise ValueError("The variable %r has not been set.", (var_name))

        self.paths[var_name] = (function, None)

    def add_path(self, var_name, function):
        """
        This method will create the variable name
        and add an update function to it, and also will
        set the variable value to None in the tuple.
        """

        self.paths[var_name] = (function, None)

    def update_variables(self):
        """
        This method will read all the variables and return
        the values in to the tuple second position
        """

        for var, funct in self.path.items():
            self.paths[var][1] = funct()

"""
State
"""

class State(object):

    def __init__(self, name):
        self.name = name


"""
State Table

    if defined by a 4-tuple <Si, Sj, Omega_h, Beta_h> where:

        * Si is the actual state
        * Sj is the next state
        * Omega_h is the input conditions
        * Beta_h is the output of the transition

    Omega_h must be a boolean condition functions, this will
    set the footprints for when you must do a transition
"""


class StateTable(object):

    def __init__(self):
        self.table = {  }

    def add_transition(self, Si, Sj, omega, beta=None):
        """
        Sets the dictionary to hash the current state to a
        triplet that contains the conditional function omega
        and the output function beta
        """
        if not Si in self.table.keys():
            self.table[Si] = [(Sj, omega, beta)]

        self.table[Si].append((Sj, omega, beta))


"""
FSMD

    Is defined by a 7-tuple <Z, X, Y, V, Delta, Lambda, Z0> in which:

        * Z is a set of states {Z0, Z1, Z2, ... , Zn}
        * X is a set of inputs {X0, X1, X2, ... , Xn}
        * Delta is a transition function, maps a tuple of a
          state and a input to a following state (Zx, Xx) -> Zy
        * Lambda is a function that transforms a state into an
          output (Zx) -> Yx
        * Z0 is the initial state

    due to the use of the word lambda in python ill change it for the
    kappa letter.

    The Delta transition function is represented by the State Table.

    The inputs are handled by the Datapath.
"""


class FSMD(object):

    def __init__(self, states, datapath, init_state):
        self.states = states
        self.datapath = datapath

    def update_variables(self):
        pass

    def update_fmsd(self):
        pass
