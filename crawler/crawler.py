from requests import put, get


class crawler:
	def __init__(self,url, key):
		self.url = url
		self.key = key
		self.put = get(self.url).json()

	def imprime():
		print(self.put)

if __name__ == "__main__":
	pass
