print("""Content-type: text/html

<TITLE>Table</TITLE>
<H1>A Multiplication Table</H1>
<HR>
<P>Table of multiplication!</P>
<table border=1>
""")
    
for i in range(1,5):
    print('<tr>')
    for j in range(1,5):
        print('<td>%d*%d=%d</td>' % (i, j,i*j))
    print('</tr>')

print("""
</table>
<HR>
""")
