import requests, json
#kukareku228 123456789

#s = requests.get("http://hpc.name/search.php?do=getdaily", auth=("kukareku228", "123456789"))
#print(s.text)


def auth():
	s = requests.Session()
	#s.verify = "cacert.der"
	r = s.post("https://hpc.name/login.php?do=login", auth=("kukareku228", "25f9e794323b453885f5181f1b624d0b"), verify = False)
	#print(r.text)
	r = s.get("http://hpc.name/search.php?do=getdaily")
	print(r.text)
	#res = s.get("http://hpc.name/search.php?do=getdaily")
	#print(res.text)
	#print(res.text)
	#print(res.headers)
	
	
	
	'''
	logindata = {'username': 'kukareku228', 'password': '123456789'}
	api_url = "http://hpc.name/search.php?do=getdaily"
	
	
	
	
	with requests.Session() as s:
		s.headers = {'User-Agent': 'Mozilla/5.0'}
		s.post(api_url, data=json.dumps(logindata))
		print (s.headers)
		# An authorised request.
		r = s.get(api_url)
		print(r.text)'''
auth()
