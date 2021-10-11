#Natalia Książek
import main
import math
import numpy as np
import linalg
from numpy.linalg import inv

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r <= 0 or h <= 0:
        return np.NaN

    p = (2 * math.pi * r * r) + (2 * math.pi * r * h)

    return p

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    fib_vec = np.array([1, 1])

    if n < 0:
        return None
    elif n == 0:
        return np.array([0])
    elif n == 1:
        return np.array([1])
    elif n == 2:
        return fib_vec
    else:
        for i in range(2, n+1):
            next_ele = fib_vec[-2] + fib_vec[-1]
            fib_vec = np.append(fib_vec, next_ele)
        return fib_vec


def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -1], [0, 1, 1], [-a, a, 1]])

    Mdet = np.linalg.det(M)

    if Mdet != 0:
        Minv = np.linalg.inv(M)
    else:
        return np.NaN

    Mt = np.transpose(M)

    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m < 0 or n < 0:
        return None

    M = np.zeros((m, n))

    for i in range(0, m+1):
        for j in range(0, n+1):
            if i > j:
                M[i][j] = i
            else:
                M[i][j] = j
    return M