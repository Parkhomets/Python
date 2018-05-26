import simplecrypt


with open("encrypted.bin", "rb") as al:
	encrypted = al.read()

with open("keys.txt", "r") as keys:
	for key in keys:
		print(key.strip())
		try:
			print(simplecrypt.decrypt(key.strip(), encrypted))
		except:
			pass
