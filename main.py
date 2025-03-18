from DidHeShot import TheBallPasses
from SignalSending import GPIO_communication
import time

if __name__ == "__main__":
	print("You can play!")
	TheBallPasses()
	print("Next party")
	time.sleep(2)
	GPIO_communication()
	
