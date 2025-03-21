'''Lassen Sie sich mit Hilfe des Modules math die folgenden Werte berechnen: den Sinus von
30◦, den Cosinus von 50 gon, die Zahl 2,163, den Logarithmus von 1,2 ·10−22 zur Basis 10
sowie den Arkuskosinus von 0.'''

import math as m

degree = lambda x : (m.pi/180) * x
gon = lambda x : (m.pi/200) * x


print(m.sin(degree(30)))

print(m.cos(gon(50)))

print(m.pow(2.1,63))

number = m.pow(1.2, -22)

print(m.log(number, 10))

print(m.acos(0))