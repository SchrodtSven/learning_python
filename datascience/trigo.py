import matplotlib.pyplot as plt
import numpy as np


# Fs = 8000
# f = 5
# sample = 8000
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.plot(x, y)
# plt.xlabel('sample(n)')
# plt.ylabel('voltage(V)')
# plt.show()

fs = 100 # sample rate 
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = np.sin(2*np.pi*f * (x/fs)) 

#this instruction can only be used with IPython Notbook. 
#% matplotlib inline
# showing the exact location of the smaples
plt.stem(x,y, 'r', )
plt.plot(x,y)

plt.show()