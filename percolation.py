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
