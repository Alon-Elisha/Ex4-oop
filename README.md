# Ex4-oop

Readme – pokemon game on a weighted directed graph

The game:
The game is very simple. on a weighted graph there are agents and pokemon, the aim of the game is to earn as many points as possible by catching pokemon using
the agents. at the start of the game, each agent/s is on a node on the graph and is able to travel from node to node if the nodes are connected by an edge
which is in the right direction. the pokemon are on edges. To catch a pokemon an agent needs to pass the edge the pokemon is on in the right direction. the more 
pokemon an agent catches the faster he gets. the game has a timer and when the timer hit zero the game is over and your grade is the amount of points you earned
by catching pokemon.

## Classes

#### EdgeData:
A class that represents a singular edge between 2 nodes.
As an object that represents an edge, it will need to have attributes that represent an edge in a graph.
An edge has a direction, and it comes out of a node, and goes into a node. In addition an edge has length/weight.
EdgeDataClass object will have the attributes of: src – the source of the edge,
dest – the destination of the edge, and w – the weight/length of the edge.

#### NodeData:
A class that represents a singular node in the graph.
As an object that represents a node, it will need to have an attribute to identify the specific node, 
an attribute/s of it’s location.
NodeData object will have the attributes of: id – the id of the node(number),
pos – a tuple of its x and y coordinates.

### DiGraph:
A class that represents a graph. the graph has a dictionary of nodes, using the nodes' ids as keys to the NodeData objects. a list of all edges in the graph and two dictionaries,
one dictionary holds for each node all the edges that go from it to other nodes. the other does the opposite, holds all the edges that go into the node from other nodes.
the important functions in the class are the add\remove node\edge functions.

## GraphAlgo:
A class that lets us run algorithms on a graph.

#### shortest path:
recieves wto id numbers of two nodes and returns the shortest path between them and the total weight of the journey.
we used Dijkstra's Algorithm to write this function. we start with the source node and visit all its neighbours and 
caculate weight of the path, we keep doing that for every unvisited node until we visit all nodes on the graph. Dijkstra's
algorithm gives all shortest paths from the source node to each other node, so we take the one ending at our destination node.
