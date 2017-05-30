#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math


infile=open('dados.txt','r')
theta=[0]
vw=[0]
a=[0]
e=[0]
t=[0]



for line in infile:
	x,y,z,v,b = line.split()
	theta.append(float(x))
	vw.append(float(y))
	a.append(float(z))
	e.append(float(v))
	t.append(float(b))



plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel(r'Energia (J)')
#plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade($\frac{m}{s}$)')

plt.title(r'P\^endulo com Arrasto', fontsize=12)
plt.grid()
#plt.plot(t,theta,'b-', linewidth=2, label="$x_{(t)}$")
#plt.plot(t,vw,'r-', linewidth=2, label="$v_{(t)}$")
#plt.plot(theta,vw,'c-', linewidth=2")
plt.plot(t,e,'b-', linewidth=2)
plt.legend(loc='upper right')
plt.savefig("tx5.pdf", dpi=96)
plt.show()


