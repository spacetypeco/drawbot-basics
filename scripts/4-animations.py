fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

page = 0

while page < 30:
    page = page + 1
    newPage(500, 500)
    
    fs = FormattedString("H", font=fontpath, fontSize=400, align="center", fontVariations={'wdth': page*10})
    path = BezierPath()
    path.text(fs, (width() / 2, height() / 4))
    drawPath(path)
    
saveImage("5-animations.mp4")