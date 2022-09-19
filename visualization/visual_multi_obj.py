import matplotlib.pyplot as plt
import numpy as np


def plot_landscape(m, B):
    x = np.linspace(B[0][0], B[0][1], 30)
    y = np.linspace(B[1][0], B[1][1], 30)
    X, Y = np.meshgrid(x, y)
    Z = evaluate(X, Y, m)
    plt.figure(m, dpi=1200)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')

def plot_front(gP_a):
    plt.figure(dpi=1200)
    plt.scatter(gP_a[0],gP_a[1])
    
def report_front(gP_a, cT, P_a, B, D, I):
    print('Objective values =', gP_a)
    T = range(cT)
    x = [ [ B[d][0]+ ((sum((2**i)*P_a[d][t][i] for i in I[d]))/((2**len(I[d]))-1))*(B[d][1]-B[d][0]) for t in T] for d in D]
    print('Solution values =', x)

