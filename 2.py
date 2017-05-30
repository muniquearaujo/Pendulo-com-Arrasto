#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

def verletarrasto(xo,vo,ao,eo):
   x=xo+vo*dt+0.5*((-wo)*math.sin(xo)-gama*vo)*dt**2
   atemp=((-wo)*math.sin(x)-gama*vo)
   vtemp=vo+0.5*(((-wo)*math.sin(xo)-gama*vo)+atemp)*dt
   atemp=((-wo)*math.sin(x)-gama*vtemp)
   v=vo+0.5*((-wo)*math.sin(xo)-gama*vo+atemp)*dt
   a=((-wo)*math.sin(x)-gama*v)
   e=0.5*v**2+1*9.8*(10-10*math.cos(x))
   return x,v,a,e

xo=1.0
vo=0.0
dt=0.01
t=0.0
xf=[1.0]
vf=[0.0]
tf=[0.0]
E=[0.0]
eo=0.0
af=[0.0]
ao=0

wo=input('Informe o valor do w²\n')
gama=input('Informe o valor de gama\n')

while t<60:
   t=t+dt
   xo,vo,ao,eo=verletarrasto(xo,vo,ao,eo)
   xf.append(xo)
   vf.append(vo)
   af.append(ao)
   tf.append(t)
   E.append(eo)
   
   
outfile=open('dados.txt','w')
for i in range(len(tf)):
	outfile.write("%s\t%s\t%s\t%s\t%s\n" % (xf[i],vf[i],af[i],E[i],tf[i]))
outfile.close()
