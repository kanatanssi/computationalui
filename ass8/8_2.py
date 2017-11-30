"""Tests if a given state exists in a Finite State Machine
- fsm created with Python Transitions
- tests for
"""
#from transitions import Machine
import NarcolepticSuperhero as ns

#MACHINE = Machine(states=STATES, transitions=TRANSITIONS, initial='blah')
MACHINE = ns.NarcolepticSuperhero("FiniteStateMan")

# Each interaction property is a set or rules that will be tested in fsm_test
#INTERACTION_PROPERTY

#INTERACTION_PROPERTIES = []

#for int_property in INTERACTION_PROPERTIES:
#    property_exists, latest_state = fsm_test(MACHINE, int_property)
#    if property_exists:
#        print property_exists
#    else: print property_exists, ", Latest state: ", latest_state

print "Testing machine for deadlocks:"
property_exists, latest_state = fsm_testDeadlock(MACHINE)
if property_exists:
    print property_exists, ", property holds. No deadlocks"
else:
    print property_exists, ", property does not hold. Latest state tested: ", latest_state

print "Testing machine for consistency:"
property_exists, latest_state = fsm_testConsistency(MACHINE)
if property_exists:
    print property_exists, ", property holds. No inconsistent triggers"
else:
    print property_exists, ", property does not hold. Latest state tested: ", latest_state

"""
Tests if given interaction property exists in given fsm
Uses exhaustive search
"""
def fsm_testDeadlock(machine):
    # We return these two in the end
    property_exists = False
    latest_state = machine.state

    # Go through the machine until each state has been reached at least once
    # If no triggers are available at given state, return with False and latest_state
    # machine.state to get current state
    # machine.get_triggers to get triggers at current state
    # machine.to_(state) to go to specific state, allows us to reverse

    # Actually, test each state and see if it has any triggers.
    ## if not, return with False and the latest state

    for state in machine.states
    


    return property_exists, latest_state

def fsm_testConsistency(machine):
    property_exists = False
    latest_state = machine.state

    # Go to each state, test each trigger for it's output state.
    ## if the state differs over the original result in the tests
    ## then the trigger is not consistent
    ### return false and latest state (the one that was being tested)

    return property_exists, latest_state
