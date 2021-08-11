#This program lets us open google maps and take address as input either from command line or clipboard.
#This highlight module webbrowser which opens web page and pyperclip which copies text from clipboard

import pyperclip
import sys
import webbrowser

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste

webbrowser.open("https://www.google.com/maps/place/" + str(address))

