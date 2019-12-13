# Script to control and animate hue lights using Indigo Domotics and Hue Lights plugin from Nathan Sheldon Software
# Uses matplotlib library of X11 color names (https://matplotlib.org/examples/color/named_colors.html)
# Color names list sorted by hue (https://en.wikipedia.org/wiki/Web_colors)
# This script demonstrates how to create lists for hue lights using list comprehension algorithms

#IMPORTS
import time
import random
from matplotlib import colors 
import colorsys
import re
import color_animation_utils as cau

#TITLE FOR SCRIPT
title_program = "Xmas 1.0 - 2019 Animations with List Comprehensions"

#TIME - INITIALIZATIONS
start_time = time.time()

#TIME - Define Initial Minutes for while loop
minutes_for_while_loop = 2
time_end_loop = time.time() + 60 * minutes_for_while_loop

#COLOR NAME DICTIONARY
color_name_dict = colors.cnames

#COLOR LISTS

#COLOR LIST INITIAL SELECTION
color_list_initial  = list(cau.color_list_rgb_secondary)
color_list_i = list(color_list_initial)

#BULB LISTS


#BULB LIST INITIAL SELECTIONS	
#bulb_list_initial = list(cau.bulb_list_office_R2L_6)
bulb_list_initial = list(cau.bulb_list_ls_out_holiday)
bulb_list = list(bulb_list_initial)

#The Number of Color Names needs to be greater than the Number of Bulbs
#if len(color_list_i) < len(bulb_list):
#	color_list_i = (color_list_i * len(bulb_list))[slice(0,len(bulb_list))]


#RAMP RATE LISTS
ramp_list_6 = [
	1,
	2,
	3,
	4,
	5,
	6,
	]	
	
ramp_list_3 = [
	1,
	2,
	3,
	]	

ramp_list_initial = list(ramp_list_6)
ramp_list = ramp_list_initial

#FUNCTIONS - PRINT
def print_time_stamp():
	#print time stamp in preferred format
	indigo.server.log("Time Stamp: " + time.strftime('%Y-%m-%d %I:%M:%S %p'))

def print_start_elapsed_time(title_routine_set):
	#print time stamp and start time for a routine
	start_time_temp = time.time()
	indigo.server.log("ROUTINE - " + title_routine_set)
	indigo.server.log("START Time Routine:")
	print_time_stamp() 

def print_stop_elapsed_time(title_routine_set):
	#print time stamp and stop time and elapsed time for a routine
	elapsed_time_temp = time.time() - start_time_temp
	indigo.server.log("STOP Time ROUTINE - " + title_routine_set)
	print_time_stamp()
	indigo.server.log("ELAPSED Time ROUTINE - " + title_routine_set + " - " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time_temp)))

def print_delay_total ():
	indigo.server.log("DELAY Total = " + str(delay_total) + ", with Ramp Rate: " + str(ramp_rate) + " + Delay Margin: " + str(delay_margin))

#FUNCTIONS
#Set Bulbs		
def set_bulb_color_rgb (color_value, bulb_id, ramp_rate = 1):
	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
	if plug.isEnabled():
		#color_value_rgb is a list containing [r,g,b], e.g. red is [255,0,0]
		r = color_value[0]
		g = color_value[1]
		b = color_value[2]
		#indigo.server.log("Hex R,G,B - " + str(r) + ", " +str(g) + ", " +str(b))
		plug.executeAction("setRGB", bulb_id, props={"red": r, "green": g, "blue": b, "rate": ramp_rate})

