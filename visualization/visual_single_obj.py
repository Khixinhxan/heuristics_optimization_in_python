import matplotlib.pyplot as plt
import numpy as np


def plot_landscape(B):
    x = np.linspace(B[0][0], B[0][1], 30)
    y = np.linspace(B[1][0], B[1][1], 30)
    X, Y = np.meshgrid(x, y)
    Z = evaluate(X, Y)
    plt.figure(dpi=1200)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')

def plot_convergence(S, best):
    plt.figure(dpi=1200)
    plt.plot(list(S),list(best.values()))

def report_solution(best, S, x_best):
    print('Objective value =', best[len(S)-1])
    print(x_best)