import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def show_weighted_graph(G):                                   # defines and displays the weighted graph
    pos = nx.planar_layout(G)
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels)
    plt.show()
   

def draw_subtree(G, T):                                      # defines and displays the sub-graph
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,                          #displays the labels of edges of the Sub-Graph
                                 pos,
                                 edge_labels = labels,)
    nx.draw_networkx_edges(G, pos,                           #displays the edges of the Sub-Graph
                            edgelist=T.edges(),
                            width=8, alpha=0.5,
                            edge_color='r',)
    nx.draw_networkx_nodes(G,                               #displays the nodes of theSub- Graph
                           pos,
                           nodelist=T.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)
    plt.show()