#convert color list to [r,g,b] values with Error checking		
def convert_color_list_to_rgb(color_list):
	#Color List Initial Print
	indigo.server.log("---------------------------------------------------------")
	indigo.server.log("Color List Error Checking and Conversion to [R,G,B] Color List for: " + title_routine_set)
	indigo.server.log("color_list - Initial = " + str(color_list))
	#Color Name Conversion to Lower Case and Print
	color_list = [x if isinstance(x,list) else x.lower() for x in color_list]
	indigo.server.log("---------------------------------------------------------")
	indigo.server.log("color_list - Names Converted to Lower() = " + str(color_list))
	indigo.server.log("---------------------------------------------------------")	
	for color_name in color_list:
		if str(color_name).lower() in color_name_dict.keys():
			indigo.server.log("Color Value = '" + str(color_name) + "' - Found in dictionary with Value: " +str(color_name_dict[color_name]))
		else:
			indigo.server.log("Color Value = '" + str(color_name) + "' - NOT found in dictionary")
	color_list = [x if isinstance(x,list) else color_name_dict.get(x,x) for x in color_list]
	indigo.server.log("---------------------------------------------------------")
	indigo.server.log("color_list - Valid color names converted to hex = " + str(color_list))
	indigo.server.log("---------------------------------------------------------")
	for color_value in color_list:
		#if color_value is a valid hex value with regexp match(like #00FF00), convert HEX value to [r,g,b] values.
		#https://stackoverflow.com/questions/1636350/how-to-identify-a-given-string-is-hex-color-format 
		if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str(color_value)):		
			color_value = color_value.lstrip("#")
			r, g, b = (int(color_value[i:i+2], 16) for i in (0,2,4))
			color_value_rgb = [r,g,b]
			indigo.server.log("Color Value = '#" + str(color_value) + "' - valid hex, [r,g,b] = " + str(color_value_rgb))
			color_list_rgb.append(color_value_rgb)
		elif isinstance(color_value, list) and len(color_value) == 3 and all(0 <= x <= 255 for x in color_value):
			#if color_value is a list with 3 [r,g,b] values, and each value is between 0 and 255, pass it through
			indigo.server.log("Color Value = is already valid [r,g,b]: " + str(color_value))
			color_list_rgb.append(color_value)			
		else:			
			indigo.server.log("Color Value = '" + str(color_value) + "' *ERROR* NOT found in color name dictionary, or is invalid")
	return color_list_rgb
					
#PRINT INITIAL VARIABLE VALUES
indigo.server.log("======================= P R O G R A M   ======================")
indigo.server.log("START Time for PROGRAM - " + title_program)
indigo.server.log("Time Stamp - " + time.strftime('%Y-%m-%d %I:%M:%S %p',time.localtime(start_time)))
indigo.server.log("--------------------------------------------------------------")
indigo.server.log("INITIAL VARIABLE VALUES:")

color_name_dict_length = len(color_name_dict)
indigo.server.log("Number of Colors in matplotlib - " + str(color_name_dict_length))

#COLOR NAME DICTIONARY - PRINT ALPHABETICALLY
#for x in sorted(color_name_dict):
#	indigo.server.log(str(x) + ", " + str(color_name_dict[x]))	

indigo.server.log("color_list_initial = " + str(color_list_initial))
color_list_initial_length = len(color_list_initial)
indigo.server.log("color_list_initial_length = " + str(color_list_initial_length))

indigo.server.log("color_list_i = " + str(color_list_i))
color_list_total = len(color_list_i)
indigo.server.log("color_list_total = " + str(color_list_total))

indigo.server.log("bulb_list = " + str(bulb_list))
bulb_list_total = len(bulb_list)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))

indigo.server.log("ramp_list = " + str(ramp_list))
ramp_list_length = len(ramp_list)
indigo.server.log("ramp_list_length = " + str(ramp_list_length))

indigo.server.log("MINUTES for While Loop: " + str(minutes_for_while_loop) + " minutes")

indigo.server.log("--------------------------------------------------------------")

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> color_list_sequence_all_0: [0] * bulb_list_total"
#i = 0
color_list_sequence_all_0 = [0] * bulb_list_total
indigo.server.log(routine)
#indigo.server.log("i = " + str(i))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_all_0 = " + str(color_list_sequence_all_0))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> color_list_sequence_all_2: [2] * bulb_list_total"
#i = 0
color_list_sequence_all_2 = [[2] * bulb_list_total]
indigo.server.log(routine)
#indigo.server.log("i = " + str(i))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_all_2 = " + str(color_list_sequence_all_2))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> color_list_sequence_all_i_eval: [i] * bulb_list_total"
#i = 0
def color_list_sequence_all_i_eval (i):	
	return [[i] * bulb_list_total]
i = 3
color_list_sequence_all_i_eval = color_list_sequence_all_i_eval (i)
indigo.server.log(routine)
indigo.server.log("i = " + str(i))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_all_i_eval = " + str(color_list_sequence_all_i_eval))


# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_all_0_to_i: [[i] * bulb_list_total for i in range(bulb_list_total)]"
#i = 0
color_list_sequence_all_0_to_i = [[i] * bulb_list_total for i in range(color_list_total)]
indigo.server.log(routine)
#indigo.server.log("i = " + str(i))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_all_0_to_i = " + str(color_list_sequence_all_0_to_i))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_all_i_to_0: [[i] * bulb_list_total for i in range(bulb_list_total)]"
#i = 0
color_list_sequence_all_i_to_0 = [[i] * bulb_list_total  for i in range(color_list_total)][::-1]
indigo.server.log(routine)
#indigo.server.log("i = " + str(i))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_all_i_to_0 = " + str(color_list_sequence_all_i_to_0))


# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_range_0_to_i: range(bulb_list_total)"
color_list_sequence_range_0_to_i = [list(range(bulb_list_total))]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_range_0_to_i = " + str(color_list_sequence_range_0_to_i))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_range_i_to_0: list(reversed(range(bulb_list_total)))"
color_list_sequence_range_i_to_0 = [list(reversed(range(bulb_list_total)))]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_range_i_to_0 = " + str(color_list_sequence_range_i_to_0))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> random.sample() - initialize k random samples for move sequences"
sample_number = 2
color_list_sample = random.sample(range(bulb_list_total),k = sample_number)
indigo.server.log(routine)
c1 = color_list_sample[0]
c2 = color_list_sample[1]
indigo.server.log("sample_number = " + str(sample_number))
indigo.server.log("c1 = " + str(c1))
indigo.server.log("c2 = " + str(c2))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_move_0_to_i: range(bulb_list_total)"
color_list_sequence_move_0_to_i = [[ c1 if i == j else c2 for j in range(bulb_list_total)] for i in range(bulb_list_total)]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_move_0_to_i = " + str(color_list_sequence_move_0_to_i))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_move_i_to_0: range(bulb_list_total)"
color_list_sequence_move_i_to_0 = [[ c1 if i == j else c2 for j in range(bulb_list_total)] for i in range(bulb_list_total)][::-1]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_move_i_to_0 = " + str(color_list_sequence_move_i_to_0))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_move_fill_0_to_i: range(bulb_list_total)"
color_list_sequence_move_fill_0_to_i = [[ c1 if i > j else c2 for j in range(bulb_list_total)] for i in range(bulb_list_total + 1)]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_move_fill_0_to_i = " + str(color_list_sequence_move_fill_0_to_i))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> List Comprehension - color_list_sequence_move_fill_i_to_0: range(bulb_list_total)"
color_list_sequence_move_fill_i_to_0 = [[ c1 if i > j else c2 for j in range(bulb_list_total)] for i in range(bulb_list_total)][::-1]
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_sequence_move_fill_i_to_0 = " + str(color_list_sequence_move_fill_i_to_0))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> [[ix, color_list_i.index(ix)] for ix in color_list_i]"
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_i = " + str(color_list_i))
indigo.server.log("color_list_total = " + str(len(color_list_i)))
indigo.server.log(str([[ix, color_list_i.index(ix)] for ix in color_list_i]))

