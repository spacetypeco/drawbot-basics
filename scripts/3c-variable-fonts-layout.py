# This example showcases a sketch generated using variable font attributes.
#
fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

newPage('A4')

y = 0

while y < height():
    fs = FormattedString(
        "ABCDEFGH", 
        font=fontpath, 
        fontSize=100, 
        align="center", 
        fontVariations=dict(wdth = y / 4),
        fill=(y/height(), 0, 1 - y/height())
    )
    
    textWidth, textHeight = textSize(fs, width=width())
    
    if y + textHeight < height():
      text(fs, (width() / 2, y))
    
    y = y + textHeight
    