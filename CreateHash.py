
# Importing the hashlib library
def generateHash(data):
	import hashlib
	hash_value = hashlib.md5(data.encode()).hexdigest()
	print(hash_value)
	return hash_value

