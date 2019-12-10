import RPi.GPIO as GPIO
import time

switches = {25: "01.mp3"}
lastPushedSwitch = False

def initSwitches():
	for i in switches:
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def readSwitches():
	global lastPushedSwitch
	for i in switches:
		if GPIO.input(i) == False and lastPushedSwitch != i:
			lastPushedSwitch = i
			return i
	return False


GPIO.setmode(GPIO.BCM)
initSwitches()

if __name__ == '__main__':
	print("main")	

	while True:

		switch = readSwitches()
		if switch != False:
			print(switch)
		
