#Color Animation Utilities for Indigo Domo and Hue Lights
#Uses the Hue Lights plugin from Nathan Sheldon Software

#Add to : /Library/Python/2.7/site-packages/

#Defines Site Speciic Configurations like Bulb ID Numbers
#Defines Sequence Lists for Animations and Brightness
#Defines Functions for Colors and Animation - to be implemented at a later date

# ---> START: SITE SPECIFIC CONFIGURATION ################################################

#********* USER CONFIGURATION REQUIRED START *********

# Define Lists of BULB ID's in Sequence Order

# BULB LIST: OUTSIDE HOLIDAY Light Strips
#indigo.devices[38251830] # "Lights - Holiday Eave Right 1 Hue Light Strip Outdoor - HueLSOut51C"
#indigo.devices[951519360] # "Lights - Holiday Eave Right 2 Hue Light Strip Outdoor - HueLSOut52C"
#indigo.devices[954492406] # "Lights - Holiday Eave Right 3 Hue Light Strip Outdoor - HueLSOut53C"
#indigo.devices[244822736] # "Lights - Holiday Eave Right 4 Hue Light Strip Outdoor - HueLSOut54C"
#indigo.devices[28616523] # "Lights - Holiday Eave Right 5 Hue Light Strip Outdoor - HueLSOut55C"
#indigo.devices[1768592995] # "Lights - Holiday Eave Right 6 Hue Light Strip Outdoor - HueLSOut56C"

bulb_list_ls_out_holiday = [
	38251830, 
	951519360,
	954492406,
	244822736,
	28616523,
	1768592995, 
	]	

# BULB LIST: OUTSIDE Garage Door Candle Lights
#indigo.devices[378158986] # "Lights - Out Garage Door Right1 - Hue Candle 2C"
#indigo.devices[1321776156] # "Lights - Out Garage Door Right2 - Hue Candle 1C"
#indigo.devices[1324747877] # "Lights - Out Garage Door Left1 - Hue Candle 5C"
#indigo.devices[1986057026] # "Lights - Out Garage Door Left2 - Hue Candle 6C"
	
bulb_list_out_garage = [
	378158986, 
	1321776156, 
	1324747877, 
	1986057026,
	]

# BULB LIST: OUTSIDE Porch Front Door Bulbs
#indigo.devices[1253643640] # "Lights - Out Porch Front Door Right - Hue15C"
#indigo.devices[1840706591] # "Lights - Out Porch Front Door Left - Hue14C"

bulb_list_out_porch = [
	1253643640, 
	1840706591, 
	]
# BULB LIST: OFFICE Right to Left - 6 Lights
#indigo.devices[764325856] # "Lights - Office Standing Lamp Right - Hue4C"
#indigo.devices[91173683] # "Lights - Office Standing Lamp Left - Hue5C"
#indigo.devices[1438718908] # "Lights - Office - HueIris1C"
#indigo.devices[1486801916] # "Lights - Office Candlestick Lamp - Hue8C"
#indigo.devices[462130400] # "Lights - Office Desk Lamp Right - Hue6C"
#indigo.devices[345799647] # "Lights - Office Desk Lamp Left - Hue7C"
#indigo.devices[1233813775] # "Lights - Office Overhead Light - Hue9C"

bulb_list_office_R2L_6 = [
	764325856, 
	91173683,
	1438718908,
	1486801916,
	462130400,
	345799647,
	]	

# BULB LIST: Office Light Strips and bulbs for TESTING Purposes 6 Lights
#indigo.devices[1648446928] # "Lights - Test 1 Hue Light Strip Out - HueLSOut21C"
#indigo.devices[127138598] # "Lights - Test 2 Hue Light Strip Out - HueLSOut22C"
#indigo.devices[62726078] # "Lights - Test 3 Hue Light Strip Indoor - HueLS3C"
#indigo.devices[203459146] # "Lights - Test 4 Hue Light Strip Indoor - HueLS2C"
#indigo.devices[462130400] # "Lights - Office Table Lamp Right - Hue6C"
#indigo.devices[345799647] # "Lights - Office Table Lamp Left - Hue7C"

bulb_list_office_test_6 = [
	1648446928, 
	127138598,
	62726078,
	203459146,
	462130400,
	345799647,
	]	

bulb_list_office_test_4 = [
	1648446928, 
	127138598,
	62726078,
	203459146,
	]	
	
bulb_list_office_test_2 = [
	462130400,
	345799647,
	]		

#********* USER CONFIGURATION REQUIRED END ***********

# ---> END: SITE SPECIFIC CONFIGURATION ##################################################

#COLOR LISTS

#Color Lists for Testing
color_list_mixed_test = [
	"RED",
	"red",
	"Green",
	"bLuE",
	"blue",
	"Rose",
	"spring green",
	"springgreen",
	"Blah",
	"00ffff#",
	"#00ff00",
	"#00ff00ff00"	
	"000ff00",
	"#00FF0",
	[0,0,255,0],
	[0,255,255],
	[500,-2,65],
	[0,255,127],
	"#0000ZZ",
	"#DA70D6",
	"#FF00FF",
	]

#RGB Color Wheel - Primary, Secondary & Tertiary Colors - https://www.1728.org/RGB.htm
color_list_rgb_primary = [
	"red",
	"lime",
	"blue",
	]

color_list_rgb_secondary = [
	"red",
	"yellow",
	"lime",
	"cyan",	
	"blue",
	"magenta",	
	]

	
color_list_rgb_tertiary = [
	"#FF0000",	#RED - Primary color
	"#FF7F00",	#ORANGE - Tertiary color
	"#FFFF00",	#YELLOW - Secondary color
	"#7FFF00",	#CHARTREUSE - Tertiary color
	"#00FF00",	#LIME - Primary color
	"#00FF7F",	#SPRING GREEN - Tertiary color
	"#00FFFF",	#CYAN (AQUA) - Secondary color
	"#007FFF",	#AZURE - Tertiary color
	"#0000FF",	#BLUE - Primary color
	"#7F00FF",	#VIOLET - Tertiary color
	"#FF00FF",	#MAGENTA (FUSCHIA) - Secondary color
	"#FF007F",	#ROSE / BRIGHT PINK - Tertiary color
	]


color_list_halloween_3 = [
	"orange",
	"purple",
	"lime",
	]	
