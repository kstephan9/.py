### https://www.youtube.com/watch?v=Mll6emjBFvA&t=440s

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)


url = 'https://wikipedia.org/wiki/World_population_estimates'

df = pd.read_html(url, header=0)

post_war = df[2]
post_war = post_war.set_index('Year')

projected = df[3].set_index('Year')
print(projected)

fig, ax = plt.subplots(figsize=[10,10])
post_war.plot(ax=ax, linewidth=7)
projected.plot(ax=ax, linestyle='dashed')
ax.set_ylabel('Global Population')

plt.show()


alldata = pd.concat([post_war, projected], axis=1)
alldata.to_excel('Global_Population.xlsx')

