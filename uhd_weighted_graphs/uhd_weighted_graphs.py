from algorithms.prims import prims_algorithm
from functions.Initial_Graph import *
import networkx as nx


T = prims_algorithm(G, int(input('Choose a node:')), draw = True, attrib = True)

