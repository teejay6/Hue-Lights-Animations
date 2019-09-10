#Script for Christmas Lights

import time
import random
from matplotlib import colors 

#TITLE FOR SCRIPT
title_program = "Hue v22 - Color Looper with color hues"

#VARIABLES - TIME DEFAULTS
ramp_rate_default = 2
delay_margin_default = 1

#VARIABLES - TIME ROUTINES
ramp_rate_pause = 5
delay_margin_pause = 2

ramp_rate_fade = 5
delay_margin_fade = 0

#TIME - INITIALIZATIONS
ramp_rate = ramp_rate_default
delay_margin = delay_margin_default
delay_total = ramp_rate + delay_margin

start_time = time.time()

#VARIABLES - Minutes for while loop for Routine
minutes_for_while_loop = 9
time_end_loop = time.time() + 60 * minutes_for_while_loop

#COLOR DICTIONARY SELECTION
color_name_dict = colors.cnames

color_list_christmas_primary = [
	"red",
	"magenta",
	"blue",
	"cyan",	
	"lime",
	"yellow",
	]

color_list_christmas_orange = [
	"red",
	"magenta",
	"blue",
	"darkorange",	
	"lime",
	"yellow",
	]

color_scene_reds = [
	"lightsalmon",
	"salmon",
	"darksalmon",
	"lightcoral",
	"indianred",
	"crimson",
	"firebrick",
	"darkred",
	"red",
	]	
	
color_scene_magentas = [
	"lavender",
	"thistle",
	"plum",
	"violet",
	"orchid",
	"fuchsia",
	"magenta",
	"mediumorchid",
	"mediumpurple",
	"blueviolet",
	"darkviolet",
	"darkorchid",
	"darkmagenta",
	"purple",
	"indigo",
	"darkslateblue",
	"slateblue",
	"mediumslateblue",
	]	
	
color_scene_blues = [
	"lightsteelblue",
	"powderblue",
	"lightblue",
	"skyblue",
	"lightskyblue",
	"deepskyblue",
	"dodgerblue",
	"cornflowerblue",
	"steelblue",
	"royalblue",
	"blue",
	"mediumblue",
	"darkblue",
	"navy",
	"midnightblue",
	]

color_scene_oranges = [
	"orangered",
	"tomato",
	"coral",
	"darkorange",
	"orange",
	]			

color_scene_greens = [
	"darkolivegreen",
	"olive",
	"olivedrab",
	"yellowgreen",
	"limegreen",
	"lime",
	"lawngreen",
	"chartreuse",
	"greenyellow",
	"springgreen",
	"mediumspringgreen",
	"lightgreen",
	"palegreen",
	"darkseagreen",
	"mediumaquamarine",
	"mediumseagreen",
	"seagreen",
	"forestgreen",
	"green",
	"darkgreen",
	]
	
color_scene_yellows = [
	"yellow",
	"lightyellow",
	"lemonchiffon",
	"lightgoldenrodyellow",
	"papayawhip",
	"moccasin",
	"peachpuff",
	"palegoldenrod",
	"khaki",
	"darkkhaki",
	"gold",
	]		
	
#SEQUENCE LISTS - Color[x] in bulb_list
color_list_sequence_chase_1_loop = [
	[1,0,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,0,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,0],
	[0,0,0,0,0,1],
	[0,0,0,0,1,0],
	[0,0,0,1,0,0],
	[0,0,1,0,0,0],
	[0,1,0,0,0,0],
	[1,0,0,0,0,0],
	]
	
color_list_sequence_chase_1_loop_fill = [
	[1,0,0,0,0,0],
	[1,1,0,0,0,0],
	[1,1,1,0,0,0],
	[1,1,1,1,0,0],
	[1,1,1,1,1,0],
	[1,1,1,1,1,1],
	[1,1,1,1,1,0],
	[1,1,1,1,0,0],
	[1,1,1,0,0,0],
	[1,1,0,0,0,0],
	[1,0,0,0,0,0],
	]
	

color_list_sequence_chase_1 = [
	[1,0,0,0,0,0],
	[0,1,0,0,0,0],
	[0,0,1,0,0,0],
	[0,0,0,1,0,0],
	[0,0,0,0,1,0],
	[0,0,0,0,0,1],
	]

color_list_sequence_chase_1_reverse = [
	[0,0,0,0,0,1],
	[0,0,0,0,1,0],
	[0,0,0,1,0,0],
	[0,0,1,0,0,0],
	[0,1,0,0,0,0],
	[1,0,0,0,0,0],
	]

color_list_sequence_chase_2_loop = [
	[1,1,0,0,0,0],
	[0,1,1,0,0,0],
	[0,0,1,1,0,0],
	[0,0,0,1,1,0],
	[0,0,0,0,1,1],
	[0,0,0,1,1,0],
	[0,0,1,1,0,0],
	[0,1,1,0,0,0],
	[1,1,0,0,0,0],
	]		

color_list_sequence_all_0 = [
	[0,0,0,0,0,0],
	]

color_list_sequence_all_1 = [
	[1,1,1,1,1,1],
	]
	
color_list_sequence_alt_1 = [
	[0,1,0,1,0,1],
	[1,0,1,0,1,0],
	]

color_list_sequence_alt_2 = [
	[1,1,0,0,1,1],
	[0,0,1,1,0,0],
	]

color_list_sequence_alt_3 = [
	[1,1,1,0,0,0],
	[0,0,0,1,1,1],
	]
		
color_list_sequence_hopscotch_1_loop = [
	[1,0,0,0,0,0],
	[0,1,0,0,0,0],
	[1,0,0,0,0,0],
	[0,0,1,0,0,0],
	[1,0,0,0,0,0],
	[0,0,0,1,0,0],
	[1,0,0,0,0,0],
	[0,0,0,0,1,0],
	[1,0,0,0,0,0],
	[0,0,0,0,0,1],
	[0,0,0,0,1,0],
	[0,0,0,0,0,1],
	[0,0,0,1,0,0],
	[0,0,0,0,0,1],
	[0,0,1,0,0,0],
	[0,0,0,0,0,1],
	[0,1,0,0,0,0],
	[0,0,0,0,0,1],
	[1,0,0,0,0,0],
	]

