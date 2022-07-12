# This example showcases a sketch generated using variable font attributes.
#
fontpath = '/Users/kyeah/Downloads/FitVariable-VF.ttf'

Variable([
    dict(name="txt", ui="EditText", args=dict(text="ABCDEFGH")),
    dict(name="wdth", ui="Slider", args=dict(value=200, minValue=1, maxValue=900))
], globals())

newPage('A4Landscape')

fs = FormattedString(
  txt,
  font=fontpath, 
  fontSize=100, 
  align="center", 
  fontVariations=dict(wdth = wdth),
)

textWidth, textHeight = textSize(fs, width=width())

text(fs, (width() / 2, height() / 2 - textHeight/2))