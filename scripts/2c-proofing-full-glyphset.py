fontpath = 'Times New Roman'
margin = 50

fs = FormattedString(font=fontpath, fontSize=32, tracking=10, lineHeight=30)

glyphs = fs.listFontGlyphNames()
fs.appendGlyph(*glyphs)

while fs:
    newPage('A4')
    fs = textBox(fs, (margin, margin, width() - 2*margin, height() - 2*margin))