color_list_sequence_rainbow_05 = [
	[0,1,2,3,4,5],	
	]

color_list_sequence_rainbow_50 = [
	[5,4,3,2,1,0],
	]		

color_list_sequence_rainbow_chase = [
	[0,1,2,3,4,5],
	[5,0,1,2,3,4],
	[4,5,0,1,2,3],
	[3,4,5,0,1,2],
	[2,3,4,5,0,1],
	[1,2,3,4,5,0],
	[0,1,2,3,4,5],
	]		
 	
color_list_sequence_rainbow_chase_reverse = [
	[0,1,2,3,4,5],
	[1,2,3,4,5,0],
	[2,3,4,5,0,1],
	[3,4,5,0,1,2],
	[4,5,0,1,2,3],
	[5,0,1,2,3,4],
	[0,1,2,3,4,5],
	]	

color_list_sequence_rainbow_chase_loop_fill = [
	[0,1,2,3,4,5],
	[0,0,2,3,4,5],
	[0,0,0,3,4,5],
	[0,0,0,0,4,5],
	[0,0,0,0,0,5],
	[0,0,0,0,0,0],
	[0,0,0,0,0,5],
	[0,0,0,0,4,5],
	[0,0,0,3,4,5],
	[0,0,2,3,4,5],
	[0,1,2,3,4,5],
	]	

color_list_sequence_rainbow_smash = [
	[1,0,0,0,0,2],
	[0,1,0,0,2,0],
	[0,0,1,2,0,0],
	[0,0,2,1,0,0],
	[0,2,0,0,1,0],
	[2,0,0,0,0,1],
	]	

color_list_sequence_rainbow_spin_each = [
	[0,1,2,3,4,5],
	[1,1,2,3,4,5],
	[2,1,2,3,4,5],
	[3,1,2,3,4,5],
	[4,1,2,3,4,5],
	[5,1,2,3,4,5],
	[0,1,2,3,4,5],
	[0,2,2,3,4,5],
	[0,3,2,3,4,5],
	[0,4,2,3,4,5],
	[0,5,2,3,4,5],
	[0,0,2,3,4,5],
	[0,1,2,3,4,5],
	[0,1,3,3,4,5],
	[0,1,4,3,4,5],
	[0,1,5,3,4,5],
	[0,1,0,3,4,5],
	[0,1,1,3,4,5],
	[0,1,2,3,4,5],
	[0,1,2,4,4,5],
	[0,1,2,5,4,5],
	[0,1,2,0,4,5],
	[0,1,2,1,4,5],
	[0,1,2,2,4,5],
	[0,1,2,3,4,5],
	[0,1,2,3,5,5],
	[0,1,2,3,0,5],
	[0,1,2,3,1,5],
	[0,1,2,3,2,5],
	[0,1,2,3,3,5],
	[0,1,2,3,4,5],
	[0,1,2,3,4,0],
	[0,1,2,3,4,1],
	[0,1,2,3,4,2],
	[0,1,2,3,4,3],
	[0,1,2,3,4,4],
	[0,1,2,3,4,5],
	]	
color_list_sequence_rainbow_spin_alt = [
	[0,1,2,3,4,5],
	[1,1,2,3,4,5],
	[2,1,2,3,4,5],
	[3,1,2,3,4,5],
	[4,1,2,3,4,5],
	[5,1,2,3,4,5],
	[0,1,0,3,4,5],
	[1,1,1,3,4,5],
	[2,1,2,3,4,5],
	[3,1,3,3,4,5],
	[4,1,4,3,4,5],
	[5,1,5,3,4,5],
	[0,1,0,3,0,5],
	[1,1,1,3,1,5],
	[2,1,2,3,2,5],
	[3,1,3,3,3,5],
	[4,1,4,3,4,5],
	[5,1,5,3,5,5],
	[0,0,2,3,4,5],
	[0,1,2,3,4,5],
	[0,2,2,3,4,5],
	[0,3,2,3,4,5],
	[0,4,2,3,4,5],
	[0,5,2,3,4,5],
	[0,0,2,0,4,5],
	[0,1,2,1,4,5],
	[0,2,2,2,4,5],
	[0,3,2,3,4,5],
	[0,4,2,4,4,5],
	[0,5,2,5,4,5],
	[0,0,2,0,4,0],
	[0,1,2,1,4,1],
	[0,2,2,2,4,2],
	[0,3,2,3,4,3],
	[0,4,2,4,4,4],
	[0,5,2,5,4,5],
	]	
	
				
#COLOR DICTIONARY and LIST SELECTIONS
random.shuffle(color_list_christmas_orange)
color_list_initial  = list(color_list_christmas_orange)
color_list = list(color_list_initial)


#List of Bulbs in Group OFFICE
#indigo.devices[345799647] # "Lights - Office Desk Lamp Left - Hue7C"
#indigo.devices[462130400] # "Lights - Office Desk Lamp Right - Hue6C"
#indigo.devices[1486801916] # "Lights - Office Candlestick Lamp - Hue8C"
#indigo.devices[1438718908] # "Lights - Office - HueIris1C"
#indigo.devices[91173683] # "Lights - Office Standing Lamp Left - Hue5C"
#indigo.devices[764325856] # "Lights - Office Standing Lamp Right - Hue4C"
#indigo.devices[1233813775] # "Lights - Office Overhead Light - Hue9C"

#indigo.devices[1648446928] # "Lights - Office Hue Light Strip Outdoor - HueLSOut1C

