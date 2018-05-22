from lxml import etree
from requests import get
import re

url = "http://hpc.name/search.php?do=getdaily"
ans = get(url)

parser = etree.HTMLParser()
root = etree.fromstring(ans.text, parser)

box = []
temp = []

#Нужно учитывать, что сервер не разрешает слишком частые обращения
for i in root.iter("a"):
	
	#print(i, i.attrib)
	var = i.attrib.get("href")
	
	
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

	
def get_description(x): #на входе url
	ans = get("http://hpc.name/" + x).text
	ans = ans[ans.find("description")::]
	ans = ans[ans.find("content")+len("content")+3:ans.find("/>")-2:]
	return ans
	
	
def last_poster(x): #url на вход
	ans = get("http://hpc.name/" + x).text
	ans = ans[ans.find("Профиль")+8::]
	ans = ans[:ans.find("</")-4:]
	return ans
	
def get_author(x):
	ans = get("http://hpc.name/" + x).text
	ans = ans[ans.find("blank")+7::]
	ans = ans[:ans.find("</"):]
	return ans

def get_data(x):
	ans = get("http://hpc.name/" + x).text
	#print(x.split("#"))
	ans = ans[ans.rfind(x.split("#")[1])::]
	result = re.findall(r'\d{2}.\d{2}.\d{4}', ans)
	return result[0]



def go():
	result = []
	for i in box:
		temp = []
		temp.append(get_description(i[0]))
		temp.append("http://hpc.name/" + i[0])
		temp.append(get_data(i[2]))
		temp.append(last_poster(i[1]))
		temp.append(get_author(i[3]))
		result.append(temp)
		print(temp)
	return result

	










