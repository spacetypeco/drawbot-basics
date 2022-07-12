# This example showcases:
# * Drawing text in a textbox with margin
# * Drawing overflow in additional pages

# the exported font we are using, OTF or TTF
# this can be a path like /path/to/MyFont.otf
# you can drag a font onto the text window to get the path
# OR this can also be the exact name of an installed font
fontpath = 'Verdana'
margin = 50

defaultText = "babe dace cede adead ebbed deeded dead cace cabaa bedead be be bebed baba deedeed deedeed abada decade be be deedeed abed be bedad be cab ebb ace be dab aced add bee acceded abed baba a cab aced bee cabda be decad be dada cadded baccae add a cecca acceded aced bee aced bacca deedeed dab abed deb cadded cad abed bebed acceded decede cadee decade be bed dad aced cabaa aced baba bacca add deeded be cab acceded acceded bee add deed bebed dab cace caeca deb abaca dad beaded be dace deedeed be cab added baaed decade be cabbed cadee dace abed bead be caeca be baaed bad ebb be deedeed babe deed a dec aced dab deedeed abede bade cace bed decd cadee bedad be deedeed cabbed dace abed babe cad decade be be a cadded baccae ceded dab dace deedeed decd acceded added be be cabaa bedead acceded dad cabda cace abede bead a beebee cace dabba a deedeed bebed baba dead bead dab caaba cabbed cab dabbed cab be be dec be bad be deed bead bedad beebee cadee decd acceded cace dec bee babe acceded bead dead bee dab deed decad be ace aced accede dada be abede be be bad cab deedeed ace deed adead accede deb deedeed bebed aced beebee"


Variable([
    dict(name="txt", ui="EditText", args=dict(text=defaultText)),
], globals())

fs = FormattedString(txt, font=fontpath, fontSize=32)

while fs:
    newPage('A4')
    fs = textBox(fs, (margin, margin, width() - 2*margin, height() - 2*margin))
