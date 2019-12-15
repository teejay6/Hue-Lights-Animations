Hue Lights Animation Scripts in Python for Indigo Domotics

These files are a set of python scripts to animate Philips Hue Lights within the Indigo Domotics framework on the Mac. They use the Hue Lights plugin from Nathan Sheldon Software.

I am currently using 6 Hue LED Color Light Strips for Christmas lights that are installed under the eaves of my roof, but you can modify the script to include any Color Hue light. The script animates the lights so they can change color, create a rainbow, chase, fill, and any other animation you can think of (and reproduce in a list comprehension).


CONFIGURATION:
Site Package Configuration File 2: color_animation_utils.py

 - Add to : /Library/Python/2.7/site-packages/

Animation File 1: Xmas 1.0 - 2019 Animations with List Comprehensions.py

 - Modify the Site Specific Configuration section at the top to define the lists of your bulbs and the device numbers.
 - Include this file in an Indigo Action Group as an “Execute Script (Script and File Actions)”. 
 - Add an Indigo Schedule for Sunset to Execute the Action Group. 


INTRODUCTION:
The way the animations work is that the files and algorithms create a series of lists that are sent to the hue lights via Indigo. These lists include:

1.  Site Package Configuration (color_animation_utils.py):

1.1 The bulb list (or lists) with the device numbers of your local bulbs. 

1.2 Standard Color Lists are also included here as I tend to use the same color lists in every animation. Note that the animations use RGB values to represent colors. You can use color names like Red, hex values like #FF0000, or lists like [255,0,0] to define the colors. You can mix any of these formats in the color lists. There is a function in the animation file that provides error checking, and converts the valid values to RGB.

2. Animation (Xmas 1.0 - 2019 Animations with List Comprehensions.py)

2.1 The program contains all of the functions, list definitions, and list comprehensions required for the hue bulb animations

2.2 The print functions define time stamps and delays. The time stamps allow the user to estimate how long the animation sequences will take to run. Every animation has a ramp rate and delay variable to define how long it takes the bulb to change color, and how long the bulb stays that color until the next animation sequence. 

2.3 The main functions convert the color lists to RGB values, and then set the individual bulbs with the individual RGB colors.

2.4 The program is verbose for error checking, and also to explain how the list comprehension algorithms create the lists. Using these examples, you can create other animations.

2.5 Lists in Python can be added, multiplied, and nested, so you can create some pretty elaborate animation sequences.

2.6 The files should be able to used as is, as long as you change the bulb device numbers and the bulb name lists. I have identified the user configuration variables that are required with the following code comments:

#********* USER CONFIGURATION REQUIRED START *********

#********* USER CONFIGURATION REQUIRED END ***********

2.7 Good luck and Happy Holidays. 