#List of Bulbs in Group HOLIDAY
#indigo.devices[38251830] # "Lights - Holiday Eave Right 1 Hue Light Strip Outdoor - HueLSOut51C"
#indigo.devices[951519360] # "Lights - Holiday Eave Right 2 Hue Light Strip Outdoor - HueLSOut52C"
#indigo.devices[954492406] # "Lights - Holiday Eave Right 3 Hue Light Strip Outdoor - HueLSOut53C"
#indigo.devices[244822736] # "Lights - Holiday Eave Right 4 Hue Light Strip Outdoor - HueLSOut54C"
#indigo.devices[28616523] # "Lights - Holiday Eave Right 5 Hue Light Strip Outdoor - HueLSOut55C"
#indigo.devices[1768592995] # "Lights - Holiday Eave Right 6 Hue Light Strip Outdoor - HueLSOut56C"

#List of Bulbs in Group Outside Garage
# indigo.devices[555256509] # "Lights - Outside Garage Door Right1 - Hue Candle 5C"
# indigo.devices[1986057026] # "Lights - Outside Garage Door Right2 - Hue Candle 6C"
# indigo.devices[378158986] # "Lights - Outside Garage Door Left2 - Hue Candle 2C"
# indigo.devices[1321776156] # "Lights - Outside Garage Door Left1 - Hue Candle 1C"

#List of Bulbs in Group Outside Front Porch
#indigo.devices[1152879806]  "Lights - Out Porch Front Door Left - Hue14C"
#indigo.devices[1015547493]  "Lights - Out Porch Front Door Right - Hue15C"

#List of Bulbs in Group Inside Light Strips
#indigo.devices[62726078] # "Lights - Holiday Hue Light Strip Indoor - Living Room - HueLS3C"
#indigo.devices[203459146] # "Lights - Holiday Hue Light Strip Indoor - Dining Room - HueLS2C"

#List of Bulbs in Group Dining Room
# indigo.devices[26520548]  "Lights - Dining Room Table Left1 - Hue11C"
# indigo.devices[1369289963]  "Lights - Dining Room Table Left2 - Hue16C"
# indigo.devices[1622703196]  "Lights - Dining Room Table Right1 - Hue17C"
# indigo.devices[236819778]  "Lights - Dining Room Table Right2 - Hue18C"

#List of Bulbs in Group Living Room
# indigo.devices[1683800860]  "Lights - Living Room Long Table Lamp - Hue10C"
# indigo.devices[138374881]  "Lights - Living Room Round Table Lamp Left - Hue12C"
# indigo.devices[1357243185]  "Lights - Living Room Round Table Lamp Right - Hue13C"
# indigo.devices[208846243]  "Lights - Living Room Square Table Lamp Left - Hue Candle 3C"
# indigo.devices[545444555]  "Lights - Living Room Square Table Lamp Right - Hue Candle 4C"

#List of Bulbs in Group Guest Bedroom
# indigo.devices[400268110]  "Lights - BR-Guest Table Lamp Left - Hue19C"
# indigo.devices[1844597071]  "Lights - BR-Guest Table Lamp Right - Hue20C"


#BULB NAME LISTS
bulb_list_office = [
	345799647, 
	462130400,
	1648446928,
	1486801916,
	91173683,
	764325856, 
	1233813775,
	1648446928,
	]

bulb_list_test = [
	1648446928, 
	]

bulb_list_Dining_Living_GBR = [
	26520548, 
	1369289963, 
	1622703196, 
	236819778,
	1683800860,
	138374881,
	1357243185,
	208846243,
	545444555,
	400268110,
	1844597071,
	]
	
bulb_list_out_garage = [
	555256509, 
	1986057026, 
	378158986, 
	1321776156,
	]
	
bulb_list_outside = [
	555256509, 
	1986057026, 
	378158986, 
	1321776156,
	203459146,
	1152879806,
	1015547493,
	62726078,
	]

bulb_list_ls_inside = [
	203459146, 
	62726078,
	]		
	
bulb_list_christmas_all = [
	38251830, 
	951519360,
	954492406,
	244822736,
	28616523,
	1768592995,
	555256509, 
	1986057026, 
	378158986, 
	1321776156,
	203459146,
	1152879806,
	1015547493,
	62726078, 
	]	
	
bulb_list_office_6 = [
	345799647, 
	462130400,
	1648446928,
	1233813775,
	1486801916,
	91173683,
	]	
	
bulb_list_ls_christmas = [
	38251830, 
	951519360,
	954492406,
	244822736,
	28616523,
	1768592995, 
	]		
	
#BULB NAME LIST SELECTION
bulb_list_initial = list(bulb_list_ls_christmas)
bulb_list = list(bulb_list_initial)

#BRIGHTNESS LISTS
brightness_list_pulse = [
	100,
	20,
	100,
	20,
	]

#BRIGHTNESS SEQUENCE LISTS
brightness_list_sequence_20_100 = [
	[100,20,20,20,20,20],
	[20,100,20,20,20,20],
	[20,20,100,20,20,20],
	[20,20,20,100,20,20],
	[20,20,20,20,100,20],
	[20,20,20,20,20,100],
	]

brightness_list_sequence_20_100_reverse = [
	[20,20,20,20,20,100],
	[20,20,20,20,100,20],
	[20,20,20,100,20,20],
	[20,20,100,20,20,20],
	[20,100,20,20,20,20],
	[100,20,20,20,20,20],
	]

brightness_list_sequence_all_20 = [
	[20,20,20,20,20,20],
	]

brightness_list_sequence_all_100 = [
	[100,100,100,100,100,100],
	]	
	

#BRIGHTNESS LIST SELECTION
brightness_list = list(brightness_list_pulse)

