import RPi.GPIO as GPIO
import time
from shutil import copyfile
import os
from soundplayer import SoundPlayer


switches = {25: {"filename": "01.mp3"}, 24: {"filename": "02.mp3"}, 23: {"filename": "03.mp3"}, 4: {"filename": "04.mp3"}, 17: {"filename": "05.mp3"}, 27: {"filename": "06.mp3"} }

SoundFilePath = "/home/pi/soundfiles/"
lastPushedSwitch = False
player = False

def initSwitches():
	for i in switches:
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def copyMediaFiles():
	if len(os.listdir('/media/PiSoundBoard')) > 0:
		os.system("sudo rm /home/pi/soundfiles/*")
		os.system("sudo cp -R /media/PiSoundBoard/*.mp3 /home/pi/soundfiles")


def readSwitches():
	global lastPushedSwitch
	for i in switches:
		if GPIO.input(i) == False and lastPushedSwitch != i:
			lastPushedSwitch = i
			return switches[i]["filename"]
	return False


GPIO.setmode(GPIO.BCM)
initSwitches()
copyMediaFiles()

if __name__ == '__main__':
	while True:
		if player != False and player.isPlaying() == False:
			lastPushedSwitch = False

		filename = readSwitches()
		if filename != False and os.path.isfile(SoundFilePath + filename):
			player = SoundPlayer(SoundFilePath + filename, 0)
			player.play(1.0)
