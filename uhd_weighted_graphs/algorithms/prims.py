import networkx as nx
from functions.drawings import draw_subtree
from functions.prims_functions import cost, min_prims_edges

def prims_algorithm(G, starting_node, draw = False, attrib = False):
    
    T = nx.Graph()
    T.add_node(starting_node)
    
    if draw == True:
        draw_subtree(G, T)
        
    while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edges(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        if draw == True:
            draw_subtree(G, T)
            
    
    if attrib == True:
        total_cost = sum(cost(G, e) for e in T.edges())
        print('')
        print('_______________PROPERTIES OF THE TREE T___________________')
        print('__________________________________________________________')
        print(f'V(T) = {list(T.nodes())}')
        print(f'V(T) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print('__________________________________________________________')
        
    return T
        