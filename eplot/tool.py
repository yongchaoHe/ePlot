#! /usr/local/bin/python3.9
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

'''
Convert RGB to Hex
'''
def RGB2Hex(R=255, G=255, B=255):
    color = "#"
    color += str(hex(R)).replace('x','0')[-2:]
    color += str(hex(G)).replace('x','0')[-2:]
    color += str(hex(B)).replace('x','0')[-2:]
    return color

'''
Color used in all kinds of graphs
'''
# Option 1:
# matplotlib color, refer to https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_prop_cycle.html
mat_colors  = plt.rcParams['axes.prop_cycle'].by_key()['color']
r_ggplot2_set1 = [
    (239, 0  , 0  ),
    (0  , 127, 255),
    (255, 165, 0  ),
    (77 , 175, 74 ),
    (148, 0  , 211),
    (255, 127, 0  ),
    (255, 218, 78 ),
    (255, 108, 145),
    (127, 184, 14 )
]
# r_ggplot2_set1 = [(250, 127, 111), (122,107,245), (255,190,122), (155, 195, 125), (255,127,0), (243,210,102), (50, 184, 151), (166, 118, 118)]
# colors = mat_colors
colors = [RGB2Hex(item[0], item[1], item[2]) for item in r_ggplot2_set1]

'''
Default markers in the line graph
Refer to https://matplotlib.org/stable/api/markers_api.html
'''
markers = ['o', 's', 'd', '+', 'h', 'p', '.', 'D']

'''
Default hatches in the bar graph
https://matplotlib.org/devdocs/gallery/shapes_and_collections/hatch_style_reference.html
'''
hatches = ['///', '\\\\\\', '.', "--", 'o', '*', 'x', '++']

'''
Default line styles in the line graph
Refer to https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
'''
linestyles = [
    ('line_1',                (0, (6, 0))),
    ('line_1',                (0, (6, 1, 3, 1, 2, 1))),
    ('dotted',                (0, (3, 1, 3, 1))),
    ('dashed',                (0, (3, 1, 1, 1, 1, 1))),
    ('dashdotted',            (0, (3, 5, 1, 5))),
    ('densely dashed',        (0, (5, 1))),
    ('densely dashdotted',    (0, (3, 1, 1, 1))),
    ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
    ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1))),
    '''
    More refined control can be achieved by providing a dash tuple (offset, (on_off_seq)).
    For example, (0, (3, 10, 1, 15)) means (3pt line, 10pt space, 1pt line, 15pt space) with no offset.
    '''
]

def hello():
    print("Hello, ePlot!")