#FUNCTIONS - PRINT
def print_bulb_state():
	bulb_name_name = indigo.devices[bulb_name].name
	color_red_RGB_state = indigo.devices[bulb_name].states['colorRed']
	color_green_RGB_state = indigo.devices[bulb_name].states['colorGreen']
	color_blue_RGB_state = indigo.devices[bulb_name].states['colorBlue']
	brightness_level_state = indigo.devices[bulb_name].states['brightnessLevel']
	color_temp_state = indigo.devices[bulb_name].states['colorTemp']
	indigo.server.log("STATE - Brightness: " + str(brightness_level_state) + " with RGB values: " + str(color_red_RGB_state) + ", " + str(color_green_RGB_state) + ", " + str(color_blue_RGB_state) + ", and Color Temp: " + str(color_temp_state))

def print_time_stamp():
	#print time stamp in preferred format
	indigo.server.log("Time Stamp: " + time.strftime('%Y-%m-%d %I:%M:%S %p'))

def print_start_elapsed_time(title_routine_set):
	#print time stamp and start time for a routine
	#start_time_temp = time.time()
	indigo.server.log("ROUTINE - " + title_routine_set)
	indigo.server.log("START Time Routine:")
	print_time_stamp() 

def print_stop_elapsed_time(title_routine_set):
	#print time stamp and stop time and elapsed time for a routine
	#elapsed_time_temp = time.time() - start_time_temp
	indigo.server.log("STOP Time ROUTINE - " + title_routine_set)
	print_time_stamp()
	indigo.server.log("ELAPSED Time ROUTINE - " + title_routine_set + " - " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time_temp)))

def print_delay_total ():
	indigo.server.log("DELAY Total: " + str(delay_total) + ", with Ramp Rate: " + str(ramp_rate) + ", plus Delay Margin: " + str(delay_margin))

#FUNCTIONS - SET BULBS

#def set_bulb_color_name_RGB (color_name_set, bulb_name_set, ramp_rate_set = 1):
	#set RGB, ramp rate, and brightness values for Hue Bulbs plugin - Look up color name in Dictionary
#	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
#	if plug.isEnabled():
#		red_color_set = color_name_dict[color_name_set].split(",")[0]
#		green_color_set = color_name_dict[color_name_set].split(",")[1]
#		blue_color_set = color_name_dict[color_name_set].split(",")[2]
#		plug.executeAction("setRGB", bulb_name_set, props={"red": red_color_set, "green": green_color_set, "blue": blue_color_set, "rate": ramp_rate_set})	

def set_bulb_color_name_RGB (color_name_set, bulb_name_set, ramp_rate_set = 1):
	#set RGB, ramp rate, and brightness values for Hue Bulbs plugin - Look up color name in matplotlib Dictionary
	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
	if plug.isEnabled():
		red_color_set = int(color_name_dict[color_name_set][1:3],16)
		green_color_set = int(color_name_dict[color_name_set][3:5],16)
		blue_color_set = int(color_name_dict[color_name_set][5:7],16)
		plug.executeAction("setRGB", bulb_name_set, props={"red": red_color_set, "green": green_color_set, "blue": blue_color_set, "rate": ramp_rate_set})	

def set_bulb_brightness (bulb_name_set, ramp_rate_set = 1, brightness_bulb_set = 100):
	#set brightness values for Hue Bulbs plugin
	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
	if plug.isEnabled():		
		plug.executeAction("setBrightness", bulb_name_set, props={"rate": ramp_rate_set, "brightness": brightness_bulb_set})
				
def set_bulb_color_number_RGB (red_color_set, green_color_set, blue_color_set, bulb_name_set, ramp_rate_set = 1):
	#set RGB, ramp rate, and brightness values for Hue Bulbs plugin - Input Numbers for each RGB Value
	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
	if plug.isEnabled():
		plug.executeAction("setRGB", bulb_name_set, props={"red": red_color_set, "green": green_color_set, "blue": blue_color_set, "rate": ramp_rate_set})		

def set_bulb_color_temperature_CT (color_temp_set, bulb_name_set, ramp_rate_set = 1):
	#set Color Temperature, ramp rate, and brightness values for Hue Bulbs plugin - Input Number for CT
	plug = indigo.server.getPlugin("com.nathansheldon.indigoplugin.HueLights")
	if plug.isEnabled():
		plug.executeAction("setCT", bulb_name_set, props={"temperature": color_temp_set, "rate": ramp_rate_set})

#FUNCTIONS - BRIGHTNESS AND COLOR TEMPERATURE FOR BULB LISTS 
def brightness_level_bulb_list():
	for bulb_name in bulb_list:
		set_bulb_brightness (
			bulb_name_set = bulb_name,	
			brightness_bulb_set = brightness_bulb,
			ramp_rate_set = ramp_rate,
			) 	
def color_temp_level_bulb_list():
	for bulb_name in bulb_list:
		set_bulb_color_temperature_CT (
			bulb_name_set = bulb_name, 
			color_temp_set = color_temp,
			ramp_rate_set = ramp_rate,
			)

#FUNCTIONS - LOOPS for COLORS and BULB LISTS		
def color_loop():
	#loop through each color in the list for all bulbs simultaneously
	for color_name in color_list:
		indigo.server.log("CHANGE COLOR:")
		indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])
		#delay_total = ramp_rate + delay_margin
		print_delay_total ()
		for bulb_name in bulb_list:
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
		time.sleep(delay_total)	
	
def color_chase():
	#loop through each color in the list one bulb at a time
	for color_name in color_list:
		indigo.server.log("CHANGE COLOR:")
		indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])
		for bulb_name in bulb_list:
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
			print_delay_total ()
			time.sleep(delay_total)	

def color_spin():
	#loop through all colors in the list one bulb at a time
	for bulb_name in bulb_list:
		for color_name in color_list:
			indigo.server.log("CHANGE COLOR:")
			indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])			
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
			print_delay_total ()
			time.sleep(delay_total)
		indigo.server.log("CHANGE BULB:")	
				
