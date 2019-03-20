# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:16:11 2019

@author: Yashodhan
"""

#Monte Carlo
import numpy as np
import matplotlib.pyplot as plt


def pi1(): #First task
    x=[]    #Drawing a square
    y=[]    #Drawing a square
    n=0     #Number of the darts landing inside the quarter.
    for i in range(1000000): #Generating random numbers
        x.append(np.random.rand())
        y.append(np.random.rand())
        if x[i]**2+y[i]**2<1: #Counting those inside the quarter
            n=n+1   
    return n/250000 #value of Pi
    
def pi2():
    x=[]
    y=[]
    n=0
    for i in range(1000000):
        x.append(np.random.rand())
        y.append(np.random.rand())
        if (x[i]-0.5)**2+(y[i]-0.5)**2<0.25: #Shifting the center to (0.5,0.5)
            n=n+1   
    return n/250000
    
def pi3():
    x=[]
    y=[]
    z=[]
    n=0
    for i in range(1000000):
        x.append(np.random.rand())
        y.append(np.random.rand())
        z.append(np.random.rand())
        if (x[i]-0.5)**2+(y[i]-0.5)**2+(z[i]-0.5)**2<0.25:
            n=n+1   
    return 6*n/1000000
    
def std():
    pi1e=[]
    pi2e=[]
    pi3e=[]
    for i in range(20):
        a1=pi1()-3.14152
        a2=pi2()-3.14152
        a3=pi3()-3.14152
        pi1e.append(np.abs(a1))
        pi2e.append(np.abs(a2))
        pi3e.append(np.abs(a3))
    print("The standard deviations are as follows")
    print(np.average(pi1e),np.average(pi2e),np.average(pi3e))
    #print(pi3e,pi2e,pi1e)
    
"""Question 2 starts here"""

"""Defining formulae"""
def cross(t):#Formula for differential cross section
    return 1.90*(10**-35)/np.sin(t)**4

def b(v):#Formula for the impact parameter
    t=v[0]
    e=v[1]
    return 2*3.36*10**-30/(np.tan(t)*e)

"""Generating random energies and angles"""
energ=7*np.random.random(175)#Values of random energies ranging from 0 to 7eV.
energies=[]#Final list to be made
for i in range(175):
    if energ[i]>3:
        energies.append(energ[i])#Only selecting energies from 3-7eV
angles=np.pi*np.random.random(len(energies))#Array of random angles ranging from 0 to Pi

"""Applying the formulae"""
blist=[]
crosslist=[]
for i in range(len(energies)):
    blist.append(b([angles[i],energies[i]]))
    crosslist.append(cross(angles[i]))

"""Plotting and calculating the mean and deviations"""
def Q2():
    plt.plot(angles,blist,"o")
    plt.savefig("blist1.png")    
    plt.show()
    plt.plot(angles,crosslist,"o")
    plt.savefig("cross1.png")
    plt.show()
    print("The mean and the standard deviation of the impact parameter are ",np.mean(blist),"and",np.std(blist),"respectively")        
    print("The mean and the standard deviation of the differential cross section are ",np.mean(crosslist),"and",np.std(crosslist),"respectively")

"""Problem 3 starts here"""     
def L(x,x0,g):
    return g/(np.pi*((x-x0)**2+g**2))

l1=np.zeros(1000)
l2=np.zeros(1000)
l3=np.linspace(-3,3,1000)
def tran():#Transforamtion method
    for i in range(1000):
        l1[i]=np.tan(np.pi*(np.random.random()-0.3975))
    plt.hist(l1,20)
    plt.savefig("lorhist.png")
def lor():#Direct method
    for i in range(1000):
        l1[i]=1/(1+np.random.random()**2)        
def ref():#Reference histogram
    for i in range(1000):
        l2[i]=3*L(l3[i],0,1)
    plt.plot(l3,l2)
    plt.savefig("lor2.png")

























































