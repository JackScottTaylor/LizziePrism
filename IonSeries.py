from custom_plt import plt
import numpy as np
from typing import Optional
import argparse

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'
plt.rcParams['mathtext.it'] = 'Arial:italic'
plt.rcParams['mathtext.bf'] = 'Arial:bold'

def latex_sci_formatter(y, _):
    if y == 0:
        return r"$0$"
    exponent = int(np.floor(np.log10(abs(y))))
    coeff = y / 10**exponent
    return r"${:.0f}\times10^{{{}}}$".format(coeff, exponent)

def extract_masses_intensities(filepath: str):
    masses, intensities = [], []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line.strip() == '': continue
            m, i = [float(x) for x in line.split()]
            masses.append(m); intensities.append(i)

def make_figure(filepath: str, title: str = '', xmin: Optional[float] = 500,
       xmax: Optional[float] = None, color:str = 'red',
       ymin: float = 0, ymax: Optional[float] = None,
       xlabel: str = 'Mass (Da)', ylabel: str = 'ion intensity'):
    masses, intensities = extract_masses_intensities(filepath)
    fig, ax = plt.subplots()
    if title: plt.title(title, pad=25)
    ax.plot(masses, intensities, linewidth=2, color=color)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0),
                     useMathText=True)
    ax.yaxis.set_major_formatter(latex_sci_formatter)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--xmin', type=float, default=500)
    parser.add_argument('--xmax', type=float, default=None)
    parser.add_argument('--color', type=str, default='red')
    parser.add_argument('--ymin', type=float, default=0)
    parser.add_argument('--ymax', type=float, default=None)
    parser.add_argument('--xlabel', type=str, default='Mass (Da)')
    parser.add_argument('--ylabel', type=str, default='ion intensity')
    args = parser.parse_args()
    make_figure(
        args.filepath, title=args.title, xmin=args.xmin,
        xmax=args.xmax, color=args.color, ymin=args.ymin,
        ymax=args.ymax, xlabel=args.xlabel, ylabel=args.ylabel
    )