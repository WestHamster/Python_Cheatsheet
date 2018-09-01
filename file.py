import sys
import cgi

print('Content-type: text/html\r\n\r\n')

html = """
<head>
<title>Data from file</title>
</head>
<body>
<center><h1>Data in File</h1></center>
<h4>%s</h4>
<h5><a href = "file2.py">Click Here to View Content of File</a></h5>
</body>"""

form = cgi.FieldStorage()

w = form['data'].value

try:
    fopen = open("New.txt","w")
    fopen.write(w)
except:
    print('Unexpected Error: '+sys.exc_info()[0])
    raise

print(html % w)
print('Successfully Created')