#PRINT INITIAL VARIABLE VALUES
indigo.server.log("================= P R O G R A M   S T A R T ============")
indigo.server.log("START Time for PROGRAM - " + title_program)
indigo.server.log("Time Stamp - " + time.strftime('%Y-%m-%d %I:%M:%S %p',time.localtime(start_time)))
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLE VALUES:")
color_name_dict_total = len(color_name_dict)	
indigo.server.log("COLORS in Dictionary: " + str(color_name_dict_total))

color_list_total = len(color_list)
indigo.server.log("COLORS in Selected List: " + str(color_list_total))
indigo.server.log("COLOR Names in Selected List:")
indigo.server.log(str(color_list))

bulb_list_total = len(bulb_list)
indigo.server.log("BULBS in Selected List: " + str(bulb_list_total))
indigo.server.log("BULB Names in Selected List:")
for bulb_name in bulb_list:	
	indigo.server.log("Bulb - " + str(indigo.devices[bulb_name].name) + ", " + str(bulb_name))
	
brightness_list_total = len(brightness_list)
indigo.server.log("BULB List Brightness - " + str(brightness_list))	
indigo.server.log("BULB List Brightness Total- " + str(brightness_list_total))	

print_delay_total ()

indigo.server.log("MINUTES for While Loop: " + str(minutes_for_while_loop) + " minutes")
indigo.server.log("---------------------------------------------------------")

#PROGRAM START
indigo.server.log("START :")
print_time_stamp()


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Color Loop - Fade - ALL Lights"

#Timing Variables
ramp_rate = 1
delay_margin = 1

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list = list(color_list_initial)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Color Loop and Fade <----- ")


#loop through each color in the list for all bulbs simultaneously, with fade to 0, then up to previous level
print_delay_total ()
for color_name in color_list:
	indigo.server.log("CHANGE COLOR:")
	indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])				
	for bulb_name in bulb_list:
		ramp_rate = 1
		delay_margin = 1
		delay_total = ramp_rate + delay_margin
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total ()
	time.sleep(delay_total)
	brightness_bulb = 0
	for bulb_name in bulb_list:
		ramp_rate = 5
		delay_margin = 0
		delay_total = ramp_rate + delay_margin
		set_bulb_brightness (
		bulb_name_set = bulb_name,	
		brightness_bulb_set = brightness_bulb,
		ramp_rate_set = ramp_rate,
		) 
	print_delay_total ()
	time.sleep(delay_total)
		
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Chase and Reverse"

#Timing Variables
#ramp_rate = ramp_rate_pause
#delay_margin = delay_margin_pause
ramp_rate = 1
delay_margin = 1

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_rainbow_chase
	+ color_list_sequence_rainbow_chase_reverse
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")


for i in sequence_list:
	indigo.server.log("SEQUENCE List: " + str(i))
	color_list = []
	for x in range(bulb_list_total):
		color_list.append(str(color_list_2[i[x]]))
	indigo.server.log("Color List: " + str(color_list))
	for x in range (bulb_list_total):
		color_name = color_list[x]
		bulb_name = bulb_list[x] 
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Brightness Sequence"

#Timing Variables
ramp_rate = .5
delay_margin = 2

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list_brightness_2 = (
	brightness_list_sequence_20_100
	+ brightness_list_sequence_20_100_reverse
	+ brightness_list_sequence_all_100
	+ brightness_list_sequence_all_20
	+ brightness_list_sequence_all_100
	)
sequence_list_brightness = sequence_list_brightness_2

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_brightness_total = len(sequence_list_brightness)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List Brightness - " + str(sequence_list_brightness))
indigo.server.log("SEQUENCE List Brightness Total - " + str(sequence_list_brightness_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence 6 Bulbs Brightness <----- ")


for i in sequence_list_brightness:
	indigo.server.log("SEQUENCE Brightness List: " + str(i))
	for x in range (bulb_list_total):
		brightness_bulb = i[x]
		indigo.server.log("Brightness List: " + str(brightness_bulb))
		bulb_name = bulb_list[x] 
		indigo.server.log("Bulb Name List: " + str(bulb_name))
		set_bulb_brightness (
			bulb_name_set = bulb_name,	
			brightness_bulb_set = brightness_bulb,
			ramp_rate_set = ramp_rate,
			) 	
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Rainbow Random"

#Timing Variables
ramp_rate = 3
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list = list(color_list_initial)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Randomize Rainbow Colors <----- ")


#loop through all colors in the list on different bulbs simultaneously
#for color_name in color_list:
while time.time() < time_end_loop:		
	c = random.randint(0, color_list_total - 1)
	b = random.randint(0, bulb_list_total - 1)
	color_name = color_list[c]
	bulb_name = bulb_list[b]
	indigo.server.log("RANDOM Color is - " + str(color_name))
	indigo.server.log("RANDOM Bulb is - " + str(bulb_name)) 
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)	
	delay_margin = random.randint(2,10)
	indigo.server.log("RANDOM Delay Margin Rate: " + str(delay_margin))
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)

		
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Color Loop"

#Timing Variables
ramp_rate = 1
delay_margin = 2

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list  = list(
	color_scene_reds
	+ color_scene_magentas
	+ color_scene_blues
	+ color_scene_oranges
	+ color_scene_greens
	+ color_scene_yellows
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Color Loop and Fade <----- ")


#loop through each color in the list for all bulbs simultaneously, with fade to 0, then up to previous level
print_delay_total ()
for color_name in color_list:
	indigo.server.log("CHANGE COLOR:")
	indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])				
	for bulb_name in bulb_list:
		ramp_rate = 1
		delay_margin = 2
		delay_total = ramp_rate + delay_margin
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total ()
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Two Color [0] to [1] to [0]"

#Timing Variables
ramp_rate = 2
delay_margin = 2

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)
#bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)


