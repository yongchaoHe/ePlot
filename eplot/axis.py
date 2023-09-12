#! /usr/local/bin/python3.9
# -*- coding: UTF-8 -*-

##
#
# x_axis = axis("x_axis", 0, 10, [item for item in range(0, 11)], ["0", "", "2", "", "4", "", "6", "", "8", "", "10"])
# y_axis = axis("", 0, 20, [item for item in range(0, 5)], ["0", "5", "10", "15", "20"])
#
#  20 +-----------------------------+
#     |                             |
#  15 +                             |
#     |                             |
#  10 +                             |
#     |                             |
#   5 +                             |
#     |                             |
#   0 +--+--+--+--+--+--+--+--+--+--+
#     0     2     4     6     8     10
#                x_axis
#
# #

class axis:
    def __init__(self, ax_label, ax_min, ax_max, ax_ticks, ax_ticklabels, ax_scale="linear", ax_figname=""):
        self.label      = ax_label
        self.min        = ax_min
        self.max        = ax_max
        self.ticks      = ax_ticks
        self.ticklabels = ax_ticklabels
        self.scale      = ax_scale
        self.figname    = ax_figname
