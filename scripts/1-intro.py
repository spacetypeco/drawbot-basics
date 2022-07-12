# This example showcases:
# * How python works (line-by-line execution, comments, indentation, python / drawbot syntax, variables, reading documentation, debugging)
# * Preview page zoom (cmd+, cmd-)


# 1 - shapes and colors
newPage('A4')

fill(1, 0, 0)
rect(0, 0, 100, 100)

fill(0, 1, 0)
rect(100, 100, 100, 100)

fill(0, 0, 1)
rect(200, 200, 100, 100)

fill(0)

stroke(1, 0, 0)
strokeWidth(5)
oval(300, 300, 100, 100)

stroke(0, 1, 0)
strokeWidth(2)
lineDash(20, 10, 10, 10)
oval(400, 400, 100, 100)

stroke(0, 0, 1)
lineDash(None)
oval(500, 500, 100, 100)

# 2 - randomness and page attributes

newPage('A4')

fill(random(), random(), random())
rect(0, 0, width(), height())

# 3 - variables

newPage('A4')

margin = 50
rect(margin, margin, width() - 2*margin, height() - 2*margin)