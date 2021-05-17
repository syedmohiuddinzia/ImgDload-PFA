from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

# initializing substring
subs = '___________'

################################################################
################################################################
req1 = Request("https://www.___________.com/___________")
html_page = urlopen(req1)

soup = BeautifulSoup(html_page, "lxml")

links1 = []
for link in soup.findAll('a'):
    links1.append(link.get('href'))
#print(links1)
################################################################
################################################################
req2 = Request("https://www.___________.com/___________/page/2")
html_page = urlopen(req2)

soup = BeautifulSoup(html_page, "lxml")

links2 = []
for link in soup.findAll('a'):
    links2.append(link.get('href'))
#print(links2)
################################################################
################################################################
req3 = Request("https://www.___________.com/___________/page/3")
html_page = urlopen(req3)

soup = BeautifulSoup(html_page, "lxml")

links3 = []
for link in soup.findAll('a'):
    links3.append(link.get('href'))
#print(links3)
################################################################
################################################################
req4 = Request("https://www.___________.com/___________/page/4")
html_page = urlopen(req4)

soup = BeautifulSoup(html_page, "lxml")

links4 = []
for link in soup.findAll('a'):
    links4.append(link.get('href'))
#print(links4)
################################################################
################################################################
links = []
links.extend(links1)
links.extend(links2)
links.extend(links3)
links.extend(links4)
#print(links)
################################################################
################################################################
#print ("The original list is : " + str(links))
flink = [i for i in links if subs in i]
#print ("All strings with given substring are : " + str(flink))
################################################################
################################################################
#print ("The original list is : " + str(links))
subs = 'page'
rlink = [i for i in links if subs in i]
#print ("All strings with given substring are : " + str(rlink))
################################################################
################################################################
new = [k for k in flink if k not in rlink]
################################################################
################################################################
new1 = []
new1 = new
for x in range(len(new)) and range(len(new1)):
	#print(new[x])
        new1[x] = "https://www.___________.com" + new[x]
        print(new1[x])
################################################################
################################################################
textfile = open("f.txt", "w")
for element in new1:
    textfile.write(element + "\n")
textfile.close()
################################################################
################################################################
for y in range(len(new1)):
	req = Request(new1[y])
	html_page = urlopen(req3)

	soup = BeautifulSoup(html_page, "lxml")

	links = []
	for link in soup.findAll('a'):
	    links.append(link.get('href'))
print(links)
################################################################
################################################################
