# https://www.youtube.com/watch?v=ZmYPzESC5YY
#
# sendex

from DefaultItems import DataFileLocation
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

print(DataFileLocation)

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

data_folder = DataFileLocation
datafile = data_folder + '\\' + 'Python_matplotlib_animation_LiveGraphs_16_samplefile.txt'
print("datfile: ", datafile)
# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


def animate(i):
    graph_data = open(datafile, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.set_ylim([None, None])
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
