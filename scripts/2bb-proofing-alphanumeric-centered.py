import string

newPage('A4Landscape')

x = 0
y = 0
w = width()
h = height()

txt = FormattedString(
    string.ascii_uppercase + string.ascii_lowercase + string.digits, 
    fontSize=60, 
    align="center"
)

tw, th = textSize(txt, width=width() - 200)

x = width() / 2 - tw/2
y = height() / 2 - th/2
textBox(txt, (x, y, tw, th))