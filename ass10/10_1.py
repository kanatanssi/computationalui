"""
Patch model
"""
from matplotlib import pyplot as mpl
datapoints = 100

# Some variables here
# Gain is the same for all apps
element_gain = 1.0

# This affects the slope of the curve - the longer the time between patches, the lower one's expected gains
time_between = 2.0
time_between2 = 5.0
time_between3 = 10.0

# We're gonna throw some guesses with time within and see which one comes about right
time_within = 1.0


# This is the rate
#R = gain / (time_between + time_within)
# If gain(timewithin) > R, continue foragign, else look for next patch

# 
def gainfunction(g, time_b, time_w):
    #l
    l = 1/time_b
    # From lecture slides
    R = (l * element_gain) / (1 + l * time_w)
    return R

# Makes a list of the gainfunction, for nicer plotting.
def gaincurve(g, time_b, time_w):
    curve = []
    accumulatedgain = 0
    for i in range(0, datapoints-1):
        accumulatedgain += gainfunction(g, time_b, time_w + i)
        curve.append(accumulatedgain)
    return curve

punainen, = mpl.plot(range(0, datapoints-1), gaincurve(element_gain, time_between, time_within), 'r-', label='T_b: '+str(time_between))
sininen, = mpl.plot(range(0, datapoints-1), gaincurve(element_gain, time_between2, time_within), 'b-', label='T_b: '+str(time_between2))
vihrea, = mpl.plot(range(0, datapoints-1), gaincurve(element_gain, time_between3, time_within), 'g-', label='T_b: '+str(time_between3))

mpl.legend(handles=[punainen, sininen, vihrea])

mpl.xlabel("time within")
mpl.ylabel("Accumulated gains")
mpl.show()
