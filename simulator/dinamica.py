import numpy as np

def forza(x1, x2, y1, y2, m1, m2, G=1):
    """Calcola la forza gravitazionale nelle due componenti"""
    F_1 = G*m1*m2/(((x2-x1)**2+(y2-y1)**2)**(3/2))
    return F_1*(x2-x1), F_1*(y2-y1)

def accelerazione(F, m):
    """Calcola l'acelerazione nelle due componenti"""
    return F/m

def calcolaAccelerazioni(x, y, m):
    """Calcola la somma di tutte le accelerazioni per ogni particella"""
    N = len(x)
    f_x = np.zeros(N)
    f_y = np.zeros(N)
    a_x = np.zeros(N)
    a_y = np.zeros(N)

    for i in range(N):
        for l in range(i+1,N):
            f = forza(x[i], x[l], y[i], y[l], m[i], m[l])
            f_x[i] += f[0]
            f_y[i] += f[1]
            f_x[l] += -f[0]
            f_y[l] += -f[0]
            
    for i in range(N):
        a_x[i] = accelerazione(f_x[i], m[i])
        a_y[i] = accelerazione(f_y[i], m[i])    
    return a_x, a_y
