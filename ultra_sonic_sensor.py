import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Constants
GPIO_TRIGGER = 23
GPIO_ECHO = 24
CENTIMETER_PER_INCH = 2.54
SONIC_SPEED = 34300  # cm/s

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001) # Wait 0.1 ms
    GPIO.output(GPIO_TRIGGER, False)
    #
    start_time = time.time()
    stop_time = time.time()

    # Calibrate times
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
    # Calculate time differences
    elapsed = stop_time - start_time
    # adjust for sonic speed 
    # divide by 2 because of front and back
    dist = elapsed * SONIC_SPEED / 2
    # Convert to inches
    dist = dist/CENTIMETER_PER_INCH
    #
    return dist

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Distance = %2.2f inches" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stoped")
        GPIO.cleanup()