#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
color_list_2_total = len(color_list_2)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list_2))
indigo.server.log("COLOR List 2 Total - " + str(color_list_2_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Two Color " + str(bulb_list_total) + " Bulbs <----- ")

color_name = color_list_2[0]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)

color_name = color_list_2[1]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)

color_name = color_list_2[0]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)


#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 20 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 20

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)
#bulb_list = list(bulb_list_initial)

#Brightness Variables
brightness_bulb = 20

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Color [0] Brightness Chase Sequence"

#Timing Variables
ramp_rate = .25
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list_brightness_2 = (
	brightness_list_sequence_all_20
	+ brightness_list_sequence_20_100 * 3
	+ brightness_list_sequence_20_100_reverse * 3
	+ brightness_list_sequence_all_20
	)
sequence_list_brightness = sequence_list_brightness_2

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_brightness_total = len(sequence_list_brightness)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List Brightness - " + str(sequence_list_brightness))
indigo.server.log("SEQUENCE List Brightness Total - " + str(sequence_list_brightness_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs Brightness <----- ")


for i in sequence_list_brightness:
	indigo.server.log("SEQUENCE Brightness List: " + str(i))
	for x in range (bulb_list_total):
		brightness_bulb = i[x]
		indigo.server.log("Brightness List: " + str(brightness_bulb))
		bulb_name = bulb_list[x] 
		indigo.server.log("Bulb Name List: " + str(bulb_name))
		set_bulb_brightness (
			bulb_name_set = bulb_name,	
			brightness_bulb_set = brightness_bulb,
			ramp_rate_set = ramp_rate,
			) 	
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Intermezzo: All Bulbs One Color"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[0]

#Brightness Variables
brightness_bulb = 20

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name is - " + str(color_name))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs One Color <----- ")

for bulb_name in bulb_list:
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Two Color - Random color[0] to color[1]"

#Timing Variables
ramp_rate = 1
delay_margin = delay_margin_default

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[1]

#Randomization - Variables
random.shuffle(bulb_list)
indigo.server.log("Random Bulb List - " + str(bulb_list))			

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name - " + str(color_name))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Random " + str(bulb_list_total) + " Bulbs <----- ")

for bulb_name in bulb_list:
	indigo.server.log("RANDOM Bulb is - " + str(bulb_name))
	ramp_rate = 3
	delay_margin = 2	
	brightness_bulb = 100
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)	
	ramp_rate = 3
	delay_margin = 0	
	brightness_bulb = 0
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)	
	delay_margin = random.randint(0,3)
	indigo.server.log("RANDOM Delay Margin Rate: " + str(delay_margin))
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)	
	brightness_bulb = 50
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Intermezzo: All Bulbs One Color"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[1]

#Brightness Variables
brightness_bulb = 20

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name is - " + str(color_name))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs One Color <----- ")

for bulb_name in bulb_list:
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Two Color - Random color[1] to color[0]"

#Timing Variables
ramp_rate = 1
delay_margin = delay_margin_default

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[0]

#Randomization - Variables
random.shuffle(bulb_list)
indigo.server.log("Random Bulb List - " + str(bulb_list))			

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name - " + str(color_name))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Random " + str(bulb_list_total) + " Bulbs <----- ")

for bulb_name in bulb_list:
	indigo.server.log("RANDOM Bulb is - " + str(bulb_name))
	ramp_rate = 3
	delay_margin = 2	
	brightness_bulb = 100
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)	
	ramp_rate = 3
	delay_margin = 0	
	brightness_bulb = 0
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)	
	delay_margin = random.randint(0,3)
	indigo.server.log("RANDOM Delay Margin Rate: " + str(delay_margin))
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)	
	brightness_bulb = 50
	set_bulb_brightness (		
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		brightness_bulb_set = brightness_bulb,
		)
	delay_total = ramp_rate + delay_margin
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Chases Alternates and Loops"

#Timing Variables
ramp_rate = 1
delay_margin = 1

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_all_0 
	+ color_list_sequence_chase_1_loop * 2
	+ color_list_sequence_all_0 
	+ color_list_sequence_chase_1_loop_fill * 2
	+ color_list_sequence_all_0
	+ color_list_sequence_chase_2_loop * 2
	+ color_list_sequence_all_0
	+ color_list_sequence_alt_1 * 3
	+ color_list_sequence_all_0
	+ color_list_sequence_alt_2 * 3
	+ color_list_sequence_all_0
	+ color_list_sequence_alt_3 * 3
	+ color_list_sequence_all_0
	+ color_list_sequence_hopscotch_1_loop * 2
	+ color_list_sequence_all_0 
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

for c in range(color_list_total):
	for i in sequence_list:
		indigo.server.log("SEQUENCE List: " + str(i))
		color_list = []
		for x in range(bulb_list_total):
			color_list.append(str(color_list_2[i[x]]))
		indigo.server.log("Color List: " + str(color_list))
		for x in range (bulb_list_total):
			color_name = color_list[x]
			bulb_name = bulb_list[x] 
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
		print_delay_total()	
		time.sleep(delay_total)
	color_list_2.append(color_list_2.pop(0))
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Two Color [0] to [1] to [0]"

#Timing Variables
ramp_rate = 2
delay_margin = 2

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)
#bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)


#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
color_list_2_total = len(color_list_2)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list_2))
indigo.server.log("COLOR List 2 Total - " + str(color_list_2_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Two Color " + str(bulb_list_total) + " Bulbs <----- ")

color_name = color_list_2[0]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)

color_name = color_list_2[1]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)

color_name = color_list_2[0]
for bulb_name in bulb_list:
	set_bulb_color_name_RGB (
		color_name_set = color_name,
		bulb_name_set = bulb_name, 
		ramp_rate_set = ramp_rate, 
		)
print_delay_total ()
time.sleep(delay_total)


#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 20 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 20

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)
#bulb_list = list(bulb_list_initial)

#Brightness Variables
brightness_bulb = 20

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Color [0] Brightness Chase Sequence"

