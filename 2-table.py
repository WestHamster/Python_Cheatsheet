print("""Content-type: text/html

<TITLE>CGI 101</TITLE>
<H1>A Third CGI Script</H1>
<HR>
<P>Hello, CGI World!</P>
<table border=1>
""")
    
for i in range(10):
    print('<tr>')
    print('<td>%d*%d = %d</td>' % (2,i+1,2*(i+1)))
    print('</tr>')

print("""
</table>
<HR>
""")
