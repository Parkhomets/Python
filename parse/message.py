from main import *
'''
from lxml import etree
from requests import get
import re, csv, time
'''

url = "http://hpc.name/search.php?do=getdaily"
ans = get(url)
parser = etree.HTMLParser()
root = etree.fromstring(ans.text, parser)

box = []
temp = []


#Нужно учитывать, что сервер не разрешает слишком частые обращения
for i in root.iter("a"):
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
		
# 1 - ссылка на пост
# 2 - последнее сообщение
# 3 - дата последнего
#
#

'''
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
	

def get_data(x):
	ans = get("http://hpc.name/" + x).text
	ans = ans[ans.rfind(x.split("#")[1])::]
	result = re.findall(r'\d{2}.\d{2}.\d{4}', ans)
	return result[0]
'''
def get_text(x):                        #сообщение достаем по споследнему посту
	ans = get("http://hpc.name/" + x).text
	ans = ans[ans.rfind(x.split("#")[1])::]
	ans = ans[ans.find("post_message_")+26::]
	ans = ans[:ans.find("</div>")-3:].replace("<br />", "")
	ans = ans.replace("<b>", "")
	ans = ans.replace("\n", "")
	ans = ans.replace("</b>", "")
	ans = ans.replace("\r", "")
	ans = ans.replace("</a>", "")
	ans = ans.replace("<a href=", "")
	return ans
'''
for i in box:
	print(i)
'''
#print(get_text("showthread.php?t=59974&p=505779#post505779"))
def go():
	result = []
	for i in box:
		temp = []
		temp.append(get_data(i[2]))
		temp.append(last_poster(i[1]))
		temp.append("http://hpc.name/" + i[1])
		temp.append(get_description(i[0]))
		temp.append("http://hpc.name/" + i[0])
		temp.append(get_text(i[2]))
		result.append(temp)
		print(temp)
	return result


go()
'''

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
while True:
	temp = go()
	log(temp)
	csv_writer(temp, "output.csv")
	time.sleep(60)
'''

