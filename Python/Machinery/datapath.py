
class Datapath(object):

    """
    Manages the data flow.

    This class manages tow fundamental types of data
    static data represented by values, and variables data
    represented by variables, the values will be setted to
    a simple value and stored in a dict, and the variables will
    need an update function that will be called wen its data is
    solicited, this will be stored in a dict and will have its
    name as key and the update function as variables
    """

    def __init__(self):
        """Initializes empty dicts for storing variables and values"""
        self.variables = {}
        self.values = {}

    def add_variable(self, var_name, update_func):
        """
        Stores the variable in a dict with its name as key
        and the update function as the value.

        This function should receive no arguments and should
        return a value from it, a simple example would be
        something like this:

            d = Datapath()

            def rand_value():
                import random
                return random.randint(0, 100)

            d.add_variable("random_0_100", rand_value)
        """
        self.variables[var_name] = update_func

    def add_value(self, val_name, val):
        """
        Stores the values in a dict with its name as key
        and the static value as the value
        """
        self.values[val_name] = val

    def delete_value(self, val_name):
        """Removes the variable with var_name from the dict"""
        self.values.pop(val_name, None)

    def delete_variable(self, var_name):
        """Removes the values with val_name from the dict"""
        self.variables.pop(var_name, None)

    def get_variable(self, var_name):
        """Returns the updated value of the variable read from the function"""
        if var_name not in self.variables.keys():
            raise ValueError("{} has not been defined.".format(var_name))

        return self.variables[var_name]()

    def get_value(self, val_name):
        """Returns the value of the dict"""
        if val_name not in self.values.keys():
            raise ValueError("{} has not been defined".format(val_name))

        return self.values[val_name]

    def get_all_variables(self):
        """
        Reads all the variables and stores the values
        returned by the update functions in a dict with
        the variable names as the key
        """

        all_vars = {}

        for var, func in self.variables.items():
            all_vars[var] = func()

        return all_vars

    def get_all_values(self):
        """Returns the values in the dict"""
        return self.values
