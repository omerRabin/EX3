# EX3
Hello, you have arrived at Eldad and Omar's project on the subject of weighted directed graphs written in Python.\
In our project we built software that produces deliberate weighted graphs and allows you to make changes to them and even various algorithms.\
In addition during the project we made comparisons between the runtimes of the functions in our algorithm class to the algorithm Class of the network-X to\
the algorithm class of our preivious Project in Java. \
The main algorithm we used in this project is DFS. we used Dijkstra to find the shortest path from two nodes in the graph.\
In addition, we used DFS to find a SCC of node and all the SCC's in the graph. SCC is the strongest connected component. \
Our project consists of several classes that create the graphic system:\
The main classes is: DiGraph, GraphAlgo.\
# DiGraph:\
|Method|Complexity|Description|
|----|------|---------|
|v_size|O(1) | Returns the number of vertices in this graph |
|e_size|O(1) |Returns the number of edges in this graph |
|get_all_v|O(1) |return a dictionary of all the nodes in the Graph, each node is represented using a pair |
|all_in_edges_of_node|O(1) |return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight) |
|all_out_edges_of_node|O(k) |return a dictionary of all the nodes connected from node_id , each node is represented using a pair(other_node_id, weight) |
|get_mc|O(1) |Returns the current version of this graph,on every change in the graph state - the MC should be increased | 
|add_edge|O(1) |Adds an edge to the graph. |
|add_node|O(1) | Adds a node to the graph. |
|remove_node|O(n) |Removes a node from the graph. |
|remove_edge|O(1) |Removes an edge from the graph. |
# GraphAlgo:
In Graph algo we used two main algorithms- DFS and Dijkstra:\
# DFS
Depth-first search  (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the\ root node in the case of a graph) and explores as far as possible along each branch before backtracking.\
# Dijkstra:
An algorithm for finding the shortest paths between nodes in a graph 



