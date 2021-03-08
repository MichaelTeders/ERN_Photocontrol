import serial
import time
from threading import Timer
import pandas as pd
import numpy as np
import sys

# Connect to Arduino
""" check Arduino Software for correct COM-Port and Baud rate
    Connection with the arduino is started here     
"""
ser = serial.Serial()
ser.setPort("COM3")
ser.baudrate = 9600
ser.open()

# What input to use? pre-saved sequence or manuel input of conditions?
""" If you want to use a prepared sequence of steps saved in the same folder as "seq.csv" and answer: yes
    If you want to give light conditions and duration for each step manually enter: no
    The input consists of 3 numbers separated by a space:
        Condition BLUE light     Condition UV light      Duration of irradiation 
        (1 = ON, 0 = OFF)        (1 = ON, 0 = OFF)          (time in seconds)   
        
    example: 1 0 5    (blue light on, uv light off, for 5 seconds)
             1 1 600  (blue light on, uv light on, for 10 minutes)
    Both lights will be turned off after total experimental time (see below).
"""
seq = input("Use prepared step sequence? ")
if seq == "yes":                                          # using a prepared seq of steps
    data = pd.read_csv("seq.csv", header=0)               # import the sequence in panda, without header
    allinfo = data.values                                 # assign seq to allinfo variable
    print("Using prepared step sequence!")

elif seq == "no":                                          # give each step manually:
    numsteps = int(input("Enter the number of steps: "))   # ask for number of total steps
    numarg = 3                                             # 1st arg: Blue, 2nd arg: UV, 3rd: irradiation time
    allinfo = []                                           # Define empty allinfo variable
    for i in range(numsteps):                              # ask for condition and duration of step
        x = input("Give condition of Blue, UV and duration of step: ").split()
        stepinfo = []
        for j in range(numarg):                            # repeatedly ask for each step
            stepinfo.append(int(x[j]))
        allinfo.append(stepinfo)


# turn of lights after experiment
""" Calculate the total duration of the experiment by addition of each individual step durations
    Then starts the function 'shutdown' with that total time to turn off both lamps and stop connection with arduino.     
"""

sum_it = np.sum(allinfo, axis=0)
dur = sum_it[-1]


def shutdown():
    ser.write("d".encode())
    print("Experiment finished at " + time.strftime("%T")+".")
    ser.close()


# Make a protocol file
""" saves all prints as a 'protocol.txt' file in the current folder.
    Old data will be overwritten.     
"""
old_stdout = sys.stdout
log_file = open("protocol.txt", "w")
sys.stdout = log_file

# Check input and send commands to Arduino
""" Main part of the function, which iterates over the prepared input and sends the according commands to the arduino.
    'allinfo' is a list of lists containing all experimental information [[b1 uv1 t1][b2 uv2 t2][...]...] (see "input")
     The light conditions given in the sequence or manually are send as statements to the arduino:
        'a' = both lights on       
        'b' = blue on, uv off      
        'c' = blue off, uv on
        'd' = both lights off
    The irradiation time is not communicated to the arduino directly, but instead as delay time until the next command.
    The prompt shows the changes and the time they are made, as well as when the experiment is finished. 
"""
t = Timer(dur, shutdown)               # start timer for turning off lights
t.start()

for i in allinfo:
    if i[0] == 100 and i[1] == 100:
        ser.write("a100".encode())
        print(time.strftime("%T") + ": Blue: 100% UV: 100%")
        time.sleep(i[-1])
    elif i[0] == 100 and i[1] == 0:
        ser.write("b100".encode())
        print(time.strftime("%T") + ": Blue: 100%, UV: off")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 100:
        ser.write("c100".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 100%")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 0:
        ser.write("d".encode())
        print(time.strftime("%T") + ": Blue: off, UV: off")
        time.sleep(i[-1])
    elif i[0] == 50 and i[1] == 50:
        ser.write("a50".encode())
        print(time.strftime("%T") + ": Blue: 50%, UV: 50%.")
        time.sleep(i[-1])
    elif i[0] == 50 and i[1] == 0:
        ser.write("b50".encode())
        print(time.strftime("%T") + ": Blue: 50%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 50:
        ser.write("c50".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 50%.")
        time.sleep(i[-1])
    elif i[0] == 25 and i[1] == 25:
        ser.write("a25".encode())
        print(time.strftime("%T") + ": Blue: 25%, UV: 25%.")
        time.sleep(i[-1])
    elif i[0] == 25 and i[1] == 0:
        ser.write("b25".encode())
        print(time.strftime("%T") + ": Blue: 25%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 25:
        ser.write("c25".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 25%.")
        time.sleep(i[-1])
    elif i[0] == 75 and i[1] == 75:
        ser.write("a75".encode())
        print(time.strftime("%T") + ": Blue: 75%, UV: 75%.")
        time.sleep(i[-1])
    elif i[0] == 75 and i[1] == 0:
        ser.write("b75".encode())
        print(time.strftime("%T") + ": Blue: 75%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 75:
        ser.write("c75".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 75%.")
        time.sleep(i[-1])
    elif i[0] == 10 and i[1] == 10:
        ser.write("a10".encode())
        print(time.strftime("%T") + ": Blue: 10%, UV: 10%.")
        time.sleep(i[-1])
    elif i[0] == 10 and i[1] == 0:
        ser.write("b10".encode())
        print(time.strftime("%T") + ": Blue: 10%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 10:
        ser.write("c10".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 10%.")
        time.sleep(i[-1])
    elif i[0] == 20 and i[1] == 20:
        ser.write("a20".encode())
        print(time.strftime("%T") + ": Blue: 20%, UV: 20%.")
        time.sleep(i[-1])
    elif i[0] == 20 and i[1] == 0:
        ser.write("b20".encode())
        print(time.strftime("%T") + ": Blue: 20%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 20:
        ser.write("c20".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 20%.")
        time.sleep(i[-1])
    elif i[0] == 80 and i[1] == 80:
        ser.write("a80".encode())
        print(time.strftime("%T") + ": Blue: 80%, UV: 80%.")
        time.sleep(i[-1])
    elif i[0] == 80 and i[1] == 0:
        ser.write("b80".encode())
        print(time.strftime("%T") + ": Blue: 80%, UV: OFF.")
        time.sleep(i[-1])
    elif i[0] == 0 and i[1] == 80:
        ser.write("c80".encode())
        print(time.strftime("%T") + ": Blue: off, UV: 80%.")
        time.sleep(i[-1])


sys.stdout = old_stdout
log_file.close()
