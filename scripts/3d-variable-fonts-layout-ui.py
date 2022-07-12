# This example showcases a sketch generated using variable font attributes.
#
fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

Variable([
    dict(name="scale", ui="Slider", args=dict(value=4, minValue=1, maxValue=10))
], globals())

newPage('A4')
y = 0

while y < height():
    fs = FormattedString(
        "ABCDEFGH", 
        font=fontpath, 
        fontSize=100, 
        align="center", 
        fontVariations={'wdth': y / scale},
        fill=(y/height(), 0, 1 - y/height())
    )
    
    textWidth, textHeight = textSize(fs, width=width())
    
    if y + textHeight < height():
      text(fs, (width() / 2, y))
    
    y = y + textHeight
    