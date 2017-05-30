#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

def verletarrasto(xo,vo):
   x=xo+vo*dt+0.5*((-wo)*math.sin(xo)-gama*vo)*dt**2
   atemp=((-wo)*math.sin(x)-gama*vo)
   vtemp=vo+0.5*(((-wo)*math.sin(xo)-gama*vo)+atemp)*dt
   atemp=((-wo)*math.sin(x)-gama*vtemp)
   v=vo+0.5*((-wo)*math.sin(xo)-gama*vo+atemp)*dt
   a=((-wo)*math.sin(x)-gama*v)
   e=0.5*v**2+1*9.8*(10-10*math.cos(x))
   return x,v,e

wo=input('Informe o valor do w²\n')
gama=input('Informe o valor de gama\n')
xo=1
vo=0
dt=0.01
t=0
xf=[1]
vf=[0]
tf=[0]
E=[0]
eo=0



while t<60:
   t=t+dt
   xo,vo,eo=verletarrasto(xo,vo)
   xf.append(xo)
   vf.append(vo)
   tf.append(t)
   E.append(eo)
   
   
plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade($\frac{m}{s}$)')

plt.title(r'P\^endulo com Arrasto', fontsize=12)
plt.grid()
plt.plot(tf,xf,'c-', linewidth=2, label="$x_{(t)}$")
plt.plot(tf,vf,'m-', linewidth=2, label="$v_{(t)}$")
plt.legend(loc='upper right')
plt.savefig("tarefa1.pdf", dpi=96)
plt.show()
  
