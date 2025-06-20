from custom_plt import plt
import numpy as np
import argparse
from typing import Optional
from math import floor, ceil

colors = [
    '#D81B60',
    '#1E88E5',
    '#FFC107',
    '#004D40'
]

def extract_data(filepath: str, zero_time: bool = True):
    with open(filepath) as file:
        time, data, fit = [], [], []
        for line in file.readlines():
            if not line[0].isnumeric(): continue
            t, d, f = line.strip().split()
            time.append(float(t))
            data.append(float(d))
            fit.append( float(f))
    time = np.array(time)
    data = np.array(data)
    fit  = np.array(fit)
    if zero_time: time = time - time[0]
    return time, data, fit

def yticks(ymin, ymax):
    '''
    Takes the range (ymin, ymax) and calculates the order of magnitude. Then
    returns a list of the most suitable yticks.
    '''
    yrange = ymax - ymin
    order = 0
    if yrange >= 10:
        while yrange / (10 ** order) >= 10: order += 1
    if yrange <= 1:
        while yrange / (10 ** order) <=  1: order -= 1
    
    ytick_min = floor(ymin / (10 ** order)) * (10 ** order)
    ytick_max = ceil(ymax / (10 ** order)) * (10 ** order)
    return np.arange(ytick_min, ytick_max+0.5*(10**order), 10**order)


def make_figure(file1: str, file2: str, label1: str = '', label2: str = '',
                color1: int = 0, color2: int = 1, zero_time: bool = True,
                title: str = '', xmin: float = 0, xmax: Optional[float] = None,
                ymin: Optional[float] = None, ymax: Optional[float] = None,
                fit1: bool = False, fit2: bool = False):
    
    fig, ax = plt.subplots()
    label1 = label1.replace(' ', '\n')
    label2 = label2.replace(' ', '\n')
    
    t, d, f = extract_data(file1, zero_time=zero_time)
    ax.plot(t, d, color=colors[color1], linewidth=2, label=label1)
    if fit1:
        plt.plot(t, f, color=colors[color1], linewidth=2, linestyle='--',
                 label=label1+' Fit')
    t, d, f = extract_data(file2, zero_time=zero_time)
    ax.plot(t, d, color=colors[color2], linewidth=2, label=label2)
    if fit2:
        plt.plot(t, f, color=colors[color2], linewidth=2, linestyle='--',
                 label=label2+' Fit')
        
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel('nm')
    fig.suptitle(title, fontweight='bold')

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    y1, y2 = ax.get_ylim()
    ax.set_yticks(yticks(y1, y2))

    xticks = ax.get_xticks()
    xticks = [x for x in xticks if x != 0.]
    ax.set_xticks(xticks)

    ax.minorticks_off()

    ax.legend(frameon=False,
              prop=dict(weight='normal'),)
    
    ax.spines['bottom'].set_position('zero')



file1 = '/Users/jack/Documents/GitHub/LizziePrism/t1A1Results.txt'
file2 = '/Users/jack/Documents/GitHub/LizziePrism/t1C1Results.txt'
make_figure(file1, file2, label1='Unmodified', label2='N-benzylmaleimide Conjugate', title=r'IL-2R$\beta \gamma$: N40C Modified vs Unmodified', xmax=400)
plt.show()
