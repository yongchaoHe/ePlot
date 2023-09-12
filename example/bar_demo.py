#! /usr/local/bin/python3.9
# -*- coding: UTF-8 -*-

from eplot.axis import axis
from eplot.figure import Figure

def demo_1():
    legends = ["Line 1", "Line 2", "Line 3", "Line 4"]
    data = [
        [
            ([item for item in range(11)], [0.2*item for item in range(11)]),
            ([item for item in range(11)], [0.4*item for item in range(11)]),
            ([item for item in range(11)], [0.6*item for item in range(11)]),
            ([item for item in range(11)], [0.8*item for item in range(11)])
        ]
    ]
    xaxis = axis(
        "X-axis", -0.5, 10.5,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"]
    )
    yaxis = axis(
        "Y-axis", 0, 10,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"]
    )

    xyaxis = [
        (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(True, 2)]

    myfig = Figure(1, 1, 4, 2.5, lwidth=1.5, alpha=0.8, legend_size=-1, fig_name="bar_demo_1", ggplot=False)
    myfig.set_legends(legends, ncol_legend=2, loc_legend=100, adjust_legend=0.75)
    myfig.plot_bar(data, xyaxis, hline, use_hatch=True)

def demo_2():
    legends = ["Line 1", "Line 2", "Line 3", "Line 4"]

    data = [
        [
            ([item for item in range(11)], [0.2*item for item in range(11)]),
            ([item for item in range(11)], [0.4*item for item in range(11)]),
            ([item for item in range(11)], [0.6*item for item in range(11)]),
            ([item for item in range(11)], [0.8*item for item in range(11)])
        ],
        [
            ([item for item in range(11)], [(0.2*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.4*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.6*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.8*item, 0.1*item) for item in range(11)])
        ],
        [
            ([item for item in range(11)], [(item/2, 0.5) for item in range(11)], [(2, 0.5) for item in range(11)]),
            ([item for item in range(11)], [(item/2, 0.5) for item in range(11)], [(2, 0.5) for item in range(11)]),
            ([item for item in range(11)], [(item/2, 0.5) for item in range(11)], [(2, 0.5) for item in range(11)]),
            ([item for item in range(11)], [(item/2, 0.5) for item in range(11)], [(2, 0.5) for item in range(11)])
        ],
        [
            ([item for item in range(11)], [(0.2*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.4*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.6*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.8*item, 1) for item in range(11)])
        ],
    ]

    xaxis = axis(
        "X-axis", -0.5, 10.5,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"]
    )
    yaxis = axis(
        "Y-axis", 0, 10,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"]
    )

    xyaxis = [
        (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(True, 2), (False, 0), (True, 6), (False, 0)]

    myfig = Figure(2, 2, 8, 5, lwidth=1.5, alpha=0.8, legend_size=-1, fig_name="bar_demo_2", ggplot=False)
    myfig.set_legends(legends, ncol_legend=4, loc_legend=100, adjust_legend=0.9)
    myfig.plot_bar(data, xyaxis, hline, use_hatch=True)

def demo_3():
    legends = [
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"],
        ["Line 1", "Line 2", "Line 3", "Line 4"]
    ]

    data = [
        [
            ([item for item in range(11)], [item/2 for item in range(11)], [2 for item in range(11)]),
            ([item for item in range(11)], [item/2 for item in range(11)], [2 for item in range(11)]),
            ([item for item in range(11)], [item/2 for item in range(11)], [2 for item in range(11)]),
            ([item for item in range(11)], [item/2 for item in range(11)], [2 for item in range(11)])
        ],
        [
            ([item for item in range(11)], [(0.2*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.4*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.6*item, 0.1*item) for item in range(11)]),
            ([item for item in range(11)], [(0.8*item, 0.1*item) for item in range(11)])
        ],
        [
            ([item for item in range(11)], [0.2*item for item in range(11)]),
            ([item for item in range(11)], [0.4*item for item in range(11)]),
            ([item for item in range(11)], [0.6*item for item in range(11)]),
            ([item for item in range(11)], [0.8*item for item in range(11)])
        ],
        [
            ([item for item in range(11)], [(0.2*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.4*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.6*item, 1) for item in range(11)]),
            ([item for item in range(11)], [(0.8*item, 1) for item in range(11)])
        ],
    ]

    xaxis = axis(
        "X-axis", -0.5, 10.5,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"],
        ax_figname="SubFig"
    )
    yaxis = axis(
        "Y-axis", 0, 10,
        [item for item in range(0, 11)],
        ["0", "", "2", "", "4", "", "6", "", "8", "", "10"]
    )

    xyaxis = [
        (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis), (xaxis, yaxis)
    ]

    # will be ignored if hline = []
    hline = [(True, 2), (False, 0), (True, 6), (False, 0)]

    myfig = Figure(2, 2, 8, 5, lwidth=1.5, alpha=0.8, legend_size=-1, fig_name="bar_demo_3", ggplot=True)
    myfig.set_legends(legends, ncol_legend=1, loc_legend=100, adjust_legend=0.9)
    myfig.plot_bar(data, xyaxis, hline, use_hatch=True)

if __name__ == '__main__':
    demo_1()
    demo_2()
    demo_3()

