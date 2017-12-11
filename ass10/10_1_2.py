""" Patch model """ 
from matplotlib import pyplot as mpl

# Some variables here
#Gain is the same for all apps gain = 1
gain = 1
# The time it takes to move between apps comes from Fitt's Law
# All the buttons are the same size I guess
# painikkeen koko docsin esimerkissä: 135 x 105, + n.10 pikseliä välissä

time_between = 0
# this is what we want to solve
time_within = 0
# We're gonna throw some guesses and see which one comes about right
# # This is the rate
#R = gain / (time_between + time_within)
# If gain(timewithin) ≥ R, continue foragign, else look for next patch def hollings(g, time_b, time_w):
#l l = 1/time_between R = (l * gain) / (1 + l * time_w) mpl.plot(time_w, R, 'r.-')

def hollings(g, time_b, time_w):
    #l
    l = 1/time_between
    R = (l * gain) / (1 + l * time_w)
    mpl.plot(time_w, R, 'r.-')
# Idk plot sth

for i in range(1,60):
    hollings(gain, time_between, time_within + i)
    mpl.show()
# R = lg / (1+ lt_w) # R = (l * gain) / (1 + l * time_within)
# # We want to solve time within # so throw in guesses and see how that turns out
# # throwing in guesses from 1 second to 60 seconds