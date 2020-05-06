import networkx as nx

print('')
print("-----------------PRIM'S ALGORITHIM----------------")
print('')
print('--------------------------------------------------')
print('')
print('The available graphs to select are G1, G2, or G3')
print('')
print("Initialize Prim's Algorithim below")
print('')
print('--------------------------------------------------')
choose_graph = input('Select one of the graphs by typing either G1, G2, or G3 here: ')


# If the user selected G1 then it set the intial graph

if choose_graph == 'G1':
    print('')
    
    G = nx.read_weighted_edgelist('data/G1.txt',
                              nodetype = int)
    
# If the user selected G2 then it set the intial graph
    
if choose_graph == 'G2':
    print('')
    
    G = nx.read_weighted_edgelist('data/G2.txt',
                              nodetype = int)
    
# If the user selected G3 then it set the intial graph
    
if choose_graph == 'G3':
    print('')

    
    G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
