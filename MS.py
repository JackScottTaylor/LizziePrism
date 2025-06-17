from typing import List, Optional
import numpy as np
from matplotlib.ticker import MaxNLocator
import argparse
import sys

from custom_plt import plt

def data_from_txt_file(filepath: str) -> List[np.ndarray]:
    '''
    Reads the mass and intensity data from a .txt file and returns the two
    data sets as numpy arrays.
    .txt format is 
    mass space intensity two new lines

    :param filepath: The filepath to the .txt file
    '''
    masses, intensities = [], []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            sline = line.split()
            if not sline: continue
            mass, intensity = sline
            mass, intensity = float(mass), float(intensity)
            masses.append(mass); intensities.append(intensity)
    return np.array(masses), np.array(intensities)

def normalise_intensities(intensities: np.ndarray) -> np.ndarray:
    minimum = min(intensities)
    intensities = intensities - minimum
    maximum = max(intensities)
    intensities = (intensities / maximum) * 100
    return intensities

def make_figure(filepath: str, title: str = '', xmin: Optional[float] = None,
       xmax: Optional[float] = None, color:str = 'red',
       ymin: float = 0, ymax: float = 100,
       xticks = 3, yticks=2, npeaks: int = 1):
    m, i = data_from_txt_file(filepath)
    i = normalise_intensities(i)

    nindices = np.argsort(i)[-npeaks:]
    line = '-' * 30
    print(line)
    print('Most Intense Peaks:')
    print(line)
    for index in nindices[::-1]:
        print(f'Mass: {m[index]}   Intensity: {i[index]:.1f}')
    print(line)

    plt.plot(m, i, color=color, zorder=999)
    if title: plt.title(title, pad=25)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xlabel('Mass (Da)')
    plt.ylabel('Relative Intensity (%)')
    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(nbins=xticks))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=yticks))
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--xmin', type=float, default=None)
    parser.add_argument('--xmax', type=float, default=None)
    parser.add_argument('--color', type=str, default='red')
    parser.add_argument('--ymin', type=float, default=0)
    parser.add_argument('--ymax', type=float, default=100)
    parser.add_argument('--yticks', type=float, default=2)
    parser.add_argument('--xticks', type=float, default=3)
    parser.add_argument('--npeaks', type=int, default=1)
    args = parser.parse_args()
    make_figure(
        args.filepath, title=args.title, xmin=args.xmin,
        xmax=args.xmax, color=args.color, ymin=args.ymin,
        ymax=args.ymax, xticks=args.xticks, yticks=args.yticks,
        npeaks=args.npeaks
    )