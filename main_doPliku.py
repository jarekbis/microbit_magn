from microbit import *
import os

licznik = 'licznik.txt'

display.show('S')
while not button_a.was_pressed():
    sleep(500)
display.show('R')

sleep(2000)

if licznik in os.listdir():
    with open(licznik, 'r') as f:
        n = int(f.read())
else:
    n = 0

if n > 9:
    n = 0

with open(licznik, 'w') as f:
    f.write(str(n+1))


with open('dane_'+str(n)+'.py', 'wt') as f:
    f.write('pomiary=[')
    delim=''
    while not button_a.was_pressed() and not button_b.was_pressed():
        for i in "321x":
            display.show(i)
            sleep(500)
        x,y,z = 0,0,0
        for i in "ABC":
            display.show(i)
            x += compass.get_x()
            y += compass.get_y()
            z += compass.get_z()
            sleep(500)
        f.write(delim+str([x//3, y//3, z//3]))
        delim=','
    f.write(']')
    f.close()
display.show(n)