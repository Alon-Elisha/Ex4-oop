# Ex4-oop

Readme – pokemon game on a weighted directed graph

The game:
The game is very simple. on a weighted graph there are agents and pokemon, the aim of the game is to earn as many points as possible by catching pokemon using
the agents. at the start of the game, each agent/s is on a node on the graph and is able to travel from node to node if the nodes are connected by an edge
which is in the right direction. the pokemon are on edges. To catch a pokemon an agent needs to pass the edge the pokemon is on in the right direction. Each time a 
pokemon is captured another on pops up in a random edge on the graph. the more pokemon an agent catches the faster he gets. the game has a timer and when
the timer hit zero the game is over and your grade is the amount of points you earned by catching pokemon.

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


### Game strategy
Our algorithm is very simple yet very effetive and gets great results. First of all, we use all the classes we listed above to convert the graph details
given to us from json to different objects so we are able to use the shortest path algorithm easily. For each agent who is currently on a node(dest = -1),
we use the shortest path algorithm to check which pokemon currently on the graph is closest to him and return the path. we also keep track of which pokemon
have a trainer on the way to them and which are not to avoid a situation where multiple trainers go to capture the same pokemon. We also dont consider a pokemon captured
when a trainer is assigned to get him but only when it is actually captured. This sounds obvious but it allows us to be able to reroute trainers when a new pokemon pops 
up and could be really close to a trainer who is currently going for a capture a long distance from his position.

## GUI
The Gui of the graph was given to us but we did add stuff to it. each trainer and pokemon is represented by a circle, for the agents, inside the circle there is a number
which is their id which means you can keep track of each agent. For the pokemon, the number inside the circle represents the amount of points the capture of this pokemon
is worth. We also added a point and amount of moves trackers and a timer that shows how much time is left in the game. The last thing we added is a stop button which
stops the game and shows you the points and moves tou made in the terminal like it would at the end of the game.


#### How to run
when downloading the files one of the files is the jar file which is the server of the game. to run the game rou need to run this jar file using the command:
<java -jar Ex4_Server_v0.0.jar x> with x being the game level you want to run(0-15). after that all you need to do is run the student_code file and the
game will start in your screen.
