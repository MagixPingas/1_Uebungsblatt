'''Mathematische Funktionen wie der Logarithmus oder der Sinus gehören meist nicht zum
Kern einer Programmiersprache. Im Falle von Python stellt das Zusatzmodul math diese
Funktionen aber zur Verfügung.
Önen Sie in der IDLE-Shell eine neue Datei, tippen Sie folgenden Programmcode ab
(oder einfacher: kopieren Sie ihn), speichern Sie ihn unter Mathe.py und starten Sie das
Programm. Überlegen Sie, was genau die einzelnen Funktionen jeweils berechnen:
import math
print ( " math . sin (90.0) = " , math . sin (90.0) )
print ( " math . sin ( math . radians (90.0)) = " ,\
math . sin ( math . radians (90.0)) )
print ( " math . acos ( -1.0) = " , math . acos ( -1.0) )
print ( " math . pi = " , math . pi )
print ( " math . degrees ( math . acos ( -1.0)) = " ,\
math . degrees ( math . acos ( -1.0)) )
print ( " math . log (100) = " , math . log (100) )
print ( " math . log (100 , 10) = " , math . log (100 , 10) )
(Hinweis: Mit \ kann man einen nicht in eine Zeile passenden Befehl auf zwei Zeilen
verteilt eingeben.)'''


import math
print ( " math . sin (90.0) = " , math . sin (90.0) )
print ( " math . sin ( math . radians (90.0)) = " ,\
math . sin ( math . radians (90.0)) )
print ( " math . acos ( -1.0) = " , math . acos ( -1.0) )
print ( " math . pi = " , math . pi )
print ( " math . degrees ( math . acos ( -1.0)) = " ,\
math . degrees ( math . acos ( -1.0)) )
print ( " math . log (100) = " , math . log (100) )
print ( " math . log (100 , 10) = " , math . log (100 , 10) )