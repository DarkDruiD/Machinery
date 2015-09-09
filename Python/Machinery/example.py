import time
import random

from datapath import Datapath

from controller import Delta
from controller import State
from controller import FSMD

def locked_on_enter():
    print "Entered locked state"
    time.sleep(3)

def locked_on_leave():
    pass

locked = State("locked")
locked.on_enter = locked_on_enter
locked.on_leave = locked_on_leave


def unlocked_on_enter():
    print "Entered unlocked state"
    time.sleep(3)

def unlocked_on_leave():
    pass

unlocked = State("unlocked")
unlocked.on_enter = unlocked_on_enter
unlocked.on_leave = unlocked_on_leave


datapath = Datapath()


def read_coin_function():
    return random.randint(0, 1)

datapath.add_variable("coin", read_coin_function)

def read_push_function():
    return random.randint(0, 1)

datapath.add_variable("push", read_push_function)


state_table = Delta()

def when_pushed(dp):
    if dp.get_variable("push"):
        return True

    return False

state_table.add_transition(
    locked,
    locked,
    when_pushed,
    None
)

def when_coined(dp):
    if dp.get_variable("coin"):
        return True

    return False

state_table.add_transition(
    locked,
    unlocked,
    when_coined,
    None
)


state_table.add_transition(
    unlocked,
    unlocked,
    when_coined,
    None
)

state_table.add_transition(
    unlocked,
    locked,
    when_pushed,
    None
)

states = (
    locked,
    unlocked
)

fmsd = FSMD(states, datapath, state_table, locked)
fmsd.run()
