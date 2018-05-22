from lxml import etree
from requests import get

url = "http://hpc.name/search.php?do=getdaily"
ans = get(url)

parser = etree.HTMLParser()
root = etree.fromstring(ans.text, parser)

box = []
temp = []
for i in root.iter("a"):
	
#	print(i, i.attrib)
	var = i.attrib.get("href")
	#print(i.attrib.get("href"))
	
	
	if "showthread" in var and "page" not in var and var not in temp:
		temp.append(var)
	elif "lastposter" in var:
		temp.append(var)
	elif "whoposted" in var:
		temp.append(var)
	
	if len(temp) == 4:
		box.append(temp)
		temp = []
	
	
	
for i in box:
	print(i)
	



