# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 06:50:25 2023

@author: Serkanburakors
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the cost matrix
costMatrix = np.array([
    [np.inf, 3, 2, np.inf, 4, np.inf, np.inf, np.inf, np.inf],                #S
    [np.inf, np.inf, np.inf, 2, np.inf, 1, np.inf, np.inf, np.inf],           #1
    [np.inf, np.inf, np.inf, 5, 1, np.inf, np.inf, np.inf, np.inf],           #2
    [np.inf, np.inf, np.inf, np.inf, np.inf, 3, 2, np.inf, np.inf],           #3
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 3, 8, np.inf],           #4
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 3, np.inf, 7],           #5
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 4],      #6
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 1],      #7
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf,np.inf]]) #T

# Define the index of the initial and final nodes
indexInitial = 0
indexFinal = 8

# Initialize variables
n = costMatrix.shape[0]
S = np.zeros(n, dtype=bool)
dist = np.full(n, np.inf)
prev = np.full(n, n+1)

dist[indexInitial] = 0

# Dijkstra's algorithm
while not np.all(S):
    candidate = np.where(~S, dist, np.inf)
    u = np.argmin(candidate)
    S[u] = True
    for v in range(n):
        if not S[v] and dist[u]+costMatrix[u,v] < dist[v]:
            dist[v] = dist[u] + costMatrix[u,v]
            prev[v] = u

# Find the shortest path and its cost
path = [indexFinal]
while path[0] != indexInitial:
    if prev[path[0]] <= n:
        path.insert(0, prev[path[0]])
    else:
        raise Exception('No path exists')
totalCost = dist[indexFinal]

# Create a graph of the network
G = nx.DiGraph()
for i in range(n):
    for j in range(n):
        if costMatrix[i,j] < np.inf:
            G.add_edge(i, j, weight=costMatrix[i,j])

# Create a dictionary of node labels
node_labels = {i: f'{i+1}' for i in range(n)}
node_labels[indexInitial] = 'S'
node_labels[indexFinal] = 'T'

# Create a list of edge labels
edge_labels = {(i,j): f'{costMatrix[i,j]}' for (i,j) in G.edges}

shortest_path = nx.shortest_path(G, source=indexInitial, target=indexFinal, weight='weight')

# Draw the graph with edge labels and node labels
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
labels = {0: 'S', 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8:'T'}
nx.draw_networkx_labels(G, pos, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='r', width=2)
plt.axis('off')
plt.show()

#Print the results
print('Optimal path is:S -', shortest_path[1],'-',shortest_path[2],'-',shortest_path[3],'-','T')
print('Optimal cost is', nx.shortest_path_length(G, source=indexInitial, target=indexFinal, weight='weight'))
