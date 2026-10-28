# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:03:27 2026

@author: emmab

TP1 : Intégration numérique 
"""
import numpy as np
import sympy as sp
import math
# Question préliminaire 

x = sp.Symbol('x')
a = - (np.pi) 
b = np.pi
def f1(x): 
    return 2*x**3 + x**2
def f2(x) : 
    return (x/(np.pi)) * np.sin(2*x)
def f3(x) : 
    return np.sqrt(x)

# Méthodes de Newton-Côtes 

#1)

def NC_elem(g,w):
    p = len(w) - 1
    return sum( w[k] * g(-1 + (2*k)/p) for k in range(0,p+1))

#2) 
def f(x) :
    return 1 
"""w1 = np.array([1,1])
w2 = np.array([1/3, 4/3, 1/3])
w3 = np.array([1/4, 3/4, 3/4, 1/4])"""
# pour f l'intégrale = 2 
# trapèze = 2 
# Simpson = 2
# Newton = 2
def g(x) :
    return x
# pour g l'intégrale = 0
# trapèze = 0
# simpson = 0
# newton = 0
def h(x) :
    return x**2 
# pour h l'intégrale = 2/3
# trapèze = 2
# simpson = 2/3
# newton = 2/3
def j(x):
    return x**3
# pour j l'intégrale = 0
# simpson = 0
# newton = 0
def l(x):
    return x**4
# pour l l'intégrale = 2/5
# simpson = 2/3
# newton = non 

#3)

def NC_comp(f,a,b,N,w):
    h = (b-a)/N
    somme = 0
    for i in range (N):
        ai = a + i*h
        ai1 = a + (i+1)*h
        g = lambda x : f((b-a)/(2*N)*x + (ai+ai1)/2)
        somme += NC_elem(g,w)
    return (h/2)*somme

#4)
#f1 : 
    #trapèzes : 10.760000000000003
    #simpson : 10.666666666666666
    #newton : 10.666666666666668
#f2 :
    #trapèze : 0.14424576446781257
    #simpson : 0.14784027460870522
    #newton : 0.1478383418243272
#f3 :
    #trapèze : 1.8682025382318124
    #simpson : 1.8830508367710808
    #newton : 1.883916638711644

#5) 
import matplotlib.pylab as plt

def trace_erreur(f,a,b,N,w,Ie):
    x = []
    y = []
    for k in range (1,N+1):
        x.append(math.log(abs(Ie - NC_comp(f,a,b,k,w))))
        y.append(math.log(k))
    plt.plot(x,y) 
    plt.title('erreur')
    plt.show()
    return 

#Méthode de Gauss-Legendre

w1 = np.array([1,1])
w2 = np.array([5/9,8/9,5/9])
w3 = np.array([1/2+(1/6)*np.sqrt(5/6), 1/2-(1/6)*np.sqrt(5/6)])

x1 = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
x2 = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
x3 = np.array([-np.sqrt(3/7 - (2/7)*np.sqrt(6/5)), -np.sqrt(3/7 + (2/7)*np.sqrt(6/5))])

def Gauss_elem(g,w,x):
    p = len(w) - 1
    return sum( w[k] * g(x[k]) for k in range(0,p+1))

#ordre de la méthode 
# pour f l'intégrale = 2 
# trapèze =  2
# Simpson = 2.0
# Newton = ?

# pour g l'intégrale = 0
# trapèze = 0
# simpson = 0
# newton = ?

# pour h l'intégrale = 2/3
# trapèze = 2/3
# simpson = 2/3
# newton = ?

# pour j l'intégrale = 0
# trapèze = 0
# simpson = 0
# newton = ?

# pour l l'intégrale = 2/5
# trapèze = non 
# simpson = 2/5
# newton = ? 

#Ordre de trapèze = 3

def m(x) :
    return x**5
# pour m l'intégrale vaut 0
# simpson = 0
# newton = ? 

def n(x) :
    return x**6
# pour n l'intégrale vaut 2/7
# simpson = non
# newton = ? 

#Ordre de simpson = 5

def Gauss_comp(f,a,b,N,w,x):
    h = (b-a)/N
    somme = 0
    for i in range (N):
        ai = a + i*h
        ai1 = a + (i+1)*h
        g = lambda x : f((b-a)/(2*N)*x + (ai+ai1)/2)
        somme += Gauss_elem(g,w,x)
    return (h/2)*somme

#f1 :
    # trapèze = 10.66666666666667
    # simpson = 10.66666666666667
    # newton = ?

#f2 :
    # trapèze = 0.14783447850632517
    # simpson = 0.14783679856712056
    # newton = ?
    
#f3 : 
    # trapèze = 1.8862702298432201
    # simpson = 1.8858429350571875
    # newton = ?

def trace_erreur_Gauss(f,a,b,N,w,x,Ie):
    x = []
    y = []
    for k in range (1,N+1):
        x.append(math.log(abs(Ie - Gauss_comp(f,a,b,k,w,x))))
        y.append(math.log(k))
    plt.plot(x,y) 
    plt.title('erreur')
    plt.show()
    return
