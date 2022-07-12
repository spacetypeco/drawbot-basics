fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

page = 0

while page < 30:
    page = page + 1
    newPage(500, 500)
    
    fs = FormattedString("H", font=fontpath, fontSize=400, align="center")
    path = BezierPath()
    path.text(fs, (width() / 2, height() / 4))
    expandedPath = path.expandStroke(page)
    drawPath(expandedPath)
    
saveImage("6a-stroke-animation.gif")