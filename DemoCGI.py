print('Content-type: text/html\r\n\r\n')

print('<html>')
print('<head>')
print('<title>File Handling Using CGI</title>')
print('</head>')
print('<body>')
print('<form action = "file.py" method = "post">')
print('<b>Enter the Data for File</b> <br>')
print('<textarea height = "350" width = "350" name = "data"></textarea> <br>')
print('<input type = "submit" value = "Submit" name = "button">')
print('</body>')
print('</html>')
