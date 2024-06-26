# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t7nphvO4Y9xBbsAot3iYpsKvXdI0p9xX
"""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,4,6,1],)
plt.ylabel("Numbers")
plt.xlabel("Indices")
plt.title("MyPlot")
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],)
plt.ylabel("Squares")
plt.xlabel("Numbers")
plt.title("Table")
plt.grid()
plt.show()

plt.plot([1,2,3,4,5],[5,10,15,20,25])
plt.xlabel("Numbers")
plt.ylabel("Factors")
plt.title("Table of 5")
plt.grid()
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],'bs')
plt.grid()
plt.show()

import numpy as np
t = np.arange(0.,5.,0.2)

plt.plot(t,t**2,'b--',label ='^2')
plt.plot(t,t**2.2,'rs',label ='^2.2')
plt.plot(t,t**2.5,'g^',label ='2.5^')
plt.legend()
plt.grid()
plt.show()

#Controlling Line Properties:
import matplotlib.pyplot as plt

x=[1,2,3,4] ; y = [1,4,9,16]
plt.plot(x,y,linewidth = 5.0)
plt.grid()
plt.show()

x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = [1,2,3,4]
y2 = [2,4,6,8]
line = plt.plot(x1,x2,y1,y2)

plt.setp(line[0],color = 'r',linewidth = 2.5)
plt.setp(line[1],color = 'g',linewidth = 2.0)
plt.grid()
plt.show()

import numpy as np
def f(t):
  return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.figure(1)

plt.subplot(211)
plt.grid()
plt.plot(t1,f(t1),'b-')

plt.subplot(212)
plt.grid()
plt.plot(t2,np.cos(2*np.pi*t2),'r--')

plt.show()

import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])
plt.figure(1)
plt.subplot(211)
plt.title('Plotting Graph')

plt.figure(2)
plt.plot([4,5,6])


plt.show()

