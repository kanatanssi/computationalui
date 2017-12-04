"""
Wraps the code from assignment 9.1
executes it
draws a plot based on the output
"""
import os
import json
from csv import reader
from subprocess import call

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

layout_mac = os.path.join(__location__, 'layout-mac')
input_txt = os.path.join(__location__, 'input/exercise-input.txt')
output_csv = os.path.join(__location__, 'output/output.csv')
original_json = os.path.join(__location__, 'layouts/original.json')

# There was some weirdness going on with the IDE and paths, so check if everything looks about right...
print "layout_mac: ", layout_mac
print "input_txt: ", input_txt
print "output_csv: ", output_csv

############################### ALTERING LAYOUTS ################################
# A - B C D  - E F  - G H I
# d1 d2 d3 d4 d5 d6
#colors = ["cyan",   "pink", "cyan", "yellow",   "cyan", "yellow",   "pink", "cyan", "yellow",
#          "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]

colors = ["pink",   "cyan", "cyan", "pink",   "cyan", "cyan",   "cyan", "cyan", "yellow",
          "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]

with open(original_json , "r") as jsonFile:
    data = json.load(jsonFile)

# change layout
for i in range(0, 15):
    data[str(i)]["color"] = colors[i]

with open("layouts/original.json", "w") as jsonFile:
    json.dump(data, jsonFile)

############################### RUN SIMULATION ################################

n_runs = 60 # This doesn't actually affect the value in the file
call([layout_mac, input_txt])

############################### DO THINGS WITH THE OUTPUT ################################

file_content = []

# Example output:                          | This is the interesting part                 | 
# bla,    f,   fa,  fn,  ua,  us, vstm, sa,| model, task, target, block, runtime, tasktime|
# 6  , 1.06, 1.53, 0.6, 0.1, 0.3,   45,  3,|     0,    0,      I,     1,    1.07, 1.07    |
# 0  ,    1,    2,   3,   4,   5,    6,  7,|     8,    9,     10,    11,      12, 13      |

# We only want to look at the first search occurence in each model the models (model = user)
# We go through each model at a time (we have 30 models initially) and find the initial search time for each letter
# Then we average the search times across all models
# If an element was discovered, we mark it as 1 here. Reset when new model.
elements = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0}

# When an element is found in a model for the first time, we add the initial search time to the sum
# The sums are then averaged across all the models
time_sums = {"A":0.0, "B":0.0, "C":0.0, "D":0.0, "E":0.0, "F":0.0, "G":0.0, "H":0.0, "I":0.0}
time_sums_averaged = {"A":0.0, "B":0.0, "C":0.0, "D":0.0, "E":0.0, "F":0.0, "G":0.0, "H":0.0, "I":0.0}

model = 0 # This is for tracking when the model changes

with open(output_csv) as f:
    reader = reader(f)
    file_content = list(reader)

# Remove first line from the list (it's not data)
file_content.pop(0)

for line in file_content:
    # If model has changed, reset elements, elements discovered, update model
    if model != line[8]:
        model = line[8]
        elements = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0}
        #discovered_elements = 0
        
    # If all the elements have been discovered, we're just going to wait until the model changes
    if elements[line[10]] == 0:
        # Mark element as discovered
        elements[line[10]] = 1
        #discovered_elements += 1
        # Add search time to time_sums
        time_sums[line[10]] += float(line[13])


counting_var = 0
for key in sorted(time_sums.iterkeys()):
    #print key, " (", colors[counting_var], ") ", time_sums[key]/n_runs#, " occurences ", element_occurences[key]
    time_sums_averaged[key] = time_sums[key]/n_runs
    print key, " (", colors[counting_var], ") ", time_sums_averaged[key]
    counting_var += 1


print "summed average values: ", sum(time_sums.values())
