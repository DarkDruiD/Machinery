
"""
Datapath

    The datapath is in charge of dealing with the manipulations
    and readings of the input data
"""


class Datapath(object):

    def __init__(self):
        self.vars = {  }

    def add_var(self, var_name):
        self.vars[var_name] = None

    def add_update_function(self, var_name, func):
        self.vars[var_name] = func

    def add_func_and_var(self, var_name, func):
        self.vars[var_name] = func

    def update(self):
        data = [  ]

        for var, func in self.vars.items():
            data.append((var, func()))

        return data


"""
State
"""

class State(object):

    def __init__(self, name):
        self.name = name
        self.on_start = None

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

    def get_transitions(self, Si):
        return self.table[Si]

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

    def __init__(self, states, datapath, state_table, init_state):
        self.vars = None
        self.curr_state = init_state

        self.states = states
        self.datapath = datapath
        self.init_state = init_state
        self.state_table = state_table

    def update_variables(self):
        self.vars = self.datapath.update()

    def update_fmsd(self):
        trans = self.state_table.get_state(self.curr_state)

        for tr in trans:
            if tr[1]:
                self.curr_state = tr[0]
                if self.curr_state.on_start:
                    self.curr_state.on_start()

    def get_current_state(self):
        return self.curr_state
