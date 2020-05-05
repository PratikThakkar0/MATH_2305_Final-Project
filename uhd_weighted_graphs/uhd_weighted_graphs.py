from algorithms.prims import prims_algorithm
import networkx as nx

G = nx.read_weighted_edgelist('data/G2.txt', nodetype = int)

T = prims_algorithm(G, 0, draw = True, attrib = True)

