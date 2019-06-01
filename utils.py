import numpy as np
from graph import *

def getAdj(g):
    node_size = g.node_size
    look_up = g.look_up_dict
    adj = np.zeros((node_size, node_size))
    for edge in g.G.edges():
        adj[look_up[edge[0]]][look_up[edge[1]]] = g.G[edge[0]][edge[1]]['weight']
    return adj