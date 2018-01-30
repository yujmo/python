import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init():
    line.set_data([], [])
    return line,


def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 5
        yield t, 1


data_gen.t = 0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(0, 5)
ax.grid()
xdata, ydata = [], []


def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,


ani = animation.FuncAnimation(
    fig, run, data_gen, blit=True, interval=10, init_func=init, repeat=False)

plt.show()
