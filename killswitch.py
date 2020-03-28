import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
KILLSWITCH = 15
GPIO.setup(KILLSWITCH, GPIO.IN)

def killswitch():
	if GPIO.input(KILLSWITCH) != GPIO.HIGH:
		print("shutdown")
		#os.system("sudo shutdown -h now")

def main():
	while True:
		killswitch()

if __name__ == "__main__":
	main()