# ---> ROUTINE BEGIN ######################################################

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Color List Index: [color_list_sequence_range_0_to_i] * 4"
color_list_index = [color_list_sequence_range_0_to_i] * 4
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index = " + str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Color List Index: Multiple Lists"
color_list_index_nested = (
	[[0] * bulb_list_total]
	+ [[5] * bulb_list_total]
	+ [[3] * bulb_list_total]
	+ [range(bulb_list_total)]
	+ [range(0,bulb_list_total,2)]
	+ [list(reversed(range(bulb_list_total)))]
	+ [([0,1] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [([1,0] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [([1,1,0,0] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [([0,0,1,1] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [([1,1,1,0,0,0] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [([0,0,0,1,1,1] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ [[ 1 if i == j else 0 for j in range(bulb_list_total)] for i in range(bulb_list_total)]
	+ [[ 1 if i == j else 0 for j in range(bulb_list_total)] for i in range(bulb_list_total)][::-1]
	+ [[ 1 if i > j else 0 for j in range(bulb_list_total)] for i in range(bulb_list_total + 1)]
	+ [[ 1 if i > j else 0 for j in range(bulb_list_total)] for i in range(bulb_list_total)][::-1]
	+ [[i] * bulb_list_total  for i in range(color_list_total)]
	+ [[i] * bulb_list_total  for i in range(color_list_total)][::-1]
	)	

indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index_nested = " + str(color_list_index_nested))
for i in color_list_index_nested:
	indigo.server.log(str(color_list_index_nested.index(i)) + ": " + str(i))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Color List Index: range(bulb_list_total - 1, -1, -1)"
color_list_index = range(bulb_list_total - 1, -1, -1)
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index = " + str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Color List Index: [i for i in reversed(range(bulb_list_total))]"
color_list_index = [i for i in reversed(range(bulb_list_total))]	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index = " + str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Color List Index: color_list_index[::-1]"	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index[::-1] = " + str(color_list_index[::-1]))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Random Shuffle Color List Index: random.shuffle(color_list_index)"
random.shuffle(color_list_index)	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index = " + str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Random Shuffle Color List Index: random.shuffle(color_list_index)"
random.shuffle(color_list_index)	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("color_list_index = " + str([color_list_index] * 3))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Color List Index of [x,y] Repeating for len(bulb_list)"
x = 0
y = 1
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log("Modulus = " + str(bulb_list_total % len(color_list_index)))
color_list_index = color_list_index * (bulb_list_total/len(color_list_index)) + [color_list_index[0]]* (bulb_list_total % len(color_list_index))
indigo.server.log("color_list_index = " + str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Color List Index:[item for item in x for i in range(n)])"
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))

color_list_index = ([0,1] * bulb_list_total)[slice(0,bulb_list_total)]
indigo.server.log("color_list_index = " + str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Chase Color List Index of [x,y] for len(bulb_list)"
x = 0
y = 1
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
color_list_index = [[ y if i == j else x for j in range(bulb_list_total)] for i in range(bulb_list_total)]
indigo.server.log(str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Nested Chase Color List Index of [x,y] for len(bulb_list)"	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log(str(color_list_index[::-1]))
for i in color_list_index[::-1]:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Chase Fill Color List Index of [x,y] for len(bulb_list)"
x = 0
y = 1
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
color_list_index = [ [ y if i >= j else x for j in range(bulb_list_total)] for i in range(bulb_list_total)]
indigo.server.log(str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Nested Chase Fill Color List Index of [x,y] for len(bulb_list)"	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log(str(color_list_index[::-1]))
for i in color_list_index[::-1]:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Chase Fill Color List Index of [x,y] for len(bulb_list) - Start with All [0]"
x = 0
y = 1
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
color_list_index = [[ y if i > j else x for j in range(bulb_list_total)] for i in range(bulb_list_total + 1)]
indigo.server.log(str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Nested Chase Fill Color List Index of [x,y] for len(bulb_list) - Start with All [0][::-1]"
x = 0
y = 1
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
color_list_index = [[ y if i > j else x for j in range(bulb_list_total)] for i in range(bulb_list_total)][::-1]
indigo.server.log(str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Nested Chase Fill Color List Index of [x,y] for len(bulb_list)"	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log(str(color_list_index[::-1]))
for i in color_list_index[::-1]:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Nested Loop Color List Index for len(color_list_index)"

color_list_index = [i] * bulb_list_total
color_list_index = [x,y]
indigo.server.log(routine)
indigo.server.log("x = " + str(x))
indigo.server.log("y = " + str(y))
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
color_list_index = [[i] * bulb_list_total  for i in range(color_list_total)]
indigo.server.log(str(color_list_index))
for i in color_list_index:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
	
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Nested Color Loop for len(color_list_index)"	
indigo.server.log(routine)
indigo.server.log("bulb_list_total = " + str(bulb_list_total))
indigo.server.log(str(color_list_index[::-1]))
for i in color_list_index[::-1]:
	indigo.server.log(str(color_list_index.index(i)) + ": " + str(i))
		
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Map of color_list_index,bulb_list,ramp_list"
indigo.server.log(routine)
indigo.server.log("color_list_index = " + str(color_list_index))
indigo.server.log("color_list_total = " + str(color_list_total))

indigo.server.log("Bulb List = " + str(bulb_list))
indigo.server.log("Bulb List Length = " + str(bulb_list_total))

indigo.server.log("bulb_list = " + str(ramp_list))
indigo.server.log("ramp_list_length = " + str(ramp_list_length))

min_length = min(color_list_total,bulb_list_total,ramp_list_length)
indigo.server.log("min_length = " + str(min_length))


for c,b,r in zip(color_list_index,bulb_list,ramp_list):
	indigo.server.log("color_list_index = " + str(c) + ", " + "bulb_list = " + str(b) + ", ramp_list = " + str(r))
indigo.server.log(str(map(None,color_list_index,bulb_list,ramp_list)))	

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Create List from 0 to i for Length of Color List Index"
color_list_index = [i for i in range(color_list_total)]	
indigo.server.log(routine)
indigo.server.log("color_list_total = " + str(color_list_total))
indigo.server.log(str(color_list_index))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Reverse Color List Index"	
indigo.server.log(routine)
indigo.server.log("color_list_total = " + str(color_list_total))
indigo.server.log(str(color_list_index[::-1]))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Sorted Color List Index"	
indigo.server.log(routine)
color_list_i = list(color_list_initial)
indigo.server.log("color_list_i = " + str(color_list_i))
indigo.server.log("color_list_total = " + str(color_list_total))
indigo.server.log(str(sorted(color_list_i, key=str.lower)))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Sorted Alphabetically Color List from Dictionary for x Substring (eg 'red', or 'light')"	
indigo.server.log(routine)
#for x in sorted(color_name_dict):
#	indigo.server.log(str(x) + ", " + str(color_name_dict[x]))
filter_str = "dark"
#filtered_dict = list(filter(lambda item: filter_str in item[0], color_name_dict.keys()))
#indigo.server.log(str(filtered_dict))
filtered_dict = [k for k in sorted(color_name_dict.iterkeys()) if filter_str in k]
indigo.server.log(str(filtered_dict))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Sorted by HSV Color List from Dictionary for x Substring (eg 'red', or 'light')"
indigo.server.log(routine)	
filter_str = "blue"
filtered_dict = [k for k in sorted(color_name_dict.iterkeys()) if filter_str in k]
for color_name in filtered_dict:
		r = int(color_name_dict[color_name.lower()][1:3],16)
		g = int(color_name_dict[color_name.lower()][3:5],16)
		b = int(color_name_dict[color_name.lower()][5:7],16)
		hue_sat_val = colorsys.rgb_to_hsv(r,g,b)
		indigo.server.log(str(color_name) + str(hue_sat_val))
		
indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Sorted by YIQ Color List from Dictionary for x Substring (eg 'red', or 'light')"
indigo.server.log(routine)	
filter_str = "red"
filtered_dict = [k for k in sorted(color_name_dict.iterkeys()) if filter_str in k]
color_list_hue = []
for color_name in filtered_dict:
	r = int(color_name_dict[color_name.lower()][1:3],16)
	g = int(color_name_dict[color_name.lower()][3:5],16)
	b = int(color_name_dict[color_name.lower()][5:7],16)
	luma_chrominance = colorsys.rgb_to_yiq(r,g,b)[0]	
	color_list_hue.append((color_name, luma_chrominance))
indigo.server.log("Sorted Alphabetically")
indigo.server.log(str(color_list_hue))
indigo.server.log("Sorted By YIQ Light to Dark")
color_list_hue = sorted(color_list_hue, reverse = True, key=lambda i: i[1])
color_list_hue = [i[0] for i in color_list_hue]
indigo.server.log("Sorted By YIQ Light to Dark - Color Name Only")
indigo.server.log(str(color_list_hue))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Hues Sorted by YIQ Color List from Dictionary for List of Substring (eg ['purple','violet'])"
indigo.server.log(routine)	
filter_str_list = ["magenta", "indigo", "violet", "Fuchsia"]
indigo.server.log(str(filter_str_list))	
indigo.server.log("Convert filter_str_list to lower()")	
filter_str_list = [x.lower() for x in filter_str_list]
indigo.server.log(str(filter_str_list))	
filtered_dict = [k for k in sorted(color_name_dict.iterkeys()) if any(c in k for c in filter_str_list)]
color_list_hue = []
for color_name in filtered_dict:
	r = int(color_name_dict[color_name.lower()][1:3],16)
	g = int(color_name_dict[color_name.lower()][3:5],16)
	b = int(color_name_dict[color_name.lower()][5:7],16)
	luma_chrominance = colorsys.rgb_to_yiq(r,g,b)[0]	
	color_list_hue.append((color_name, luma_chrominance))
indigo.server.log("Sorted Alphabetically")
indigo.server.log(str(color_list_hue))
indigo.server.log("Sorted By YIQ Light to Dark")
color_list_hue = sorted(color_list_hue, reverse = True, key=lambda i: i[1])
indigo.server.log(str(color_list_hue))
color_list_hue = [i[0] for i in color_list_hue]
indigo.server.log("Sorted By YIQ Light to Dark - Color Name Only")
indigo.server.log(str(color_list_hue))

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> matplotlib is_color_like hex validation"
indigo.server.log(routine)	
color_list_i = list(cau.color_list_rgb_secondary)
indigo.server.log("color_list_i = " + str(color_list_i))	
indigo.server.log("color_list_i.lower() = " + str(color_list_i))	
for color_name in color_list_i:
	if colors.is_color_like(color_name):
		indigo.server.log("color_name = " + str(color_name) + ": Color IS valid")
	else:
		indigo.server.log("color_name = " + str(color_name) + ": Color NOT valid")

indigo.server.log("======================= R O U T I N E =======================")
routine = "---> regular expression hex validation"
indigo.server.log(routine)	
color_list_i = list(cau.color_list_rgb_secondary)
indigo.server.log("color_list_i = " + str(color_list_i))	
indigo.server.log("color_list_i.lower() = " + str(color_list_i))	
for color_name in color_list_i:
	if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str(color_name)):
		indigo.server.log("color_name = " + str(color_name) + ": Color IS valid")
	else:
		indigo.server.log("color_name = " + str(color_name) + ": Color NOT valid")
		
i = "ffffff" # Your Hex

match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', i)
#match = re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', i)

if match:                      
  indigo.server.log("Hex IS valid for: " + str(i))	 

else:
  indigo.server.log("Hex is NOT valid for: "  + str(i))	 


indigo.server.log("======================= R O U T I N E =======================")
routine = "---> Color List Substitute Value for Name in Dict"
indigo.server.log(routine)	
#color_list_i = list(cau.color_list_rgb_secondary)
color_list_i = list(cau.color_list_rgb_secondary)
indigo.server.log("color_list_i = " + str(color_list_i))	
color_list_name_substitute = []
color_list_name_substitute = [x if isinstance(x,list) else x.lower() for x in color_list_i]
indigo.server.log("color_list_name_substitute = " + str(color_list_name_substitute))	

for color_name in color_list_name_substitute:
	if str(color_name).lower() in color_name_dict.keys():
		indigo.server.log("color_name = " + str(color_name) + " - Found in dictionary with Value: " +str(color_name_dict[color_name]))
		#color_list_name_substitute[color_name] = str(color_name_dict[color_name]))
	else:
		indigo.server.log("color_name = " + str(color_name) + ": - NOT found in dictionary")

color_list_name_substitute = [x if isinstance(x,list) else color_name_dict.get(x,x) for x in color_list_name_substitute]
indigo.server.log("color_list_name_substitute = " + str(color_list_name_substitute))

color_list_name_substitute = [x for x in color_list_name_substitute if not isinstance(x,basestring)]
indigo.server.log("color_list_name_substitute = " + str(color_list_name_substitute))

	

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Animation"

#Timing Variables
ramp_rate = 2
delay_margin = 5

#TIME - Define Minutes for while loop
minutes_for_while_loop = 300
#minutes_for_while_loop = 60
time_end_loop = time.time() + 60 * minutes_for_while_loop

#Timing Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)

#Bulb List
bulb_list = list(cau.bulb_list_ls_out_holiday)
#bulb_list = list(cau.bulb_list_office_R2L_6)

#Color List Initial
#color_list = list(color_list_initial)
#color_list = list(color_list_hex_6)
#color_list = cau.color_list_rgb_tertiary
color_list = cau.color_list_rgb_secondary
#color_list = color_list_mixed_wrong_test
#color_list = color_list_mixed_test
#color_list = color_list_hex_6
#color_list = list(color_list_halloween_test_1)

#Color Name Conversion to Hex values, and Color List Conversion to [R,G,B] and Print
color_list_rgb = []
convert_color_list_to_rgb(color_list)
indigo.server.log("---------------------------------------------------------")
indigo.server.log("color_list_rgb - Valid Hex Color Values Converted to [R,G,B] = " + str(color_list_rgb))

#The Number of Color Names needs to be equal to or greater than the Number of Bulbs
if len(color_list_rgb) < len(bulb_list):
	color_list_rgb = (color_list_rgb * len(bulb_list))[slice(0,len(bulb_list))]
	indigo.server.log("---------------------------------------------------------")
	indigo.server.log("The Bulb List Total is longer than the Color List Total, so the Color List has been extended")
color_list_bulb_total = list(color_list_rgb)

#Calculate List Totals	
bulb_list_total = len(bulb_list)
color_list_total = len(color_list_rgb)

list_comp_color_all_bulbs = [[i] * bulb_list_total for i in range(bulb_list_total)]

#Color List Index Nest
color_list_index_nested = (

	color_list_sequence_all_0_to_i
	+ (color_list_sequence_range_0_to_i
	+ color_list_sequence_range_i_to_0) * 2
	+ [[2] * bulb_list_total]
	+ (color_list_sequence_move_0_to_i
	+ color_list_sequence_move_i_to_0) * 2
	+ [[4] * bulb_list_total]
	+ (color_list_sequence_move_fill_0_to_i
	+ color_list_sequence_move_fill_i_to_0) * 2	
	+ [([0,2] * bulb_list_total)[slice(0,bulb_list_total)]]
	+ color_list_sequence_all_i_to_0

	)	

#Color List Indexed Calculations
color_list_index_nested_total = len(color_list_index_nested)

#Estimated Routine Time
estimated_routine_time_total_seconds = color_list_index_nested_total * (delay_total)
estimated_routine_time_minutes = estimated_routine_time_total_seconds/60
estimated_routine_time_seconds = estimated_routine_time_total_seconds % 60
estimated_routine_cycles_in_the_while_loop = (minutes_for_while_loop * 60 / estimated_routine_time_total_seconds)

#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list_rgb))
indigo.server.log("COLOR List Total = " + str(color_list_total))
indigo.server.log("Color List - Index Nested - " + str(color_list_index_nested))
indigo.server.log("Color List - Index Nested Total = " + str(color_list_index_nested_total))
indigo.server.log("Estimated Routine Time = " + str(estimated_routine_time_minutes) + ":" + str(estimated_routine_time_seconds) + " (mm:ss)")
indigo.server.log("Estimated Routine Cycles in While Loop = " + str(estimated_routine_cycles_in_the_while_loop) + " cycles in the " + str(minutes_for_while_loop) + " minute while loop")
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

while time.time() < time_end_loop:	
	for i in color_list_index_nested:
		indigo.server.log("Color List - Index Nested : " + str(i))
		color_list_temp = []
		for x in range(bulb_list_total):
			color_list_temp.append(color_list_rgb[i[x]])
		indigo.server.log("Color List: " + str(color_list_temp))
		for x in range (bulb_list_total):
			color_value = color_list_temp[x]
			bulb_id = bulb_list[x] 
			set_bulb_color_rgb (
				color_value = color_value,
				bulb_id = bulb_id, 
				ramp_rate = ramp_rate, 
				)
		print_delay_total()	
		time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

indigo.server.log("======================= C O M P L E T E =======================")


#END PROGRAM
elapsed_time = time.time() - start_time
indigo.server.log("COMPLETE!")
indigo.server.log("STOP Time for PROGRAM - " + title_program)
print_time_stamp()
indigo.server.log("ELAPSED Time PROGRAM - " + title_program + " - " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
indigo.server.log("================= P R O G R A M   E N D  ===============")
