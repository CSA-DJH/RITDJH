import getpass
import csv
import time
import re
import RPi.GPIO as io 
io.setmode(io.BCM) 
pir_pin = 24 
power_pin = 23
 
io.setup(pir_pin, io.IN) 
io.setup(power_pin, io.OUT)
io.output(power_pin, False)
PERIOD_OF_TIME = 3#600
def loginoffline():
    f2 = open('UserListWithOutGradesWO10.csv - UserListWithOutGradesWO10.csv.csv', 'r')
    f = open("Logins.txt","a") 
    students=csv.reader(f2)
    username=input("Please enter your username: ")
    password=getpass.getpass("Please enter your password: ")
    username_rowgetnumyo=2 #change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
    password_rowgetnum=3 #master_row to the schools student list
    for hosts_rowyo in students:
        row = 1
        username=username.replace("@chaparralstaracademy.com","")
        hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].replace("@chaparralstaracademy.com","")
        hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].zfill(4)
        if (username == hosts_rowyo[username_rowgetnumyo]) & (password == hosts_rowyo[password_rowgetnum]):
            print("Logging in.", end=""),
            time.sleep(1)
            print(".", end=""),
            time.sleep(1)
            print(".")
            time.sleep(3)
            print("Logging in complete! Plug in your chromebook now;")
            f.write(username+"\n")
            start = time.time()
            while True :
                io.output(power_pin, True)
                
                if time.time() > start + PERIOD_OF_TIME:
                    print("POWER OFF")
                    time.sleep(1)
                    io.output(power_pin, False)
                    time.sleep(3)
                    loginoffline()
                    break
            break
    print("Logging in.", end=""),
    time.sleep(1)
    print(".", end=""),
    time.sleep(1)
    print(".")
    time.sleep(3)
    print("Error logging in, please try again! ")
    loginoffline()
    f2.close()
    f.close()
    
loginoffline()
