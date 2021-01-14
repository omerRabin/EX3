# Hello to our directed weighted graph Project in Python
![graph](https://user-images.githubusercontent.com/61798552/104636667-61cb2900-56ac-11eb-8800-cb578bb578c9.png)
Hello, you have arrived at Eldad and Omar's project on the subject of weighted directed graphs written in Python.\
In our project we built software that produces deliberate weighted graphs and allows you to make changes to them and even various algorithms.\
In addition during the project we made comparisons between the runtimes of the functions in our algorithm class to the algorithm Class of the network-X to\
the algorithm class of our preivious Project in Java. \
The main algorithm we used in this project is DFS. we used Dijkstra to find the shortest path from two nodes in the graph.\
In addition, we used DFS to find a SCC of node and all the SCC's in the graph. SCC is the strongest connected component. \
Our project consists of several classes that create the graphic system:\
The main classes is: DiGraph, GraphAlgo.
# DiGraph:
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
In Graph algo we used two main algorithms- DFS and Dijkstra:
# DFS
![](DFSgif.gif)

Depth-first search  (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the\ root node in the case of a graph) and explores as far as possible along each branch before backtracking.
# Dijkstra:
An algorithm for finding the shortest paths between nodes in a graph\
# The Algorithm:
Let the node at which we are starting be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will assign some\ initial distance values and will try to improve them step by step.\
Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.\
Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance\ to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has\ length 2, then the distance to B through A will be 6 + 2 = 8.\
If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.\
When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set.\
A visited node will never be checked again.\
If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
When planning a route, it is actually not necessary to wait until the destination node is "visited" as above: the algorithm can stop once the destination node has the smallest tentative distance among all "unvisited" nodes (and thus could be selected as the next "current").

|Method|Complexity|Description|
|----|------|---------|
|get_graph|O(1) | return: the directed graph on which the algorithm works on. |
|load_from_json|O(1) |Loads a graph from a json file. |
|save_to_json|O(1) | Saves the graph in JSON format to a file |
|shortest_path|O(1) |Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm |
|connected_component|O(k) |Finds the Strongly Connected Component(SCC) that node id1 is a part of. |
|connected_components|O(1) |Finds all the Strongly Connected Component(SCC) in the graph. | 
|plot_graph|O(n^2) |Plots the graph. |

