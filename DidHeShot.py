import RPi.GPIO as GPIO 
import time
from TakePicture import take_picture 
from AnalyzePicture import analyse_skittle

def TheBallPasses():    
    GPIO.setmode(GPIO.BCM)  #enable 
    GPIO_Ball_Pass = 18   #physical pin is 12

    GPIO.setwarnings(False)
    GPIO.setup(GPIO_Ball_Pass, GPIO.IN)
    
    i = 0 # number of shot done
    count_win=0 # deals with Strike and Spare

    try:
        while(i<2):
            State=True
            while State:
                count_win=0 # deals with Strike and Spare
                enter = GPIO.input(GPIO_Ball_Pass)     #pin 12 receive from TFMS5..0
                if enter == GPIO.HIGH:
                    time.sleep(4)
                    #take_picture()
                    print("photo")
                    i+=1
                    print("Picture ok!")
                    StateSkittle=analyse_skittle()

                    for element in StateSkittle:
                        if element==True:
                            count_win+=1
                            
                    if count_win==len(StateSkittle) and i==2:
                        print('Spare!')
                    elif count_win==len(StateSkittle) and i==1:
                        print('Strike!!!')
                    elif count_win != len(StateSkittle) and i==2:
                        print(len(StateSkittle))
                        print(count_win)
                        print(f'{len(StateSkittle)-count_win} skittle(s) remaining...')

                    State=False

    except KeyboardInterrupt:
        GPIO.cleanup()
    print("You can play!")
