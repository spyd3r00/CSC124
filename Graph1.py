import matplotlib.pyplot as plt
import numpy as np


labels = ['10', '100', '1000', '10000']
Seconds = []
file = open('Time.txt')
textfile= file.read()
values = textfile.split(",")

for i in values:
	Seconds.append(float(i))


Merge = Seconds[0],Seconds[2],Seconds[4],Seconds[6]
Insert = Seconds[1],Seconds[3],Seconds[5],Seconds[7]

x = np.arange(len(labels)) 
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Merge, width, label='Merge')
rects2 = ax.bar(x + width/2, Insert, width, label='Insert')


ax.set_title('Execution Time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()