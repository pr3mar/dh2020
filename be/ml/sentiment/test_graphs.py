# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:57:51 2020

@author: Bosec
"""


import d3py
import networkx as nx

import logging
logging.basicConfig(level=logging.DEBUG)

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(4,2)

# use 'with' if you are writing a script and want to serve this up forever
with d3py.NetworkXFigure(G, width=500, height=500) as p:
    p += d3py.ForceLayout()
    p.show()