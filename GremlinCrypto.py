def encrypt_Vigenere():
	print("Будте внимательны, функция шифровки не учтывает символы переноса строки")
	x = input("Введите строку: ").upper()
	key = input("Введите ключ: ").upper()
	eng  = ["A", "B", "C", "D", "E", "F",
			"G", "H", "I", "J", "K", "L",
			"M", "N", "O", "P", "Q", "R",
			"S", "T", "U", "V", "W", "X",
			"Y", "Z"]
	symbols = ["~","!","@","#","$","%",
			   "^","&","*","(",")","-",
			   "_","=", "+","``",",",".",
			   "?","/",":",";","\'","\"",
			   "[","]", "{", "}", "№", " ",
			   "0","1","2","3","4","5","6",
			   "7","8", "9"]
	rus = ["Й","Ф","Я","Ц","Ы","Ч","У",
		   "В","С","К","А","М","Е","И",
		   "Н","Т","Г","О","Ш","Л","Б",
		   "Щ","Д","Ю","З","Ж","Х","Э",
		   "Ё","П","Р","Ь","Ъ"]
	rus_lang = True
	eng_lang = True
	for i in x:
		if i not in eng and i not in symbols:
			eng_lang = False
			break
	for i in x:
		if i not in rus and i not in symbols:
			rus_lang = False
			break
	for i in key:
		if i not in eng:
			eng_lang = False
			break
	for i in key:
		if i not in rus:
			rus_lang = False
			break
	if (rus_lang == False and eng_lang == False):
		print("Невозможно применить данный алгоритм из-за непредвиденных символов")
		print("Это может быть связано с неправильностью ключа")
		print("Или нахождением букв другого алфавита в строке")
		return

	if (eng_lang):
		encrypt_Vigenere_eng(x, key)
	elif rus_lang:
		encrypt_Vigenere_rus(x, key)
def decrypt_Vigenere():
	print("Будте внимательны, функция дешифровки не учтывает символы переноса строки")
	x = input("Введите строку: ").upper()
	key = input("Введите ключ: ").upper()
	eng  = ["A", "B", "C", "D", "E", "F",
			"G", "H", "I", "J", "K", "L",
			"M", "N", "O", "P", "Q", "R",
			"S", "T", "U", "V", "W", "X",
			"Y", "Z"]
	symbols = ["~","!","@","#","$","%",
			   "^","&","*","(",")","-",
			   "_","=", "+","``",",",".",
			   "?","/",":",";","\'","\"",
			   "[","]", "{", "}", "№", " ",
			   "0","1","2","3","4","5","6",
			   "7","8", "9"]
	rus = ["Й","Ф","Я","Ц","Ы","Ч","У",
		   "В","С","К","А","М","Е","И",
		   "Н","Т","Г","О","Ш","Л","Б",
		   "Щ","Д","Ю","З","Ж","Х","Э",
		   "Ё","П","Р","Ь","Ъ"]
	rus_lang = True
	eng_lang = True
	for i in x:
		if i not in eng and i not in symbols:
			eng_lang = False
			break
	for i in x:
		if i not in rus and i not in symbols:
			rus_lang = False
			break
	for i in key:
		if i not in eng:
			eng_lang = False
			break
	for i in key:
		if i not in rus:
			rus_lang = False
			break
	if (rus_lang == False and eng_lang == False):
		print("Невозможно применить данный алгоритм из-за непредвиденных символов")
		print("Это может быть связано с неправильностью ключа")
		print("Или нахождением букв другого алфавита в строке")
		return

	if (eng_lang):
		decrypt_Vigenere_eng(x, key)
	elif rus_lang:
		decrypt_Vigenere_rus(x, key)
def encrypt_Vigenere_eng(crypted, kkey):
	x = crypted
	spaces = []
	symbols = []
	alpha = ["A", "B", "C", "D", "E", "F",
			 "G", "H", "I", "J", "K", "L",
			 "M", "N", "O", "P", "Q", "R",
			 "S", "T", "U", "V", "W", "X",
			 "Y", "Z"]
	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y
	text = ''
	for i in x:
		text += i
	key = kkey
	var = ''
	i = 0
	while i < len(text):
		var += key[i % len(key)]
		i += 1
	key = var
	res = []
	i = 0
	while i < len(text):
		res.append(alpha[(alpha.index(text[i]) + alpha.index(key[i])) % 26])
		i += 1
	for i in range(0, len(spaces)):
		res.insert(spaces[i], symbols[i])
	res = "".join(res)
	print(res)
def encrypt_Vigenere_rus(crypted, kkey):
	print("Будте внимательны, функция шифровки не учтывает символы переноса строки")
	x = crypted
	spaces = []
	symbols = []
	alpha = ["А", "Б", "В", "Г", "Д", "Е","Ё",
	 		 "Ж", "З", "И", "Й", "К", "Л", "М",
			  "Н", "О", "П", "Р", "С", "Т", "У",
			   "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ",
			    "Ы", "Ь", "Э", "Ю", "Я"]

	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y
	text = ''
	for i in x:
		text += i
	key = kkey
	var = ''
	i = 0
	while i < len(text):
		var += key[i % len(key)]
		i += 1
	key = var
	res = []
	i = 0
	while i < len(text):
		res.append(alpha[(alpha.index(text[i]) + alpha.index(key[i])) % 33])
		i += 1
	for i in range(0, len(spaces)):
		res.insert(spaces[i], symbols[i])
	res = "".join(res)
	print(res)
