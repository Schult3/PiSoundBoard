import RPi.GPIO as GPIO
import time
from soundplayer import SoundPlayer


switches = {25: {"filename": "01.mp3"}, 24: {"filename": "02.mp3"}, 23: {"filename": "03.mp3"} }

SoundFilePath = "/media/PiSoundBoard/"
lastPushedSwitch = False
player = False

def initSwitches():
	for i in switches:
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def readSwitches():
	global lastPushedSwitch
	for i in switches:
		if GPIO.input(i) == False and lastPushedSwitch != i:
			lastPushedSwitch = i
			return switches[i]["filename"]
	return False


GPIO.setmode(GPIO.BCM)
initSwitches()

if __name__ == '__main__':
	while True:
		if player != False and player.isPlaying() == False:
			lastPushedSwitch = False

		filename = readSwitches()
		if filename != False:
			player = SoundPlayer(SoundFilePath + filename, 0)
			player.play(1.0)
