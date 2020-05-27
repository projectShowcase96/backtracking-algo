# how to use dictionary with networkx: stackoverflow - 44540458

# # importing networkx  
from networkx import nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 


# test - 1
# dictionary of graph vertices and edges
# adjacency_matrix = {

#     'A' : ['B', 'C'],
#     'B' : ['A', 'C', 'D'],
#     'C' : ['A', 'B', 'E'],
#     'D' : ['B', 'E', 'F'],
#     'E' : ['C', 'D'],
#     'F' : ['D']
# }


# test - 2
# dictionary of graph vertices and edges
adjacency_matrix = {

    'A' : ['B', 'C'],
    'B' : [],
    'C' : ['D'],
    'D' : ['E'],
    'E' : ['G'],
    'G' : []
}


G = nx.Graph(adjacency_matrix)
nx.draw(G, with_labels=True)
plt.savefig("graph/directed_graph1.png") 
# plt.show()


# # clearing the current plot 
# plt.clf() 