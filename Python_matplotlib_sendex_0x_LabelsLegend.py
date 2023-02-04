# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [2, 3, 4]
y2 = [10, 14, 12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck It Out')


x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x, y, label="Bars1", color='r')
plt.bar(x2, y2, label="Bars2", color='c')


population_ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 121, 122, 130, 111, 115, 112, 80, 85, 65, 54, 54, 55]

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages)

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)


x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [50, 20, 40, 20, 10, 40, 50, 20]


plt.scatter(x, y, label='skitscat', color='k', marker='*', s=500)


plt.legend()


plt.show()
