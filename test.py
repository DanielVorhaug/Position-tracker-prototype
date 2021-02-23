

import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

start_time = time.time_ns()
    
f = open("blink.txt", "w")
f.write(" ")
f.close()

while True:
    data = arduino.readline()

    data = data.decode("utf-8")

    

    if len(data) > 0:
        f = open("blink.txt", "a")
        f.write(str((time.time_ns() - start_time)/1000000000) + ", " + data.strip().strip(".") + "\n")
        print(data.strip().strip("."))
        f.close()