from ahk import AHK
from bot import Bot

ahk = AHK()

bot = Bot()

while True:
	if ahk.key_state("q"):
		bot.activate()
	bot.wait()
