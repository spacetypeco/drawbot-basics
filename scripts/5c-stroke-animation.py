fontpath = 'Verdana'

page = 0

while page < 300:
    page = page + 1
    newPage(500, 500)
    frameDuration(1/30)
    
    fs = FormattedString("H", font=fontpath, fontSize=400, align="center")
    path = BezierPath()
    path.text(fs, (width() / 2, height() / 4))
    
    # Draw 20 concentric outlines for each page
    for i in range(20):
        fill(None)
        
        # Draw a thick stroke
        stroke(0)
        strokeWidth(page - i*10)
        drawPath(path)
    
        # Draw a thinner, white stroke to erase 
        # the inner lining of the previous stroke
        stroke(1)
        strokeWidth(page - i*10 - 5)
        drawPath(path)
    
saveImage("5c-stroke-animation.mp4")