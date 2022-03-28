import bs4 as bs
import urllib.request

#parsing
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

#creating soup
soup = bs.BeautifulSoup(source,'html.parser')


#interating through all tags paragraphs
for p in soup.find_all('p'):
    print(p.name)
    print(p.string)
    print(p.text)
    print("")
#info from table
for tr in soup.find_all('tr'):
    print(tr.name)
    print(tr.text)
    print("")

#all links
for url in soup.find_all('a'):
	print(url.get('href'))


#grab all text
print(soup.get_text())
