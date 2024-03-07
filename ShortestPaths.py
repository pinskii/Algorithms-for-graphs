import graph
import sys
from collections import deque

def max_vertices_on_shortest_path(g, s, t, B):
    # BFS algorithm modified to save the shortest paths
    n = g.n
    dist = [float('inf')] * n
    dist[s] = 0
    paths = [[] for _ in range(n)]
    paths[s] = [[s]]
    q = deque([s])

    while q:
        u = q.popleft()
        for v in g.adj[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                new_paths = [path + [v] for path in paths[u]]
                paths[v].extend(new_paths)
                q.append(v)

            elif dist[v] == dist[u] + 1:
            # If there are multiple shortest paths to v, append the new paths
                new_paths = [path + [v] for path in paths[u]]
                paths[v].extend(new_paths)

            
# Counting the vertices in set B encountered in the paths
    max_vertices = 0
    for path in paths[t]:
        vertices_count = sum(1 for vertex in B if vertex in path)
        max_vertices = max(max_vertices, vertices_count)

    return max_vertices

# Read in a set of vertices from a file.
# These are just numbers separated by whitespace.
def readset(filename):
  f = open(filename, 'r')
  s = set()
  for line in f:
    for v in line.split():
      s.add(int(v))
  return s

# Read the pair, again, just two integers separated by whitespace.
def readpair(filename):
  f = open(filename, 'r')
  for line in f:
    (v,w) = line.split()
    return (int(v), int(w))

# If ran from the command line:
if __name__ == "__main__":
    # Graph is the first command line argument:
    g = graph.Graph()
    g.readgraph(sys.argv[1])
    
    # Vertices are the second command line argument:
    B = readset(sys.argv[2])
    
    # Pair is the third command line argument:
    (v, w) = readpair(sys.argv[3])

    # Call your algorithm:
    result = max_vertices_on_shortest_path(g, v, w, B)

    # Print the result:
    print(result)
