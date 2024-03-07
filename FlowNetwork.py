# A template for Ford Fulkerson algorithm and min cut

from graph import Graph
from copy import deepcopy as copy
import sys
from collections import deque
#from icecream import ic


## This code assumes flow is dictionary with keys (u,v) and values flow(u,v)
## Define the sum of two flows
def SumFlow(f1,f2):
  f = {}
  for (u,v) in set(f1.keys()) | set(f2.keys()):
    if not (u,v) in f1:
      f[(u,v)] = f2[(u,v)]
    elif not (u,v) in f2:
      f[(u,v)] = f1[(u,v)]
    else:
      f[(u,v)] = f1[(u,v)] + f2[(u,v)]
  return f



## This is an EXAMPLE of how the flow network class can be implemented, some implementation is missing
class FlowNetwork:
  def __init__(self,G) -> None:
    self.G = G
    self.FindSource()
    self.FindSink()
    
  ## Find the source, it is the first vertex with a non-empty adjacency list:
  def FindSource(self):
    for u in range(self.G.n):
      if len(self.G.adj[u]) > 0:
        self.s = u
        return    
  ## Find the sink. It is the last vertex.
  def FindSink(self):
    self.t = self.G.n-1

  # Define the value of a flow
  def FlowValue(self,f):
    return sum([f[(self.s,u)] for u in G.adj[self.s] if (self.s,u) in f])

  ## Create a residual graph
  def MakeResidual(self, f):
    ## Copy the graph:
    G = copy(self.G)
    for (u,v) in f:
      c = 0
      ## Copy the weight
      if (u,v) in G.w:
        c = G.w[(u,v)]
      #calculate residual capasity
      cf = c - f[(u,v)]
      ## It is an error if the residual capacity is negative
      if cf < 0:
        raise Exception("capacity violation in f")
      ## Add the edge if the residual capacity is positive
      if not v in G.adj[u]:
        G.addEdge(u,v)
      G.w[(u,v)] = cf
    return G

  ## Finding the augmenting path using BFS algorithm
  def FindAugPath(self, Gr=None, s=None, t=None):
    if Gr is None:
        Gr = self.MakeResidual({})
    if s is None:
        s = self.s
    if t is None:
        t = self.t

    visited = set()
    queue = deque([(s, [s])])

    while queue:
        u, path = queue.popleft()
        if u == t:
            return path
        visited.add(u)
        for v in Gr.adj[u]:
            if v not in visited and Gr.w[(u, v)] > 0:
                queue.append((v, path + [v]))
                visited.add(v)
    return []


  ## Make an augmenting flow from a path
  def MakeAugFlow(self,path, Gr = None):
    if Gr is None:
      Gr = self.G
    f = {}
    for i in range(len(path)-1):
      u = path[i]
      v = path[i+1]
      if (u,v) not in Gr.w or Gr.w[(u,v)] == 0:
        raise Exception("Edge not in Gr or saturated")
      f[(u,v)] = 0
    cf = min([Gr.w[(u,v)] for (u,v) in f])
    for (u,v) in f:
      f[(u,v)] = cf
    return f

  # Ford fulkerson algorithm
  def FordFulkerson(self):
    f = {}
    G = self.G
    Gr = self.MakeResidual(f)
    ap = self.FindAugPath(G)
    while ap != []:
      fp = self.MakeAugFlow(ap,Gr)
      f = SumFlow(f,fp)
      Gr = self.MakeResidual(f)
      ap = self.FindAugPath(Gr)
    return f

  def MinCutEdges(self):
    # Get the maximum flow using Ford Fulkerson
    max_flow = self.FordFulkerson()
    # Make the residual graph
    residual = self.MakeResidual(max_flow)
    S = set([])

    # Add source to the set S
    S.add(self.s)

     # Find the set of reachable vertices from the source in the residual graph
    visited = set()
    queue = deque([self.s])

    while queue:
        u = queue.popleft()
        visited.add(u)
        for v in self.G.adj[u]:
            # Check if the edge has residual capacity in the residual graph
            if (u, v) in residual.w and residual.w[(u, v)] > 0 and v not in visited:
                queue.append(v)
                # Add the reachable vertices to the set S
                S.add(v)

    # Test print: print("Reachable vertices:", S)

    # Get the edges that cross the cut:
    Edges = [(u, v) for u in S for v in self.G.adj[u] if v not in S]

    # Return these edges
    return Edges
            
if __name__ == "__main__":
    G = Graph()
    inputgraph = sys.argv[1]
    G.readgraph(inputgraph)
    F = FlowNetwork(G)
    edges = F.MinCutEdges()
    print("Edges that cross the minimum cut:", edges)
  

 