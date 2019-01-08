# RolandCNC_Python
Roland Modela MDX-15/20 - CNC Machine Python

I rediscovered a Roland Modela MDX-15 in my attic. Apparently (after some Google searching) more people
have them collecting dust because the Roland software for it is from the last century (literally) and
another problem is that most modern computers don't have a 25-pin serial interface anymore.

Fortunately some other Johan guy found a way to connect an FTDI board directly to the main IC on the mainboard
of the MDX:
http://vonkonow.com/wordpress/2012/08/bringing-a-12-year-old-roland-mdx-20-up-to-date/

Step 0. Solder FTDI (e.g. the breakout version from Sparkfun) to the Modela mainboard.

I want to control the machine using Python so the next step is to fix that:

Step 1. Install pylibftdi for Python(3)

Alas I ran into some library problem:

File "listFTDI.py", line 24, in <module>
    from pylibftdi import Driver
ImportError: No module named pylibftdi

It seems PyFtdi is also needed to get rid of this problem.

Step 1b. Insgall PyFtdi, see: http://eblot.github.io/pyftdi/installation.html

Running listFTDI.py gives me:
mbp-johan:batch jakorten$ python3 listFTDI.py
FTDI:FT232R USB UART:A700eYoJ
