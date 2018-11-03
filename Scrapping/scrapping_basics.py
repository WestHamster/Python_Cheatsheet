import bs4 as bs
import urllib.request

p=[]
source = urllib.request.urlopen('https://data-lessons.github.io/library-webscraping-DEPRECATED/02-csssel/').read()

soup = bs.BeautifulSoup(source,'lxml')

print(soup.title)
print()
print()
print(soup.title.name)
print()
print()
print(soup.title.string)	#TO RETRIEVE THE TITLE ELEMENT
print()
print()
print(soup.title.parent.name) #TO RETRIEVE THE PARENT ELEMENT
print()
print()
print(soup.p)
print()
print()
for para in soup.find_all('p'):
	print(para.string)
	print(str(para.text))
	#if(str(para.text)=="programming"):
	#	print(str(para.text))
print()
print()
for anchor in soup.find_all('a'):
	print(anchor.get('href'))		#TO RETRIEVE THE ANCHOR ELEMENTS
print()
print()
print(soup.get_text())	#RETRIEVE THE WHOLE WEB-PAGE text material