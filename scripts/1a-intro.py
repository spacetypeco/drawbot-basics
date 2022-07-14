# This example showcases:
# * How python works (line-by-line execution, comments, python / drawbot syntax, variables, reading documentation, debugging)
# * Preview page zoom (cmd+, cmd-)

#
# Drawbot is a Python library for creating 2D, ready-to-print graphics.
# Each line of code in this file is run sequentially from top to bottom.
#
# Lines starting with a '#' character are interpreted as comments. They are not run
# by the computer, but they allow us to make notes within our program.
#
# We can create a new graphics page using the newPage function provided by DrawBot.
# This works with a specific page size, like 'A4' or 'A4Landscape'.
#
# Here, we're calling the "newPage" function and giving it parameters.
newPage('A4')

# Values like 0 or 100 can be assigned to any variable name, like x or y.
x = 0
y = 0
w = 100
h = 100

# https://drawbot.com/content/shapes/primitives.html
rect(x, y, w, h)