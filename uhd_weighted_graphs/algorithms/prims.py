import networkx as nx           # package required to build graphs and sub-graphs
from functions.drawings import draw_subtree    #File imported from the draw_subtree
from functions.prims_functions import cost, min_prims_edges      #File imported from the Prims_functions

def prims_algorithm(G, starting_node, draw = False, attrib = False):           # Defining Prim's Algorithm
    
    T = nx.Graph()
    T.add_nodes(starting_node)
    
    if draw == True:                                                           # draws the sub graph with minimum cost
        draw_subtree(G, T)
        
    while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edges(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        if draw == True:
            draw_subtree(G, T)
            
    
    if attrib == True:                                                        # defines and returns the Total cost,  
        total_cost = sum(cost(G, e) for e in T.edges())                       # the number of edges,
        print('')                                                             # and its corresponding weights of the sub-graph.  
        print('_______________PROPERTIES OF THE TREE T___________________')    
        print('__________________________________________________________')
        print(f'V(T) = {list(T.nodes())}')
        print(f'V(T) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print('__________________________________________________________')
        
    return T
        
