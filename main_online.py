from microbit import *

#microbit.uart.init(baudrate=9600)

while True:
    x=compass.get_x()
    y=compass.get_y()
    z=compass.get_z()
    print("m",x,y,z)
    #uart.write(x,y,z)
    sleep(100)