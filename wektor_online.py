from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import serial, time
port = "COM13"
s=serial.Serial(port)
s.baudrate = 115200

fig = plt.figure()
ax = fig.gca(projection='3d')

while True:
    d = str(s.readline(),'cp1250')
    if d[0]=='m':
        m = [int(i) for i in d.split(" ") if i!='m' ]
        ax.quiver(0, 0, 0, m[0], m[1], m[2], normalize=True)
        #print(m)
        plt.draw()
        plt.pause(0.01)
        ax.collections[0].remove()


