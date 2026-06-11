import numpy as  np
from scipy.integrate import odeint 

def sir(y, trasm, recup, t):  # He puesto el argumento t al final
        
    S, I, R = y
    dSdt = -trasm*S*I #Calculamos la operación de susceptibles
    dIdt = trasm*S*I - recup*I #Calculamos la operación de infectados
    dRdt = recup*I #Calculamos la operación de recuperados
    
    return dSdt, dIdt, dRdt
    

def modeloSIR_no_tasa(S0, I0, R0, trasm, recup, T): #Definimos la primera función, que no contiene dinámica vital 

    y0 = (S0, I0, R0)


    t = np.linspace(0, T, T+1)
    y = odeint(sir, y0, t, args=(trasm, recup))  # He añadido args=(trasm, recup)
    S, I, R = y.T

    return t, S, I, R




def sir_tasa(y, trasm, recup, vac, nym, t):  # He puesto el argumento t al final
        
    S, I, R = y
    dSdt =  - trasm*S*I - (vac+nym)*S
    dIdt = trasm*S*I - recup*I - nym*I
    dRdt = recup*I - nym*R + vac*S
        
    return dSdt, dIdt, dRdt


def modeloSIR_tasa(S0, I0, R0, trasm, recup, nym, vac, T): #Definimos las segunda función añadiendo la dinámica vital

    y0 = (S0, I0, R0)

    t = np.linspace(0, T, T+1)
    y = odeint(sir_tasa, y0, t, args=(trasm, recup, vac, nym) )  # He añadido args = (trasm, recup, vac, nym)
    S, I, R = y.T
    
    return t, S, I, R





#def modeloSIR_no_tasa(S0, I0, R0, trasm, recup, T): #Definimos la primera función, que no contiene dinámica vital 
    def sir(y, t):
        
        S, I, R = y
        dSdt = -trasm*S*I #Calculamos la operación de susceptibles
        dIdt = trasm*S*I - recup*I #Calculamos la operación de infectados
        dRdt = recup*I #Calculamos la operación de recuperados
        
        return dSdt, dIdt, dRdt
    

    y0 = (S0, I0, R0)


    t = np.linspace(0, T, T+1)
    
    y = odeint(sir, y0, t)
    S, I, R = y.T
    return t, S, I, R


#def modeloSIR_tasa(S0, I0, R0, trasm, recup, nym, vac, T): #Definimos las segunda función añadiendo la dinámica vital
    def sir_modificado(y, t):
        
        S, I, R = y
        dSdt = nym - trasm*S*I - (vac+nym)*S
        dIdt = trasm*S*I - recup*I - nym*I
        dRdt = trasm*I - nym*R + vac*S
        
        return dSdt, dIdt, dRdt
    

    y0 = (S0, I0, R0)
    

    t = np.linspace(0, T, T+1)
    y = odeint(sir_modificado, y0, t)
    S, I, R = y.T
    
    return t, S, I, R