#Timing Variables
ramp_rate = .25
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list_brightness_2 = (
	brightness_list_sequence_all_20
	+ brightness_list_sequence_20_100 * 3
	+ brightness_list_sequence_20_100_reverse * 3
	)
sequence_list_brightness = sequence_list_brightness_2

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_brightness_total = len(sequence_list_brightness)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List Brightness - " + str(sequence_list_brightness))
indigo.server.log("SEQUENCE List Brightness Total - " + str(sequence_list_brightness_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs Brightness <----- ")


for i in sequence_list_brightness:
	indigo.server.log("SEQUENCE Brightness List: " + str(i))
	for x in range (bulb_list_total):
		brightness_bulb = i[x]
		indigo.server.log("Brightness List: " + str(brightness_bulb))
		bulb_name = bulb_list[x] 
		indigo.server.log("Bulb Name List: " + str(bulb_name))
		set_bulb_brightness (
			bulb_name_set = bulb_name,	
			brightness_bulb_set = brightness_bulb,
			ramp_rate_set = ramp_rate,
			) 	
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Brighten to 100 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 100

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)
#bulb_list = list(bulb_list_initial)

#Brightness Variables
brightness_bulb = 100

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Chase"

#Timing Variables
ramp_rate = 1
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_rainbow_05
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

for c in range(color_list_total + 1):
	for i in sequence_list:
		indigo.server.log("SEQUENCE List: " + str(i))
		color_list = []
		for x in range(bulb_list_total):
			color_list.append(str(color_list_2[i[x]]))
		indigo.server.log("Color List: " + str(color_list))
		for x in range (bulb_list_total):
			color_name = color_list[x]
			bulb_name = bulb_list[x] 
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
		print_delay_total()	
		time.sleep(delay_total)
	color_list_2.append(color_list_2.pop(0))
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################



# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################



# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Intermezzo: All Bulbs One Color"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[2]

#Brightness Variables
brightness_bulb = 50

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name is - " + str(color_name))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs One Color <----- ")

for bulb_name in bulb_list:
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Variables:
title_routine_set = "Color Chase - Fade"
ramp_rate = 1
delay_margin = 1
#ramp_rate = random.randint(1,5)
#indigo.server.log("RANDOM Ramp Rate: " + str(ramp_rate))

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
color_list  = list(color_list_initial)
indigo.server.log("COLOR Name List - " + str(color_list))
bulb_list = list(bulb_list_initial)
indigo.server.log("BULB List - " + str(bulb_list))

#Randomization - Variables
#random.shuffle(color_list)
#indigo.server.log("RANDOM Color Name List - " + str(color_list))
#random.shuffle(bulb_list)
#indigo.server.log("Random Bulb List - " + str(bulb_list))		

#Routine MAIN 
#while time.time() < time_end_loop:
#loop through each color in the list one bulb at a time, with fade to 0, then up to previous level
for color_name in color_list:
	indigo.server.log("CHANGE COLOR:")
	indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])
	for bulb_name in bulb_list:
		ramp_rate = 2
		delay_margin = 0
		delay_total = ramp_rate + delay_margin
		brightness_bulb = 0
		set_bulb_brightness (
		bulb_name_set = bulb_name,	
		brightness_bulb_set = brightness_bulb,
		ramp_rate_set = ramp_rate,
		) 
		print_delay_total ()
		time.sleep(delay_total)
		ramp_rate = 2
		delay_margin = 0
		delay_total = ramp_rate + delay_margin		
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
		print_delay_total ()
		time.sleep(delay_total)	

#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Intermezzo: All Bulbs One Color"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[3]

#Brightness Variables
brightness_bulb = 50

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name is - " + str(color_name))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs One Color <----- ")

for bulb_name in bulb_list:
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Chase Loop Fill"

#Timing Variables
ramp_rate = 1
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_rainbow_chase_loop_fill
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

for c in range(color_list_total + 1):
	for i in sequence_list:
		indigo.server.log("SEQUENCE List: " + str(i))
		color_list = []
		for x in range(bulb_list_total):
			color_list.append(str(color_list_2[i[x]]))
		indigo.server.log("Color List: " + str(color_list))
		for x in range (bulb_list_total):
			color_name = color_list[x]
			bulb_name = bulb_list[x] 
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
		print_delay_total()	
		time.sleep(delay_total)
	color_list_2.append(color_list_2.pop(0))
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Smash"

#Timing Variables
ramp_rate = 1
delay_margin = 0

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_all_0 
	+ color_list_sequence_rainbow_smash
	+ color_list_sequence_all_1 
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

for c in range(color_list_total + 1):
	for i in sequence_list:
		indigo.server.log("SEQUENCE List: " + str(i))
		color_list = []
		for x in range(bulb_list_total):
			color_list.append(str(color_list_2[i[x]]))
		indigo.server.log("Color List: " + str(color_list))
		for x in range (bulb_list_total):
			color_name = color_list[x]
			bulb_name = bulb_list[x] 
			#delay_total = ramp_rate + delay_margin
			set_bulb_color_name_RGB (
				color_name_set = color_name,
				bulb_name_set = bulb_name, 
				ramp_rate_set = ramp_rate, 
				)
		print_delay_total()	
		time.sleep(delay_total)
	color_list_2.append(color_list_2.pop(0))
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Intermezzo: All Bulbs One Color"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)
color_name = color_list[4]

#Brightness Variables
brightness_bulb = 50

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)



#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("COLOR Name is - " + str(color_name))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs One Color <----- ")

for bulb_name in bulb_list:
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Variables:
title_routine_set = "Color Spin"
ramp_rate = 1
delay_margin = 1
#ramp_rate = random.randint(1,5)
#indigo.server.log("RANDOM Ramp Rate: " + str(ramp_rate))

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
color_list  = list(color_list_initial)
indigo.server.log("COLOR Name List - " + str(color_list))
#bulb_list = list(bulb_list_initial) + list(bulb_list_out_garage) + list(bulb_list_ls_inside)
bulb_list = list(bulb_list_initial)
indigo.server.log("BULB List - " + str(bulb_list))

