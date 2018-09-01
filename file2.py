import sys

e = ' '
try:
    fopen = open("New.txt","r")
    for  i in fopen:
        e+=i
except:
    print('Error')


html = """Content-type: text/html\r\n\r\n
<head>
<title>Data in File</title>
</head>
<body>
<hr>
<center><h2>%s</h2></center>
<hr>
</body>"""

print(html % e)
