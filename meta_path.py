import pickle as pkl 
import networkx as nx 
from graph import *
from utils import *
import numpy as np 

def meta_path():
    f=open('./data/h2id.dict','rb')
    h2id=pkl.load(f)
    f.close()

    f=open('./data/s2id.dict','rb')
    s2id=pkl.load(f)
    f.close()

    g=Graph()
    g.read_edgelist('./data/s_h.edgelist')

    adj=getAdj(g)

    num_s=len(s2id)
    num_h=len(h2id)

    s_h=adj[:num_s,num_s:] #189*357

    h_s=s_h.T #357*189

    s_s=np.matmul(s_h,h_s) #189*189
    h_h=np.matmul(h_s,s_h) #357*357

    tmp1=np.hstack((s_s,s_h)) #189*546
    tmp2=np.hstack((h_s,h_h)) #357*546

    meta_path_matrix=np.vstack((tmp1,tmp2))
    return meta_path_matrix

if __name__=='__main__':
    a=meta_path()
    print(a)