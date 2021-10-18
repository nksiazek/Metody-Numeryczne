import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random


def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """
    if x1.shape != y1.shape or min(x1.shape) == 0 or x2.shape != y2.shape or min(x2.shape) == 0:
        return None

    fig, ax = plt.subplots()
    ax.plot(x1, y1, color='blue', linewidth=4)
    ax.plot(x2, y2, color='red', linewidth=2)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend([label1, label2])

    return fig


def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    """Funkcja służąca do stworzenia dwóch wykresów typu plot w konwencji subplot wertykalnie lub chorycontalnie. 
    Szczegółowy opis w zadaniu 5.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    x1label(str): opis osi x dla pierwszego wykresu,
    y1label(str): opis osi y dla pierwszego wykresu,
    x2label(str): opis osi x dla drugiego wykresu,
    y2label(str): opis osi y dla drugiego wykresu,
    title(str): tytuł wykresu,
    orientation(str): parametr przyjmujący wartość '-' jeżeli subplot ma posiadać dwa wiersze albo '|' jeżeli ma posiadać dwie kolumny.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 5
    """
    if x1.shape != y1.shape or min(x1.shape) == 1 or x2.shape != y2.shape or min(x2.shape) == 1:
        return None

    if len(x1) != len(set(x1)) or len(x2) != len(set(x2)):
        return None

    if orientation == '-':
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle(title)

        ax1.plot(x1, y1)
        ax1.set(xlabel=x1label, ylabel=y1label)

        ax2.plot(x2, y2)
        ax2.set(xlabel=x2label, ylabel=y2label)

    elif orientation == '|':
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
        fig.suptitle(title)

        ax1.plot(x1, y1)
        ax1.set(xlabel=x1label, ylabel=y1label)

        ax2.plot(x2, y2)
        ax2.set(xlabel=x2label, ylabel=y2label)

        fig.tight_layout(pad=2.0)
    else:
        return None

    return fig




def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
    if x.shape != y.shape or min(x.shape) == 1:
        return None

    if len(x) != len(set(x)):
        return None

    if log_axis == 'x':
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        ax.set_xscale('log')

    elif log_axis == 'y':
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        ax.set_yscale('log')

    elif log_axis == 'xy':
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        ax.set_yscale('log')
        ax.set_xscale('log')

    else:
        return None

    return None

#TESTY
# x1 = np.linspace(-10, 10)
# x2 = np.linspace(-10, 10)
#
# y1 = x1+2
# y2 = x2**2 - 2*np.sin(x2) + 3

#compare_plot(x1, y1, x2, y2, 'x', 'y', 'compare', 'y1', 'y2')
#parallel_plot(x1, y1, x2, y2, 'x1', 'y1', 'x2', 'y2', 'title', '|')
#log_plot(x1, y1, 'x', 'y', 'log plot', 'xy')