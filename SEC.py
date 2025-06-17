from custom_plt import plt
import numpy as np
import argparse
from typing import Optional

def data_from_csv_file(filepath: str):
    with open(filepath, encoding='utf-16') as file:
        mls, maus = [], []
        lines = file.readlines()[3:]
        for line in lines:
            ml, mau = line.split()[:2]
            ml, mau = float(ml), float(mau)
            mls.append(ml); maus.append(mau)
    return np.array(mls), np.array(maus)

def make_figure(filepath: str, title: str = '', xmin: Optional[float] = None,
       xmax: Optional[float] = None, color:str = 'black',
       ymin: float = 0, ymax: Optional[float] = None):
    mls, maus = data_from_csv_file(filepath)
    if title: plt.title(title, pad=25)
    fig, ax = plt.subplots()
    ax.plot(mls, maus, linewidth=2, color=color)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--xmin', type=float, default=None)
    parser.add_argument('--xmax', type=float, default=None)
    parser.add_argument('--color', type=str, default='black')
    parser.add_argument('--ymin', type=float, default=0)
    parser.add_argument('--ymax', type=float, default=None)
    args = parser.parse_args()
    make_figure(
        args.filepath, title=args.title, xmin=args.xmin,
        xmax=args.xmax, color=args.color, ymin=args.ymin,
        ymax=args.ymax
    )

make_figure('/Users/jack/Downloads/SEC N40C-PDL1 190924 real run 001.csv')