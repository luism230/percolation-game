class Vertex:
	# `index` is a unique integer identifier, `color` is an integer in [-1, 0, 1].
	# Silver vertices have color=0, and teal vertices have color=1.
	# Unmarked vertices have color=-1.
	def __init__(self, index, color=-1):
		self.index = index
		self.color = color

class Edge:
	# `a` and `b` are Vertex objects corresponding to the endpoints of this edge.
	def __init__(self, a, b):
		self.a = a
		self.b = b

class Graph:
	# `vertices` and `edges` are iterables of Vertex and Edge objects respectively
	# Internally, we store these as set()s on the graph class.
	def __init__(self, vertices, edges):
		self.V = set(vertices)
		self.E = set(edges)


#MY STUFF

class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def getAttachedEdges(graph, v):
        return [e for e in graph.E if (e.a == v or e.b == v)]

    def ChooseVertexToColor(graph, active_player):
        
        V = list(graph.V)
        greatest = random.choice([v for v in graph.V if v.color == -1])
        for i in V:
            if len(PercolationPlayer.getAttachedEdges(graph, i)) > len(PercolationPlayer.getAttachedEdges(graph, greatest)) and i.color == -1:
                greatest = i
        return greatest
            

    def ChooseVertexToRemove(graph, active_player):
        
        oppE = 0
        for i in [j for j in graph.V if j.color != active_player]:
            oppE += len(PercolationPlayer.getAttachedEdges(graph, i))


        for v in graph.V:
            edges = PercolationPlayer.getAttachedEdges(graph, v)
            if len(edges) == 1:
                if edges[0].a.color == active_player and edges[0].b.color != active_player:
                    return edges[0].a
                elif edges[0].b.color == active_player and edges[0].a.color != active_player:
                    return edges[0].b

        if oppE == 0:
            return random.choice([v for v in graph.V if v.color == active_player])

        greatest = random.choice([v for v in graph.V if v.color == active_player])
        for i in graph.V:
            if len(PercolationPlayer.getAttachedEdges(graph, i)) > len(PercolationPlayer.getAttachedEdges(graph,greatest)) and i.color == active_player:
                greatest = i
        return greatest


# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()
