import string

fontpath = 'Times New Roman'
margin = 50

txt = string.ascii_lowercase + string.ascii_uppercase + string.digits
fs = FormattedString(txt, font=fontpath, fontSize=60)

while fs:
    newPage('A4')
    fs = textBox(fs, (margin, margin, width() - 2*margin, height() - 2*margin))