#Randomization - Variables
random.shuffle(color_list)
indigo.server.log("RANDOM Color Name List - " + str(color_list))
random.shuffle(bulb_list)
indigo.server.log("Random Bulb List - " + str(bulb_list))		

#Routine MAIN 
#while time.time() < time_end_loop:
color_spin()

#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Spin - Each then Alternate Bulbs"

#Timing Variables
#ramp_rate = ramp_rate_pause
#delay_margin = delay_margin_pause
ramp_rate = 1
delay_margin = 1

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_rainbow_spin_each
	+ color_list_sequence_rainbow_spin_alt
	+ color_list_sequence_rainbow_05
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")


for i in sequence_list:
	indigo.server.log("SEQUENCE List: " + str(i))
	color_list = []
	for x in range(bulb_list_total):
		color_list.append(str(color_list_2[i[x]]))
	indigo.server.log("Color List: " + str(color_list))
	for x in range (bulb_list_total):
		color_name = color_list[x]
		bulb_name = bulb_list[x] 
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Color Loop - Fade - ALL Lights"

#Timing Variables
ramp_rate = 1
delay_margin = 1

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Color Variables
color_list = list(color_list_initial)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List - " + str(color_list))
indigo.server.log("COLOR List Total - " + str(color_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")
indigo.server.log("-----> Color Loop and Fade <----- ")


#loop through each color in the list for all bulbs simultaneously, with fade to 0, then up to previous level
print_delay_total ()
for color_name in color_list:
	indigo.server.log("CHANGE COLOR:")
	indigo.server.log("Color Selected: " + color_name + ", with RGB Values: "+ color_name_dict[color_name])				
	for bulb_name in bulb_list:
		ramp_rate = 1
		delay_margin = 1
		delay_total = ramp_rate + delay_margin
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total ()
	time.sleep(delay_total)
	brightness_bulb = 0
	for bulb_name in bulb_list:
		ramp_rate = 5
		delay_margin = 1
		delay_total = ramp_rate + delay_margin
		set_bulb_brightness (
		bulb_name_set = bulb_name,	
		brightness_bulb_set = brightness_bulb,
		ramp_rate_set = ramp_rate,
		) 
	print_delay_total ()
	time.sleep(delay_total)
		
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Pause - Dim to Brightness 0 - ALL Lights"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

brightness_bulb = 0

#Bulb Variables
bulb_list = list(bulb_list_initial) + list(bulb_list_outside)

#Brightness Variables
brightness_bulb = 0

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("INITIAL VARIABLES & SETTINGS for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("BRIGHTNESS - " + str(brightness_bulb))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")

brightness_level_bulb_list()

#Routine Delay: 
print_delay_total ()
time.sleep(delay_total)	
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################

# ---> ROUTINE BEGIN ######################################################

#Routine Title:
indigo.server.log("================= R O U T I N E   S T A R T ============")
title_routine_set = "Sequences - Rainbow Still"

#Timing Variables
ramp_rate = ramp_rate_pause
delay_margin = delay_margin_pause

#Bulb Variables
bulb_list = list(bulb_list_initial)

#Color Variables
color_list_2 = list(color_list_initial)
color_list = list(color_list_2)

#Sequence Variables
sequence_list = (
	color_list_sequence_rainbow_05 
	+ color_list_sequence_rainbow_50
	+ color_list_sequence_rainbow_05
	)

#Routine Initialization
delay_total = ramp_rate + delay_margin
start_time_temp = time.time()
print_start_elapsed_time(title_routine_set)
bulb_list_total = len(bulb_list)
color_list_total = len(color_list)
sequence_list_total = len(sequence_list)


#Print Variables and Initial Settings
indigo.server.log("---------------------------------------------------------")
indigo.server.log("Variables and Initial Settings for: "+ title_routine_set)
print_delay_total ()
indigo.server.log("BULB List - " + str(bulb_list))
indigo.server.log("BULB List Total is - " + str(bulb_list_total))
indigo.server.log("COLOR List 2 - " + str(color_list))
indigo.server.log("COLOR List 2 Total - " + str(color_list_total))
indigo.server.log("SEQUENCE List - " + str(sequence_list))
indigo.server.log("SEQUENCE List Total - " + str(sequence_list_total))
indigo.server.log("---------------------------------------------------------")

#Routine MAIN
indigo.server.log("ROUTINE Main:")

indigo.server.log("-----> Sequence " + str(bulb_list_total) + " Bulbs <----- ")


for i in sequence_list:
	indigo.server.log("SEQUENCE List: " + str(i))
	color_list = []
	for x in range(bulb_list_total):
		color_list.append(str(color_list_2[i[x]]))
	indigo.server.log("Color List: " + str(color_list))
	for x in range (bulb_list_total):
		color_name = color_list[x]
		bulb_name = bulb_list[x] 
		set_bulb_color_name_RGB (
			color_name_set = color_name,
			bulb_name_set = bulb_name, 
			ramp_rate_set = ramp_rate, 
			)
	print_delay_total()	
	time.sleep(delay_total)
	
#Routine COMPLETE	
elapsed_time_temp = time.time() - start_time_temp
print_stop_elapsed_time(title_routine_set)
indigo.server.log("================= R O U T I N E   E N D ================")

# <--- ROUTINE END ########################################################


#END PROGRAM
elapsed_time = time.time() - start_time
indigo.server.log("COMPLETE!")
indigo.server.log("STOP Time for PROGRAM - " + title_program)
print_time_stamp()
indigo.server.log("ELAPSED Time PROGRAM - " + title_program + " - " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
indigo.server.log("================= P R O G R A M   E N D  ===============")
