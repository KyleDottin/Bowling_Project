import RPi.GPIO as GPIO 
import time
from TakePicture import take_picture 
from AnalyzePicture import analyse_skittle

def TheBallPasses():    
    GPIO.setmode(GPIO.BCM)  #enable 
    GPIO_Ball_Pass = 18   #physical pin is 12

    GPIO.setwarnings(False)
    GPIO.setup(GPIO_Ball_Pass, GPIO.IN)
    
    i = 0               # number of shot done

    try:
        while(i<2):
            State=True
            while State:
                enter = GPIO.input(GPIO_Ball_Pass)     #pin 12 receive from TFMS5..0
                if enter == GPIO.HIGH:
                    time.sleep(4)
                    #take_picture()
                    print("photo")
                    i+=1
                    print("Picture ok!")
                    #analyse_skittle()
                    print("analyse")
                    State=False

    except KeyboardInterrupt:
        GPIO.cleanup()
    print("You can play!")
