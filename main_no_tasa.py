import matplotlib.pyplot as plt
from funciones_epidemia import modeloSIR_no_tasa

#S0 = float(input('Introduzca el valor de personas susceptibles a infectarse (entre 0 y 1):'))  #personas Susceptibles a infectarse iniciales
#I0 = float(input('Introduzca el valor de personas infectadas (entre 0 y 1):')) #personas Infectadas iniciales
#R0 = float(input('Introduzca el valor de personas recuperadas (entre 0 y 1):')) #personas Recuperadas iniciales
#trasm = float(input('Introduzca el valor de la tasa de trasmision de la enfermedad (entre 0 y 1):')) #Tasa de transmisión de la enfermedad
#recup = float(input('Introduzca el valor de la tasa de recuperacion de la enfermedad (entre 0 y 1):')) #Tasa de recuperación
#T = float(input('Introduzca el numero de días en el que la epidemia estuvo en activo:')) #Días de epidemia

S0 = 0.99  #Susceptibles iniciales
I0 = 0.01 #Infectados iniciales
R0 = 0 #Recuperados iniciales
trasm = 0.08 #Tasa de transmisión de la enfermedad
recup = 0.025 #Tasa de recuperación
T = 300 #Días de epidemia

t, S, I, R, = modeloSIR_no_tasa(S0, I0, R0, trasm, recup, T)


plt.plot(t, S, label='Población susceptible')
plt.plot(t, I, label='Población infectada')
plt.plot(t, R, label='Población recuperada')
plt.xlabel('Tiempo (días)')
plt.ylabel('Población')
plt.legend()
plt.show()
