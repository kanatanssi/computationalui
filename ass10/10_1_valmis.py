"""
Patch model
"""
from matplotlib import pyplot as mpl
datapoints = 100

# Some variables here
# Gain is the same for all apps
gain = 1.0

# The time it takes to move between apps comes from Fitt's Law
# All the buttons are the same size I guess
#time_between = 0.5
time_between = 2.0
time_between2 = 5.0
time_between3 = 10.0

# this is what we want to solve
time_within = 1.0
# We're gonna throw some guesses and see which one comes about right

# This is the rate
#R = gain / (time_between + time_within)
# If gain(timewithin) > R, continue foragign, else look for next patch

def hollings(g, time_b, time_w):
    #l
    l = 1/time_b
    R = (l * gain) / (1 + l * time_w)
    #mpl.plot(time_w, R, 'r-')
    #mpl.plot(R, time_w, 'r.')
    return R

def hollingscurve(g, time_b, time_w):
    curve = []
    accumulatedgain = 0
    for i in range(0, datapoints-1):
        accumulatedgain += hollings(g, time_b, time_w + i)
        curve.append(accumulatedgain)
    return curve


#mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between, time_within), 'r-')
#mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between2, time_within), 'b-')
#mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between3, time_within), 'g-')

punainen, = mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between, time_within), 'r-', label='T_b: '+str(time_between))
sininen, = mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between2, time_within), 'b-', label='T_b: '+str(time_between2))
vihrea, = mpl.plot(range(0, datapoints-1), hollingscurve(gain, time_between3, time_within), 'g-', label='T_b: '+str(time_between3))

mpl.legend(handles=[punainen, sininen, vihrea])

#line_up, = plt.plot([1,2,3], label='Line 2')
#line_down, = plt.plot([3,2,1], label='Line 1')
#plt.legend(handles=[line_up, line_down])

mpl.xlabel("time within")
mpl.ylabel("Accumulated gains")
mpl.show()

# R = lg / (1+ lt_w)
# R = (l * gain) / (1 + l * time_within)
# We want to solve time within
# so throw in guesses and see how that turns out
# throwing in guesses from 1 second to 60 seconds
