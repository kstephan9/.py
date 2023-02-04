# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']


# plt.plot([], [], color='m', label='Sleeping', linewidth=5)
# plt.plot([], [], color='c', label='Eating', linewidth=5)
# plt.plot([], [], color='r', label='Working', linewidth=5)
# plt.plot([], [], color='k', label='Playing', linewidth=5)

# plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

color_list = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities, colors=color_list, startangle=90, shadow=True, explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.legend()


plt.show()
