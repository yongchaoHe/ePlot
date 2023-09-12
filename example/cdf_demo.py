#! /usr/local/bin/python3.9
# -*- coding: UTF-8 -*-

import math
import numpy as np

from eplot.axis import axis
from eplot.figure import Figure

def demo_1():
    legends = ["Line 1", "Line 2", "Line 3", "Line 4"]

    data = [
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ]
    ]

    xaxis = axis(
        "X-axis", 1, 10000,
        [10**item for item in range(0, 5)],
        [r'$10^{0}$', r'$10^{1}$', r'$10^{2}$', r'$10^{3}$', r'$10^{4}$']
    )
    yaxis = axis(
        "Y-axis", 0, 1,
        [0.1*item for item in range(0, 11)],
        ["0", "", "0.2", "", "0.4", "", "0.6", "", "0.8", "", "1"]
    )
    xyaxis = [
        (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(False, 2)]

    myfig = Figure(1, 1, 4, 2.5, lwidth=1.5, alpha=0.8, fig_name="cdf_demo_1", ggplot=False)
    myfig.set_legends(legends, ncol_legend=2, loc_legend=100, adjust_legend=0.75)
    myfig.plot_cdf(data, xyaxis, hline, xlog=True)

def demo_2():
    legends = ["Line 1", "Line 2", "Line 3", "Line 4"]

    data = [
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
    ]

    xaxis = axis(
        "X-axis", 1, 10000,
        [10**item for item in range(0, 5)],
        [r'$10^{0}$', r'$10^{1}$', r'$10^{2}$', r'$10^{3}$', r'$10^{4}$']
    )
    yaxis = axis(
        "Y-axis", 0, 1,
        [0.1*item for item in range(0, 11)],
        ["0", "", "0.2", "", "0.4", "", "0.6", "", "0.8", "", "1"]
    )
    xyaxis = [
        (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(True, 0.2), (True, 0.6), (True, 0.6), (True, 0.8)]

    myfig = Figure(2, 2, 8, 5, lwidth=1.5, alpha=0.8, fig_name="cdf_demo_2", ggplot=False)
    myfig.set_legends(legends, ncol_legend=4, loc_legend=100, adjust_legend=0.9)
    myfig.plot_cdf(data, xyaxis, hline, xlog=True)

def demo_3():
    legends = [
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"]
    ]

    data = [
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
        [
            np.random.normal(5, 1, 1000),
            np.random.normal(50, 10, 1000),
            np.random.normal(500, 100, 1000),
            np.random.normal(5000, 1000, 1000)
        ],
    ]

    xaxis = axis(
        "X-axis", 1, 10000,
        [10**item for item in range(0, 5)],
        [r'$10^{0}$', r'$10^{1}$', r'$10^{2}$', r'$10^{3}$', r'$10^{4}$'],
        ax_figname="SubFig"
    )
    yaxis = axis(
        "Y-axis", 0, 1,
        [0.1*item for item in range(0, 11)],
        ["0", "", "0.2", "", "0.4", "", "0.6", "", "0.8", "", "1"]
    )
    xyaxis = [
        (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(True, 0.2), (True, 0.6), (True, 0.6), (True, 0.8)]

    myfig = Figure(2, 2, 8, 5, lwidth=1.5, alpha=0.8, fig_name="cdf_demo_3", ggplot=True)
    myfig.set_legends(legends, ncol_legend=1, loc_legend=100, adjust_legend=0.9)
    myfig.plot_cdf(data, xyaxis, hline, xlog=True)

if __name__ == '__main__':
    demo_1()
    demo_2()
    demo_3()
