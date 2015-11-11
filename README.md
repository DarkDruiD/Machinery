# Machinery
---

The FSM are a simple yet complete approach to solve automation problems, but from time to time in system development libraries fall short for the need and a simple FSM that provides states and transitions is far from enough, that is why this library was written, in order to allow you to make a full project based in a FSMD machine that allows you to read variables and operate and change states with the values.


## States
The states have tow possible actions, the first is executed when the FSMD enters a state and the second one is executed when the FSMD leaves the state.
```python
from Machinary.automaton import State

def locked_on_enter():
    print "Entered locked state"

def locked_on_leave():
    print "Leaved locked state"

locked = State("locked")
locked.on_enter = locked_on_enter
locked.on_leave = locked_on_leave
```


## Datapath

The datapath is the functional piece that allows you to read variables and store values.

The datapath make a difference between the variables and the values, calling variables the ones that may need to be read constantly during the automaton execution loop, and naming values the ones that may be stored during a single step or transitional moments.


To create a variable you can do it like this:
```python
from Machinary.automaton import Datapath

datapath = Datapath()

def read_coin_function():
    return random.randint(0, 1)

datapath.add_variable("coin", read_coin_function)
```
The add_variable method should receive a name and a function to read the values from, the FSMD will be in charge of dealing with the reads of the variable.

You might desire to delete this variables in the running time, this can be accomplished by the following code:
```python
datapath.delete_variable("coin")
```

To create a value you can doit like the following:
```python
datapath.add_value("time", 4)
```

In a similar fashion of the variables you can delete a value:
```python
datapath.delete_variable("coin")
```

## Transitions

This is the angular stone of the FSMD this will tell you how and where are you going to transition from one state to another.

In order to make a transition you'll need to specify the state you are going to be in, after that the state in which you want to transition, the function that will make the logic of the transition and finally a transformation function that can convert the datapath values in to something different before entering a new state, this last one is not often used, but can be useful in certain moments.

You can create a transition function with a simple  function that receives a datapath in order to read the variables and decide if it need to make the transition, if does not need to transition it should return False, else it should return True:

```python
def when_pushed(dp):
    if dp.get_variable("push"):
        return True
    return False
```
In sithe this function should not be any infinite loops, the automaton reads this function every certain time and will be encharged to make the transition when True is returned.

Then you can create a transition to a trasition table in this wahy:
```python
from Machinary.automaton import Delta

state_table = Delta()

state_table.add_transition(
    locked,
    locked,
    when_pushed,
    None
)
```

## The FSMD

finally you can create the FSMD object to run the desired behavior, you'll need to make a set of your states and pas to it that set, the datapath, a state table and finally the starting State.

```python
from Machinary.automaton import FSMD

states = (
    locked,
    unlocked
)

fmsd = FSMD(states, datapath, state_table, locked)
fmsd.run()
```
