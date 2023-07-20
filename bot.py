import time
import cv2
import mss
import numpy as np
import pytesseract
from ahk import AHK
from fuzzywuzzy import fuzz
from utils import queryMousePosition

ahk = AHK()


class Bot:
	def __init__(self):
		print("Press q to activate bot!")
		self.title = "Terraria AutoFish bot"
		self.drink_time = 999999999999999999999999
		self.sct = mss.mss()
		self.active = False

	def click(self):
		ahk.click()

	def activate(self):
		self.active = not self.active
		if self.active:
			self.click()
			self.drink()
			print("Bot is activated, enjoy!")
		else:
			print("Bot is deactivated, be free!")
		time.sleep(1)

	def catch(self):
		print("Catch!")
		self.click()

		time.sleep(1)

		print("New rod Dropped!")
		self.click()
		self.click()

	def drink(self):
		ahk.key_down('b')
		time.sleep(0.05)
		ahk.key_up('b')
		self.drink_time = time.time()+2

	def show(self, title, img):
		cv2.imshow(title, img)
		if cv2.waitKey(25) & 0xFF == ord("`"):
			cv2.destroyAllWindows()
			quit()

	def wait(self):
		if self.active:
			if time.time() >= self.drink_time:
				self.drink()

			cur = queryMousePosition()
			mon = {"left": cur['x'] - 200,
				"top": cur['y'] - 75,
				"width": 400,
				"height": 50}
			img = np.asarray(self.sct.grab(mon))

			rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			pcm6 = pytesseract.image_to_string(rgb, lang='eng', config='--psm 6')
			pcm7 = pytesseract.image_to_string(rgb, lang='eng', config='--psm 7')

			self.show(self.title, img)

			if (((fuzz.ratio(pcm6.lower(), 'crate')) > 50 or (fuzz.ratio(pcm7.lower(), 'crate')) > 50)
			or ('crate' in pcm6.lower() or 'crate' in pcm7.lower())):
				print(f"{pcm6} is a crate ")
				self.catch()

			else:
				pass
				print("it's not a crate")
