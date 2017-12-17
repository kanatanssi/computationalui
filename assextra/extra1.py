"""
Model and visualize the location of the three most common elements of the webpages
Normalize locations x/y to a range of [0..1] (element location / total h or total w)
Find 3 most common elements
Plot the locations of these elements
x axis [0..1]
y axis [0..1]
"""
import os
import json
import glob
import operator
import numpy as np
from matplotlib import pyplot as mpl
import matplotlib.ticker as ticker

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

ws_path = os.path.join(__location__, "Extra-assignment-web-pages/ShoppingSites/") #'/Extra-assignment-web-pages/Shopping Sites')

elements_popularity = {}
all_the_vars = []

# Read through json file, look for most common elements.
# ie. count each element and we'll get which ones are the most common
# Implement here
def readData(f_name, element_count, save_everything):
    data = json.load(open(f_name))

    for element in data["elements"]:
        # For the sake of readability. This is the feature field (ex. "Social") in the element
        elem = data["elements"][element]

        # Get the sizes of element 0, that one describes the canvas size.
        zero_width = float(data["elements"]["0"]["width"])
        zero_height = float(data["elements"]["0"]["height"])
        
        # add to the count of this element
        # (the second parameter of get sets a default value if entry doesn't exist in the dictionary)
        if (elem != "0"):
            element_count[elem["feature"]] = element_count.get(elem["feature"], 0) + 1
        
        # record name, position and sizes of feature, normalized against the feature 0
            save_everything.append([elem["feature"],(elem["xPosition"]/zero_width),1-(elem["yPosition"]/zero_height),1-(elem["height"]/zero_height),1-(elem["width"]/zero_width)])

# Simply plot?

# Then do the probability thing?
# Count each feature and their probability (count / 30)
# Average the position and size of features
# Generate image where appropriate rectangles have been placed
# (based on average locations and sizes)
# Maybe for position use probability and for size use average in bins (eg. 30% of canvas size, 50%... etc)

######################################## MAIN HERE ########################################

# get the most popular elements, their positions and size
for filename in glob.glob(ws_path + "*.json"):
    readData(filename, elements_popularity, all_the_vars)

# Don't need "none", it's just the canvas
del elements_popularity["none"]

# Change here for 3-4 most popular
three_most_pop = list(dict(sorted(elements_popularity.iteritems(), key=operator.itemgetter(1), reverse=True)[:3]))

plots = range(0,3) # could also be 4
counting_var = 0
colors = ['r', 'b', 'y', 'g']
markers = ['^', '*', '.', 'x']
# List of dictionaries, one for each of the most popular models
occurences = [{},{},{}] #You might want to adjust size here too

#for mp in three_most_pop:
#    for atv in all_the_vars:
#        if atv[0] == mp:
#            round_pos = (str(format(atv[1], '.1f'))+","+str(format(atv[2], '.1f')))
#            occurences[counting_var][round_pos] = occurences[counting_var].get(round_pos, 0) + 1

# For each of the 3 most popular elements, get the positions (and average size of elements)
for mp in three_most_pop:
    x = []
    y = []
    for atv in all_the_vars:
        if atv[0] == mp:
            #print str(atv[1]) + " [1] ja [2] " + str(atv[2]) + " " + colors[counting_var] + " " + mp
            #x.append(atv[1])
            #y.append(atv[2])
            # Get the probabilty here
            # Round position to nearest full decimal (0.n)
            # Save decimal as key and number of hits as value
            
            # Example of adding value to dict when key might not exist
            #element_count[elem["feature"]] = element_count.get(elem["feature"], 0) + 1
            
            # so key is a string of both x and y rounded to the nearest 0.n, value is nr of hits
            #probabilies[counting_var] = [str(format(atv[1], '.1f'))+","+str(format(atv[2], '.1f'))]
            round_pos = (str(format(atv[1], '.1f'))+","+str(format(atv[2], '.1f')))
            occurences[counting_var][round_pos] = occurences[counting_var].get(round_pos, 0) + 1
            probability = occurences[counting_var][round_pos]/30.0
            plots[counting_var] = mpl.scatter(atv[1], atv[2], c=colors[counting_var], s=10000*probability, label=mp, alpha=probability*0.5, edgecolors='none')
    #plots[counting_var] = mpl.scatter(x, y, c=colors[counting_var], s=50, label=mp, alpha=0.3, edgecolors='none')
    
    counting_var += 1
# For correct drawing of the legend
plots[0] = mpl.scatter(0, 0, c=colors[0], s=10, label=three_most_pop[0], alpha=1, edgecolors='none')
plots[1] = mpl.scatter(0, 0, c=colors[1], s=10, label=three_most_pop[1], alpha=1, edgecolors='none')
plots[2] = mpl.scatter(0, 0, c=colors[2], s=10, label=three_most_pop[2], alpha=1, edgecolors='none')
# Cover that dot up
mpl.scatter(0, 0, c='white', s=11, alpha=1, edgecolors='none')

print occurences[0]
mpl.legend(handles=[plots[0], plots[1], plots[2]], loc="best") # add plots[3] for 4th one
mpl.xticks(np.arange(0, 1, 0.1))
mpl.yticks(np.arange(0, 1, 0.1))
mpl.show()


# Divide 0..1 to increments of 3? 5? 10?
# track where does an element fall (normalized loc vs. increment)
# simple probability is times hit / times could've hit

# Iterate over increments 0.1 at a time
# If normalized value of element is smaller than increment, it falls within this increment
# Increment hit ++ for element n

# get element
# get element's position
# get probability of the element being in that position
# use that for alpha :) (bigger probability = more visible dot)

# increment hit / total number for scalar?