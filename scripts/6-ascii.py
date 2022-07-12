import string

font = "Verdana"
margin = 50

Variable([
    dict(name="pointSize", ui="Slider", args=dict(value=3, minValue=1, maxValue=5))
], globals())

newPage('A4')
path = BezierPath()
path.textBox(
    string.ascii_uppercase + string.digits, 
    (margin, margin, width() - 2*margin, height() - 2*margin), 
    font=font, 
    fontSize=100, 
    align="center"
)

for x in range(0, width(), 5):
    for y in range(0, height(), 5):
        if path.pointInside((x, y)):
            fill(random())
            oval(x, y, pointSize, pointSize)