from requests import put, get


class Crawler:
	def __init__(self,url, key):
		self.url = url
		self.key = key
		self.get = get(self.url).json()

	def checar():
		if self.key in self.get:
			print("sucesso")
		else:
			print("Falha")

if __name__ == "__main__":
	crawler = Crawler("http://google.com", "google")
	crawler.checar()
