import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 
f = open("Logins.txt","a") 
pir_pin = 24 
power_pin = 23
start = time.time() 
io.setup(pir_pin, io.IN) 
io.setup(power_pin, io.OUT)
io.output(power_pin, False)
'''
while True:
    if io.input(pir_pin):
        print("POWER ON")
        io.output(power_pin, True)
        time.sleep(20);
        print("POWER OFF")
        io.output(power_pin, False)
        time.sleep(5)
    time.sleep(1)
'''


   

PERIOD_OF_TIME = 3600 

while True :
    
        io.output(power_pin, True)

    if time.time() > start + PERIOD_OF_TIME 
        print("POWER OFF")
        io.output(power_pin, False)
    break 

    f.write("and can I get some pickles on that")

f.close()
