from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

exec(open('dane_8.py').read())
print(len(pomiary))
#wx , wy, wz = 6 , 9, 1
wx , wy, wz = 9 , 6, 1

if len(pomiary) != wx*wy*wz:
    raise ValueError

x = [j for i in range(wy) for j in range(wx)]
y = [i for i in range(wy) for j in range(wx)]
z = [10 for i in range(wx*wy)]

mx = [pomiary[i][0] for i in range(len(pomiary))]
my = [pomiary[i][1] for i in range(len(pomiary))]
mz = [pomiary[i][2] for i in range(len(pomiary))]


ax.quiver(x, y, z, mx, my, mz, normalize=True)

plt.show()
