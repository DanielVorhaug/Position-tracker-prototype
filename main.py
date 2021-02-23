import pyautogui
import keyboard
import time
import serial
import math
import win32api, win32con 

# win32api.SetCursorPos((x, y))
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def main():
    #arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
    a = 1
    #coordinate = list(pyautogui.position())
    #dCoordinate = [0, 0]
    #while keyboard.is_pressed("q") q== False:

    movement = [0,0]
    angle = 0 #math.pi/4
    sensitivity = 1
    filter_factor = 0.2

    coordinate_zero = [int(1920/2) ,int(1080/2)]

    position = [0,0]

    while keyboard.is_pressed("q") == False: 
        
        coordinates = pyautogui.position()

        win32api.SetCursorPos((coordinate_zero[0], coordinate_zero[1]))

        data = arduino.readline()
        data = data.decode("utf-8")

        if len(data) > 0:
            try:
                angle_new = -float(data.strip().strip(".")) * math.pi / 180 + 0.2
                angle = (1 - filter_factor) * angle + filter_factor * angle_new
                #print(angle)
            except:
                print("crash")
                angle = 0

        #print(a)
        a+=1
        #time.sleep(0.001)
        new_coordinates = pyautogui.position()

        dx = coordinates[0] - coordinate_zero[0]
        dy = coordinates[1] - coordinate_zero[1]

        movement[0] = (dx * math.cos(angle) + dy * math.sin(angle)) / sensitivity
        movement[1] = (dy * math.cos(angle) - dx * math.sin(angle)) / sensitivity

        position[0] += movement[0]
        position[1] += movement[1]

        print(position, "\t", angle)

        

        if keyboard.is_pressed("n") == True:
            position = [0,0]

        # new_coordinate = list(pyautogui.position())
        # dCoordinate = [new_coordinate[0] - coordinate[0], new_coordinate[1] - coordinate[1]]
        # coordinate = new_coordinate
        # print(dCoordinate)
        # time.sleep(0.01)



main()