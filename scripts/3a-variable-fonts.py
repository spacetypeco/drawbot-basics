# This example showcases a sketch generated using variable font attributes.
#
fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

newPage('A4Landscape')

fs = FormattedString(
  "ABCDEFGH", 
  font=fontpath, 
  fontSize=100, 
  align="center", 
  fontVariations=dict(wdth = 300),
)
  
textWidth, textHeight = textSize(fs)

text(fs, (width() / 2, height() / 2 - textHeight/2))