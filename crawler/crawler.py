from requests import put, get


class Crawler:
	def __init__(self,url, key):
		self.url = url
		self.key = key
		self.get = get(self.url).json()

	def imprime():
		print(self.get)

if __name__ == "__main__":
	crawler = Crawler()
	crawler.imprime()
