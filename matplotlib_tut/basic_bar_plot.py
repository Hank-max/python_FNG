#this is just a basic x,y plot

import numpy as np  #this is required to plot all of the data as bars. This is going to allow us to offset the x values.
from matplotlib import pyplot as plt


#print(plt.style.available) 
# uncomment above and comment out the plt.show to see a list of all the different styles.
#you can also use this instead of choosing all of the colors and such. 

#for example you could just use this style
#plt.style.use('fivethirtyeight')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
          

dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850]

#this is the second line on the plot
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370]


plt.plot(ages_x, py_dev_y, color='b', linestyle='--',linewidth=3, label = 'data set 1') #You can also google hex colors
plt.plot(ages_x, dev_y, label = 'data set 2')
#if you wanted this to be a bar chart, then do the following
#plt.bar(ages_x, dev_y, label = 'data set 2')

#note the way the lines are stacked in the plot are based on the plotting order in the code (i.e. one on top of another)

plt.xlabel('ages')
plt.ylabel('salary')
plt.title('basic plot')

plt.grid(True)
plt.legend()  #this is required for the 'label' data to show in the plot
plt.show() #this is required.
