import pickle as pkl
import networkx as nx
from graph import *

# g=Graph()
# g.read_edgelist('./data/s_h.edgelist')
# print(g.G.number_of_nodes()) #546

f=open('./data/h2id.dict','rb')
h2id=pkl.load(f)
f.close()

f=open('./data/s2id.dict','rb')
s2id=pkl.load(f)
f.close()

print(len(h2id))
print(len(s2id))
print(len(h2id)+len(s2id))