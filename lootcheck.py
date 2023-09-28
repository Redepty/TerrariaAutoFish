from fuzzywuzzy import fuzz


class LootCheck:

	def __init__(self):
		with open("loot.txt", "r") as file:
			self.lines = file.readlines()
			for i in range(len(self.lines)):
				if "\n" in self.lines[i]:
					self.lines[i] = self.lines[i][0:self.lines[i].find("\n")]

	def check(self, pcm6, pcm7):
		for i in self.lines:
			if (((fuzz.ratio(pcm6.lower(), i)) > 50 or (fuzz.ratio(pcm7.lower(), i)) > 50)
					or (i in pcm6.lower() or i in pcm7.lower())):
				print(f"{pcm7} is a {i}")
				return True
		return False
