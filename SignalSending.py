import RPi.GPIO as GPIO
import time

def GPIO_communication():
    GPIO.setmode(GPIO.BCM)
    GPIO_Send_PIN = 17           # GPIO physical pin 11
    GPIO_Receive_PIN = 27        # GPIO physical pin 13
    State = False;

    GPIO.setwarnings(False)
    GPIO.setup(GPIO_Send_PIN, GPIO.OUT)
    GPIO.setup(GPIO_Receive_PIN, GPIO.IN)
    

    try:
        print("The platform should move soon!")
        twice=0
        while twice<3:
            GPIO.output(GPIO_Send_PIN, GPIO.HIGH)  # Sent High on PA7 with pin 11
            State = True;
            time.sleep(1)
            print("The signal is turned off.")    
            GPIO.output(GPIO_Send_PIN, GPIO.LOW)  # Sent a Low signal
            twice+=1

        while State:
            signal = GPIO.input(GPIO_Receive_PIN)   # Receive on pin 13 from PA
            if signal == GPIO.HIGH:
                print("The platform is up!")
                State=False
                break
            else:
                re=True
                #print("The platform is moving...")

    except KeyboardInterrupt:
        GPIO.cleanup()

