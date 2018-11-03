import bs4 as bs
import urllib.request
import requests

source = urllib.request.urlopen("https://data-lessons.github.io/library-webscraping-DEPRECATED/02-csssel/")
#response = requests.get(source,timeout = 5)
soup = bs.BeautifulSoup(source,'lxml')   #OR  content = BeautifulSoup(response.content,"html.parser")

nav = soup.nav

for url in nav.find_all('a'):
	print(url.get('href'))
print()

for div in soup.find_all('div',class_='p'):
	print(div.text)

############################################
#For table reading
############################################

source1 = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup1=bs.BeautifulSoup(source1,'lxml')

table = soup1.table	#OR  table = soup.find("table")

print(table)
print()
print()
table_rows = table.find_all("tr")
for tr in table_rows:
	td=tr.find_all("td")
	row = [i.text for i in td]
	print(row)
print()
print()

###########################################
#For XML parsing
###########################################

source2 = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
soup2=bs.BeautifulSoup(source2,'xml')

for url2 in soup2.find_all('loc'):
	print(url2.text)

print()
print()
##########################################
#For Dynamic Data / Javascript
########################################## 

source3=urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup3 = bs.BeautifulSoup(source3,'lxml')

js_test = soup3.find('p',class_='jstest')
print(js_test.text)

print()
print()
##########################################
#TEST ON RANDOM SITE - DON'T DO IT WITHOUT PERMISSION
#########################################
source4= urllib.request.urlopen("http://thesolarlabs.com/").read()
soup4 = bs.BeautifulSoup(source4,'lxml')

for div in soup4.find_all('div',class_='container'):
	print(div.text)