#! /usr/local/bin/python3.9
# -*- coding: UTF-8 -*-

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *
import matplotlib.gridspec as gridspec
import re
import os
import math
import numpy as np

from .axis import *
from .tool import *

class Figure:
    def __init__(self, row, col, width, height, fsize=10, axissize=-1, legend_size=-1, lwidth=1, msize=3, alpha=1, fig_name="", ggplot=True, no_legend=False):
        self.row      = row
        self.col      = col
        self.width    = width
        self.height   = height
        self.fsize    = fsize
        self.msize    = msize    # marker size
        self.alpha    = alpha    # color alpha
        self.fig_name = fig_name
        self.ggplot   = ggplot
        self.no_legend= False
        if legend_size != -1:
            self.legend_size = legend_size
        else:
            self.legend_size = self.fsize

        if axissize != -1:
            self.axissize = axissize
        else:
            self.axissize = self.fsize

        matplotlib.rcParams['ps.useafm']          = True
        matplotlib.rcParams['pdf.use14corefonts'] = True
        matplotlib.rcParams['text.usetex']        = True
        matplotlib.rcParams['font.size']          = fsize
        # matplotlib.rcParams.update({'font.size': fsize})
        matplotlib.rcParams['lines.linewidth']    = lwidth
        if self.ggplot == True:
            plt.style.use('ggplot')
        self.set_font()

    '''
    Set default font style and size
    Refer to https://matplotlib.org/stable/tutorials/text/text_props.html#default-font
    '''
    def set_font(self):
        matplotlib.rcParams['font.family']  = 'serif'    # 'cursive', 'fantasy', 'monospace', 'sans', 'sans serif', 'sans-serif', 'serif'
        matplotlib.rcParams['font.style']   = 'normal'   # 'normal', 'italic'
        # matplotlib.rcParams["font.variant"] = "normal" # 'normal', ''
        # matplotlib.rcParams["font.stretch"] = "normal" # 'normal', ''
        # 'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'
        # matplotlib.rcParams['font.weight']  = 'black'
        matplotlib.rcParams['font.size']    = self.fsize

        # matplotlib.rcParams['font.sans-serif']=['Songti']
        # matplotlib.rcParams['axes.unicode_minus']=False

    '''
    Legend related settings
    Refer to https://matplotlib.org/stable/api/legend_api.html
    '''
    def set_legends(self, legends, ncol_legend=0, loc_legend=100, adjust_legend=0.9):
        if type(legends[0]) == list:
            # Generate a legend for each sub-figure
            self.share_legend = False
        else:
            # All subfigures share a legend
            self.share_legend = True
        self.legends       = legends
        self.ncol_legend   = ncol_legend
        self.loc_legend    = loc_legend
        self.adjust_legend = adjust_legend
        if ncol_legend == 0:
            if self.share_legend == True:
                self.ncol_legend = len(legends)
            else:
                self.ncol_legend = len(legends[0])
        if loc_legend == 100:
            if self.share_legend == True:
                self.loc_legend = 'upper center'
            else:
                self.loc_legend = 0

    '''
    axis related settings
    '''
    def set_axis(self, ax, xyaxis, hline=[], loop=0, x_log=False, y_log=False):
        x_axis = xyaxis[0]
        y_axis = xyaxis[1]
        if x_log == True:
            if x_axis.min == 0:
                print("Warning: x_axis.min cannot set to be 0 when x_log=True")
                x_axis.min = 1
            ax.set_xscale("log")
        if y_log == True:
            if y_axis.min == 0:
                print("Warning: y_axis.min cannot set to be 0 when y_log=True")
                y_axis.min = 1
            ax.set_yscale("log")

        if self.col * self.row > 1:
            if x_axis.figname == "":
                ax.set_xlabel("(" + chr(97+loop) + ") " + x_axis.label)
            else:
                ax.set_xlabel(x_axis.label + "\n" + "(" + chr(97+loop) + ") " + x_axis.figname)
            # ax.set_xlabel(x_axis.label)
        else:
            ax.set_xlabel(x_axis.label)
        ax.set_xlim(x_axis.min, x_axis.max)
        ax.set_xticks(x_axis.ticks)
        ax.set_xticklabels(x_axis.ticklabels, rotation=x_axis.rotation)
        ax.set_xticklabels(x_axis.ticklabels)
        ax.set_ylabel(y_axis.label)
        ax.set_ylim(y_axis.min, y_axis.max)
        ax.set_yticks(y_axis.ticks)
        ax.set_yticklabels(y_axis.ticklabels)

        if len(hline) > 0:
            if hline[loop][0] == True:
                ax.plot([x_axis.min, x_axis.max], [hline[loop][1], hline[loop][1]], color="red", ls=":")

        if self.share_legend == False and self.no_legend == False:
            ax.legend(loc=self.loc_legend, ncol=self.ncol_legend, prop={'size': self.legend_size})

    '''
    yongchao style
    '''
    def set_no_frame(self, ax):
        '''
        for key, spine in ax.spines.items():
            # 'left', 'right', 'bottom', 'top'
            if key == 'right' or key == 'top' or key == 'left' or 'bottom':
                spine.set_visible(False)
        '''
        # https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params
        # ax.tick_params(axis=u'both', which=u'both', length=0)
        ax.tick_params(direction="in")
        if self.ggplot == False:
            ax.xaxis.grid(ls=":", alpha=1, linewidth=1)
            ax.yaxis.grid(ls=":", alpha=1, linewidth=1)

    def plot_start(self):
        fig, axList = plt.subplots(self.row, self.col, figsize=(self.width, self.height))
        axes = []
        for row_loop in range(0, self.row):
            for col_loop in range(0, self.col):
                if self.row == 1 and self.col == 1:
                    ax = axList
                elif self.row == 1:
                    ax = axList[col_loop]
                elif self.col == 1:
                    ax = axList[row_loop]
                else:
                    ax = axList[row_loop][col_loop]
                self.set_no_frame(ax)
                axes.append(ax)
        return fig, axes

    def plot_end(self, fig, lines, fig_name):
        plt.tight_layout()
        if self.share_legend == True:
            fig.legend(lines, self.legends, loc=self.loc_legend, prop={'size': self.legend_size}, borderaxespad=0.6, ncol=self.ncol_legend)
            plt.subplots_adjust(top=self.adjust_legend)
        pp = PdfPages(fig_name + ".pdf")
        pp.savefig()
        pp.close()
        print("[INFO] Generating figure " + fig_name + ".pdf")

    def plot_line(self, data, xyaxis, hline, use_marker=True, ls_plain=False, xlog=False):
        if self.row * self.col != len(data):
            print("len(data)=" + str(len(data)) + ", but row*col=" + str(self.row) + "*" + str(self.col))
            return
        fig, axes = self.plot_start()
        lines     = []
        for loop in range(len(axes)):
            ax       = axes[loop]
            sub_data = data[loop]
            # lines    = []
            for line_loop in range(len(sub_data)):
                plot_func = ""
                if len(sub_data[line_loop][1]) == 0:
                    continue
                if type(sub_data[line_loop][1][0]) == tuple:
                    plot_func = plot_func + "ax.errorbar(sub_data[line_loop][0], [item[0] for item in sub_data[line_loop][1]], yerr=[item[1] for item in sub_data[line_loop][1]], "
                else:
                    plot_func = plot_func + "ax.plot(sub_data[line_loop][0], sub_data[line_loop][1], "
                if ls_plain == True:
                    plot_func = plot_func + "ls='-', "
                elif use_marker == True:
                    plot_func = plot_func + "marker=markers[line_loop%len(markers)], markersize=self.msize, markerfacecolor='white', "
                else:
                    plot_func = plot_func + "ls=linestyles[line_loop][1], "
                if self.share_legend == False:
                    plot_func = plot_func + "label=self.legends[loop][line_loop], "
                plot_func = plot_func + "color=colors[line_loop%len(colors)], alpha=self.alpha)"
                l = eval(plot_func)
                if len(lines) > line_loop:
                    lines[line_loop] = l[0]
                else:
                    lines.append(l[0])
            self.set_axis(ax, xyaxis[loop], hline, loop, x_log=xlog, y_log=False)
        self.plot_end(fig, lines, self.fig_name)

    def plot_bar(self, data, xyaxis, hline, edge=0.05, total_width=0.9, use_hatch=True):
        if self.row * self.col != len(data):
            print("len(data)=" + str(len(data)) + ", but row*col=" + str(self.row) + "*" + str(self.col))
            return
        fig, axes = self.plot_start()
        lines     = []
        for loop in range(len(axes)):
            ax       = axes[loop]
            sub_data = data[loop]
            lines    = []
            n = len(sub_data)
            width = total_width / n
            for line_loop in range(len(sub_data)):
                x_data = [(item - (total_width - width) / 2 + line_loop * width) for item in sub_data[line_loop][0]]
                plot_func = "ax.bar(x_data, "
                if type(sub_data[line_loop][1][0]) == tuple:
                    plot_func = plot_func + "[item[0] for item in sub_data[line_loop][1]], yerr=[item[1] for item in sub_data[line_loop][1]], ecolor=colors[line_loop%len(colors)], "
                else:
                    plot_func = plot_func + "sub_data[line_loop][1], "
                if use_hatch == True:
                    plot_func = plot_func + "hatch=hatches[line_loop%len(hatches)], "
                if self.share_legend == False and self.no_legend == False:
                   plot_func = plot_func + "label=self.legends[loop][line_loop], "
                # plot_func = plot_func + "width=width, edgecolor='white', color=self.colors[line_loop%len(self.colors)], alpha=self.alpha)"
                plot_func = plot_func + "width=width, edgecolor='white', color=colors[line_loop%len(colors)], alpha=self.alpha)"
                l = eval(plot_func)
                lines.append(l[0])

                # Stack bar
                if len(sub_data[line_loop]) > 2:
                    plot_func = "ax.bar(x_data, "
                    if type(sub_data[line_loop][2][0]) == tuple:
                        # plot_func = plot_func + "[item[0] for item in sub_data[line_loop][2]], yerr=[item[1] for item in sub_data[line_loop][2]], ecolor=colors[line_loop%len(colors)], bottom=[item[0] for item in sub_data[line_loop][1]], "
                        plot_func = plot_func + "[item[0] for item in sub_data[line_loop][2]], yerr=[item[1] for item in sub_data[line_loop][2]], ecolor=colors[line_loop%len(colors)], bottom=[item[0] for item in sub_data[line_loop][1]], "
                    else:
                        plot_func = plot_func + "sub_data[line_loop][2], bottom=sub_data[line_loop][1], "
                    if use_hatch == True:
                        plot_func = plot_func + "hatch=hatches[line_loop%len(hatches)], "
                    # if self.share_legend == False:
                    #     plot_func = plot_func + "label=self.legends[loop][line_loop], "
                    plot_func = plot_func + "width=width-" + str(edge) + ", edgecolor=colors[line_loop%len(colors)], color='white', alpha=self.alpha)"
                    l = eval(plot_func)
            self.set_axis(ax, xyaxis[loop], hline, loop, x_log=False, y_log=False)
        self.plot_end(fig, lines, self.fig_name)

    def plot_cdf(self, data, xyaxis, hline, xlog=False, ylog=False):
        if self.row * self.col != len(data):
            print("len(data)=" + str(len(data)) + ", but row*col=" + str(self.row) + "*" + str(self.col))
            return
        percentiles = [0, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999, 0.9999, 0.99999, 1]
        fig, axes = self.plot_start()
        lines     = []
        for loop in range(len(axes)):
            ax       = axes[loop]
            sub_data = data[loop]
            lines    = []
            for line_loop in range(len(sub_data)):
                rtt = sub_data[line_loop]
                rtt = sorted(rtt)
                ys = [(float)(j+1)/len(rtt) for j in range(len(rtt))]
                plot_func = "ax.plot(rtt, ys, "
                # plot_func = plot_func + "ls=self.linestyles[line_loop][1], "
                # if self.share_legend == False:
                #     plot_func = plot_func + "label=self.legends[loop][line_loop], "
                plot_func = plot_func + "color=colors[line_loop%len(colors)], alpha=self.alpha)"
                l = eval(plot_func)

                points = [rtt[int(item*len(rtt))] for item in percentiles[:-1]] + [rtt[-1]]

                ax.plot(points, percentiles, markers[line_loop%len(markers)], color=colors[line_loop%len(colors)], markersize=self.msize, markerfacecolor='white')
                plot_func = "ax.plot([],[], marker=markers[line_loop%len(markers)], color=colors[line_loop%len(colors)], markersize=self.msize, markerfacecolor='white'"
                if self.share_legend == False:
                    plot_func = plot_func + ", label=self.legends[loop][line_loop]"
                plot_func = plot_func + ")"
                l = eval(plot_func)

                lines.append(l[0])
            self.set_axis(ax, xyaxis[loop], hline, loop, x_log=xlog, y_log=ylog)
        self.plot_end(fig, lines, self.fig_name)
