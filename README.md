# Here are a few of algorithms I implemented with Python for a university course Algorithms for graphs. 

# Maximum number of vertices on a shortest path (ShortestPaths.py)

## Overview
This Python program calculates the maximum number of vertices from a given set B that can appear on a shortest path from a start vertex s to an end vertex t in a directed graph.

## Instructions

1. **Directed Graph Input:**
   - Make a text file representing the directed graph in the format specified by the `writegraph` method in the `Graph` class. Each line should contain a vertex `u`, followed by ":", and a list of vertices it leads to separated by whitespace.

2. **Set of Vertices Input:**
   - Make a text file containing the set of vertices `B`. Simply list the vertices separated by spaces.

3. **Start and End Vertex Input:**
   - Choose a pair of vertices for the start (`s`) and end (`t`) vertices. These should be valid vertices in the graph. Write the pair separated by whitespace.

4. **Run the Program:**
   - Make sure to have the graph.py file installed.
   - Open the right filepath in terminal or command prompt.
   - Run the script with the input files as command line arguments.
  
## Notes
There were some templates used in the program. Graph.py was given by the course teacher, as well as the template for the ShortestPaths file. I implemented the max_vertices_on_shortest_path function.


# Program to find the edges that cross the minimum cut (FlowNetwork.py)

## Overview
This Python program finds the edges in a flow network that cross the minimum cut. 

## Instructions

1. **Graph Input:**
   - Make a text file representing the directed graph in the format specified by the `writegraph` method in the `Graph` class. Each line should contain a vertex `u`, followed by ":", and a list of vertices `v` and capacities `w` it leads to separated by whitespace. 
   Example format: 
   u: (v, w) (v, w)

2. **Run the Program:**
   - Make sure to have the given graph.py file installed in the same folder.
   - Open the right filepath in terminal or command prompt.
   - Run the script with the input file as command line argument, for example:
   > python FlowNetwork.py <input file>

## Notes
There were some templates used in the program. Graph.py was given by the course teacher, as well as the template for the FlowNetwork file. I implemented the FindAugPath and MinCutEdges functions.