def decrypt_Vigenere_eng(crypted, kkey):
	alpha = ["A", "B", "C", "D", "E", "F",
		 	"G", "H", "I", "J", "K", "L",
			 "M", "N", "O", "P", "Q", "R",
			 "S", "T", "U", "V", "W", "X",
			 "Y", "Z"]
	symbols = []
	spaces = []
	x = crypted
	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y



	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	#x = x.split()
	text = "".join(x)
	key = kkey
	i = 0
	var = ''
	while i < len(text):
			var += key[i % len(key)]
			i += 1
	key = var
	def Vigenere(text):
		res = []
		i = 0
		while i < len(text):
			res.append(alpha[(alpha.index(text[i]) + alpha.index(key[i])) % 26])
			i += 1
		text = "".join(res)
		#print(text) выводит все переборы
		return text
	for i in range(0, 25):
		text = Vigenere(text)
	res = []
	for i in text:
		res.append(i)
	for i in range(0, len(spaces)):
		res.insert(spaces[i], symbols[i])
	res = "".join(res)
	text = "".join(res)
	print(text)
def decrypt_Vigenere_rus(crypted, kkey):
	alpha = ["А", "Б", "В", "Г", "Д", "Е","Ё",
		 	 "Ж", "З", "И", "Й", "К", "Л", "М",
			 "Н", "О", "П", "Р", "С", "Т", "У",
			 "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ",
			 "Ы", "Ь", "Э", "Ю", "Я"]
	symbols = []
	spaces = []
	x = crypted
	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y



	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	#x = x.split()
	text = "".join(x)
	key = kkey
	i = 0
	var = ''
	while i < len(text):
			var += key[i % len(key)]
			i += 1
	key = var
	def Vigenere(text):
		res = []
		i = 0
		while i < len(text):
			res.append(alpha[(alpha.index(text[i]) + alpha.index(key[i])) % 33])
			i += 1
		text = "".join(res)
		#print(text) выводит все переборы
		return text
	for i in range(0, 32):
		text = Vigenere(text)
	res = []
	for i in text:
		res.append(i)
	for i in range(0, len(spaces)):
		res.insert(spaces[i], symbols[i])
	res = "".join(res)
	text = "".join(res)
	print(text)
	
	
	
def Caesar():
	eng  = ["A", "B", "C", "D", "E", "F",
			"G", "H", "I", "J", "K", "L",
			"M", "N", "O", "P", "Q", "R",
			"S", "T", "U", "V", "W", "X",
			"Y", "Z"]
	symbols = ["~","!","@","#","$","%",
			   "^","&","*","(",")","-",
			   "_","=", "+","``",",",".",
			   "?","/",":",";","\'","\"",
			   "[","]", "{", "}", "№", " ",
			   "0","1","2","3","4","5","6",
			   "7","8", "9"]
	rus = ["Й","Ф","Я","Ц","Ы","Ч","У",
		   "В","С","К","А","М","Е","И",
		   "Н","Т","Г","О","Ш","Л","Б",
		   "Щ","Д","Ю","З","Ж","Х","Э",
		   "Ё","П","Р","Ь","Ъ"]
		   
	x = input().upper()
	rus_lang = True
	eng_lang = True
	for i in x:
		if i not in eng and i not in symbols:
			eng_lang = False
			break
	for i in x:
		if i not in rus and i not in symbols:
			rus_lang = False
			break
	
	if (rus_lang == False and eng_lang == False):
		print("Невозможно применить данный алгоритм из-за непредвиденных символов")
		print("Это может быть связано с неправильностью ключа")
		print("Или нахождением букв другого алфавита в строке")
		return
		
	if (eng_lang):
		Caesar_eng(x)
	elif rus_lang:
		Caesar_rus(x)
		
def Caesar_eng(text):
	x = text
	spaces = []
	symbols = []
	alpha = ["A", "B", "C", "D", "E", "F",
			 "G", "H", "I", "J", "K", "L",
			 "M", "N", "O", "P", "Q", "R",
			 "S", "T", "U", "V", "W", "X",
			 "Y", "Z"]
	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y
	for i in range(0, 26):
		var = []
		strin = ''
		for j in x:
			var.append(alpha[(alpha.index(j) + i) % 26])
		
		for l in range(0, len(spaces)):
			var.insert(spaces[l], symbols[l])
		res = ''.join(var)
		if i < 10:
			print(i, " : ", res)
		else:
			print(i, ": ", res)
def Caesar_rus(text):
	x = text
	spaces = []
	symbols = []
	alpha = ["А", "Б", "В", "Г", "Д", "Е","Ё",
		 	 "Ж", "З", "И", "Й", "К", "Л", "М",
			 "Н", "О", "П", "Р", "С", "Т", "У",
			 "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ",
			 "Ы", "Ь", "Э", "Ю", "Я"]
	for i in range(0, len(x)):
		if x[i] not in alpha:
			spaces.append(i)
			symbols.append(x[i])
	y = ""
	for i in x:
		if i in alpha:
			y += i
	x = y
	for i in range(0, 33):
		var = []
		strin = ''
		for j in x:
			var.append(alpha[(alpha.index(j) + i) % 33])
		
		for l in range(0, len(spaces)):
			var.insert(spaces[l], symbols[l])
		res = ''.join(var)
		if i < 10:
			print(i, " : ", res)
		else:
			print(i, ": ", res)
