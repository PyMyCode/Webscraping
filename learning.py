from bs4 import BeautifulSoup

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

print(soup)
print(type(soup))

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag)
print(tag.prettify())
print(tag.name) #b
print(tag.string) #Extremely bold


for tr in soup.find_all('tr'):
    print(tr.name)
    print(tr.text)
    print("")

#all links
for url in soup.find_all('a'):
	print(url.get('href'))
