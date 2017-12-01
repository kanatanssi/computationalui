import random
from IPython.utils.capture import capture_output
from transitions import Machine

class NarcolepticSuperhero(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def __init__(self, name):

        # No anonymous superheroes on my watch! Every narcoleptic superhero gets
        # a name. Any name at all. SleepyMan. SlumberGirl. You get the idea.
        self.name = name

        # What have we accomplished today?
        self.kittens_rescued = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='asleep')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # At some point, every superhero must rise and shine.
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')

        # Superheroes need to keep in shape.
        self.machine.add_transition('work_out', 'hanging out', 'hungry')

        # Those calories won't replenish themselves!
        self.machine.add_transition('eat', 'hungry', 'hanging out')

        # Superheroes are always on call. ALWAYS. But they're not always
        # dressed in work-appropriate clothing.
        self.machine.add_transition('distress_call', '*', 'saving the world',
                                    after='change_into_super_secret_costume')

        # When they get off work, they're all sweaty and disgusting. But before
        # they do anything else, they have to meticulously log their latest
        # escapades. Because the legal department says so.
        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty',
                                    after='update_journal')

        # Sweat is a disorder that can be remedied with water.
        # Unless you've had a particularly long day, in which case... bed time!
        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')

        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        self.machine.add_transition('nap', '*', 'asleep')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        """ Print a thing """
        print "Beauty, eh?"

####################### SECOND FSM HERE! ############################
class WaterTap(object):

    # Define some states
    states = ['cold water', 'hot water', 'no water', 'lukewarm water']

    def __init__(self, name):

        # Superheroes get a name, why not water taps too?
        self.name = name

        # Initialize the state machine
        self.machine = Machine(model=self, states=WaterTap.states, initial='no water')

        # Run some hot water
        self.machine.add_transition('hot', 'no water', 'hot water', after='water_status')
        # Run some cold water
        self.machine.add_transition('cold', 'no water', 'cold water', after='water_status')
        # Run some mixed temperature water
        self.machine.add_transition('both', 'no water', 'lukewarm water', after='water_status')
        # Don't run any water
        self.machine.add_transition('stop', 'hot water', 'no water', after='water_status')
        self.machine.add_transition('stop', 'cold water', 'no water', after='water_status')
        self.machine.add_transition('stop', 'lukewarm water', 'no water', after='water_status')
        # Change water temperature
        self.machine.add_transition('hot', 'cold water', 'hot water', after='water_status')
        self.machine.add_transition('hot', 'lukewarm water', 'hot water', after='water_status')
        self.machine.add_transition('cold', 'hot water', 'cold water', after='water_status')
        self.machine.add_transition('cold', 'lukewarm water', 'cold water', after='water_status')
        self.machine.add_transition('both', 'cold water', 'lukewarm water', after='water_status')
        self.machine.add_transition('both', 'hot water', 'lukewarm water', after='water_status')
        
    def water_status(self):
        """ Print a thing """
        print "Now running: ", self.state

####################### TESTS HERE! ############################

def fsm_test(machine):
    """
    This function just calls the two functions below it
    and prints their resuls
    """
    print "############################################"
    print "###### Testing machine for deadlocks: ######"
    print "############################################"
    property_exists, latest_state = fsm_testDeadlock(machine)
    if property_exists:
        print property_exists, ", property holds. No deadlocks"
    else:
        print property_exists, ", property does not hold. Latest state tested: ", latest_state

    print "###########################################"
    print "###### Testing machine for feedback: ######"
    print "###########################################"
    property_exists, latest_state = fsm_testFeedback(machine)
    if property_exists:
        print property_exists, ", property holds. Every transition gives feedback"
    else:
        print property_exists, ", property does not hold. Latest state tested: ", latest_state

####################### DEADLOCK TEST HERE! ############################

def fsm_testDeadlock(machine):
    """
    Tests machine for deadlocks
    """
    # We return these two in the end
    property_exists = False
    latest_state = machine.state

    # Go through each state and get triggers
    # If no non-default triggers are available
    # return with False and latest_state
    # (That means there's no actions available == deadlock)

    for state in machine.states:
        latest_state = state
        print "Current state: ", state
        for trigger in machine.machine.get_triggers(state):
        # If no: a non-default trigger exists, no deadlock, move on to next state
        # filter out triggers with names "to_..." (since automatically generated ones are to_<state>)
            if trigger[:3] != "to_":
                print "Trigger: ", trigger
                property_exists = True
                break
        # If state has no non-default triggers, deadlock exists.
        # return false and latest_state
        # no need to iterate the rest of the states
        if not property_exists:
            return property_exists, latest_state
    return property_exists, latest_state

####################### FEEDBACK TEST HERE! ############################

# Tests machine for continuous feedback
def fsm_testFeedback(machine):
    """
    Tests machine for feedback
    In practice this means that each trigger (==transition)
    is tested for feedback in the form of printing
    if nothing is printed, then it is assumed the user also gets no feedback
    (unless the user has some other, unexpected way of sensing feedback
    like a brain-computer interface)
    """
    property_exists = True
    latest_state = machine.state

    # Go to each state, test each trigger and capture output.
    ## if no feedback is given, then the property does not hold :(

    for state in machine.states:
        latest_state = state
        print "Current state: ", state
        
        for trigger in machine.machine.get_triggers(state):
        # filter out triggers with names "to_..." (since automatically generated ones are to_<state>)
        # because we don't need to test for the automatically generated triggers imo
            if trigger[:3] != "to_":
                #print "Trigger: ", trigger
                exe_str = 'machine.'+trigger+'()'
                #print exe_str

                # This is where we capture the print from stdout
                with capture_output() as c:
                    exec exe_str
                c()
                if c.stdout == "":
                    property_exists = False
                    break
        # If no feedback is given
        # return false and latest_state
        # no need to iterate the rest of the states
        if not property_exists:
            return property_exists, latest_state
    return property_exists, latest_state

####################### UNIMPLEMENTED CONSISTENCY TEST HERE! ############################

# Tests machine for consistency
#def fsm_testConsistency(machine):
    """
    Tests machine for consistency
    """
#    property_exists = False
#    latest_state = machine.state

    # Go to each state, test each trigger for it's output state.
    ## if the state differs over the original result in the tests
    ## then the trigger is not consistent
    ### return false and latest state (the one that was being tested)

#    for state in superhero.states:
#        latest_state = state
#        print "Current state: ", state
#        for trigger in machine.machine.get_triggers(state):
        # If no: a non-default trigger exists, no deadlock, move on to next state
        # filter out triggers with names "to_..." (since automatically generated ones are to_<state>)
#            if trigger[:3] != "to_":
#                print "Trigger: ", trigger
#                property_exists = True
#                break
        # If state has no non-default triggers, deadlock exists.
        # return false and latest_state
        # no need to iterate the rest of the states
#        if not property_exists:
#            return property_exists, latest_state
#    return property_exists, latest_state


####################### MAIN HERE! ############################

# Create superheromachine
superhero = NarcolepticSuperhero("FiniteStateMan")
# Create WaterTap
watertap = WaterTap("WaterTap")

print watertap.state
print watertap.states
watertap.cold()
print watertap.state

exe_str = 'watertap.'+'hot'+'()'
print exe_str
with capture_output() as c:
    exec exe_str
c()
if c.stdout == "":
    print "no feedback"
else:
    print c.stdout

fsm_test(superhero)
fsm_test(watertap)