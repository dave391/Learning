


def calcoli_rettangolo(base:float,altezza:float):
    '''calcolo 
    - perimetro 
    - area rettangolo'''
    area_rett = base * altezza
    perimetro_rett = (base*2) + (altezza*2)
    return area_rett,perimetro_rett

def calcoli_cerchio(raggio:float):
    '''calcolo 
    - perimetro 
    - area cerchio'''
    import numpy as np
    area_cerchio = np.pi * raggio**2
    perimetro_cerchio = 2*np.pi*raggio
    return area_cerchio,perimetro_cerchio