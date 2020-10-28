class Vertex:
    def __init__(self, vertexName):
        self.name = vertexName                      # vertex's name
        self.neighbor = {}                          # vertex's neighbor

    def __str__(self):
        return str(self.name) + ' neighbor: ' + str([x.name for x in self.neighbor])

    def add_neighbor(self, neighbor, weight=0):
        self.neighbor[neighbor] = weight

    def get_connections(self):
        return self.neighbor.keys()

    def get_name(self):
        return self.name

    def get_weight(self, neighbor):
        return self.neighbor[neighbor]

class Graph:
    def __init__(self):
        self.vertexs_dict = {}                      # vertexs
        self.num_vertexs = 0                        # Number vertexs
        self.directed = False                       # direction

    def __iter__(self):
        return iter(self.vertexs_dict.values())

    def get_vertexs(self):
        return self.vertexs_dict.keys()

    #   Return the number, n, of vertices in G.
    def get_vertexsCnt(self):
        return self.num_vertexs

    #   Return the number, m, of edges in G.
    def get_allEdges(self):
        edges = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (self.directed == True):
                    edges[frm + to] = weight
                else:
                    if not (frm + to in edges.keys() or to + frm in edges.keys()):
                        edges[frm + to] = weight
        return len(edges.keys())

    #   Return a set or list containing all n vertices in G.
    def get_listVertex(self):
        listvertex = list(self.vertexs_dict.keys())
        return listvertex

    #   Return a set or list containing all m edges in G.\
    def get_listEdge(self):
        edges = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (self.directed == True):
                    edges[frm + to] = weight
                else:
                    if not (frm + to in edges.keys() or to + frm in edges.keys()):
                        edges[frm + to] = weight
        return edges.keys()

    #   Return some vertex, v, in G.
    def get_vertexData(self, vertexName):
        if vertexName in self.vertexs_dict:
            return self.vertexs_dict[vertexName]
        else:
            return None

    #   Return the degree, deg(v), of a given vertex, v, in G.
    def get_vertexNeighborCnt(self):
        degree_of_vertices = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            degree_of_vertices[source] = len(self.vertexs_dict[frm].get_connections())
        return degree_of_vertices

    #   Return a set or list containing all the edges incident upon a give in G.
    def get_incidentEdges(self, vertex):
        incident_edges = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].get_connections():
                to = destination.name
                if (vertex == to):
                    incident_edges[source] = to
        return incident_edges

    #   Return a set or list containing all the vertices adjacent to a give in G.
    def get_adjacentVertices(self, vertex):
        return self.get_vertexData(vertex)

    #   Return the two end vertices of an edge, e, in G; if e is directed, indicate vertex is the origin of e and which is the destination of e.
    def get_V2WithEdge(self, given_edge):
        edge_verices = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (given_edge == weight):
                    if (self.directed == True):
                        edge_verices[frm + "->" + to] = weight
                    else:
                        edge_verices[frm + to] = weight
        return edge_verices

    #   Return whether two given vertices, v and w, are adjacent in G.
    def get_edgeWithV2(self, v, w):
        edges = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                edges[frm + to] = weight
        return (v + w in edges.keys() or w + v in edges.keys())

    #   Indicate whether a given edge, e, is directed in G.
    def get_directionEdge(self, given_edge):
        does_edge_exist = False
        if (self.directed == True):
            for source in self.vertexs_dict:
                frm = self.vertexs_dict[source].name
                for destination in self.vertexs_dict[frm].neighbor:
                    to = destination.name
                    frmV = self.get_vertexData(frm)
                    weight = frmV.get_weight(destination)
                    if (given_edge == weight):
                        return ("Directed edge")
        return ("No directed edge")

    #   Return the in –degree of v, inDegree(v).
    def inDegree(self, v):
        in_degree = 0
        if (self.directed == True):
            for source in self.vertexs_dict:
                frm = self.vertexs_dict[source].name
                for destination in self.vertexs_dict[frm].neighbor:
                    to = destination.name
                    if (v == to):
                        in_degree += 1
            return in_degree
        else:
            return ("No in-degree for undirected graph")

    #   Return a set or list containing all the incoming (or outgoing) … upon a given vertex, v, in G.
    def get_VInOut(self, v):
        incoming_edges_for_v = []
        outgoing_edges_for_v = self.vertexs_dict[v].neighbor.values()
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (v == to):
                    incoming_edges_for_v.append(weight)
        return (incoming_edges_for_v + list(outgoing_edges_for_v))

    #   Return a set or list containing all the vertices adjacent to a give along incoming (or outgoing) edges in G.
    def get_EInOut(self, v):
        in_degree = 0
        adgecent_vertices_of_v = []
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (v == to):
                    adgecent_vertices_of_v.append(frm)
        adgecent_vertices_of_v = adgecent_vertices_of_v + list(self.vertexs_dict[v].neighbor.keys())
        return set(adgecent_vertices_of_v)

    #   Insert a new directed (or undirected) edge, e, between two given,… and w, in G.
    def add_vertex_edge(self, frm, to, cost=0):
        if frm not in self.vertexs_dict:
            self.add_vertex(frm)
        if to not in self.vertexs_dict:
            self.add_vertex(to)
        self.vertexs_dict[frm].add_neighbor(self.vertexs_dict[to], cost)
        if self.directed == False:
            self.vertexs_dict[to].add_neighbor(self.vertexs_dict[frm], cost)


    #   Insert a new (isolated) vertex, v, in G.
    def add_vertex(self, vertexName):
        self.num_vertexs = self.num_vertexs + 1
        new_vertex = Vertex(vertexName)
        self.vertexs_dict[vertexName] = new_vertex
        return new_vertex

    #   Remove a given edge, e, from G.
    def remove_edge(self, remove_edge):
        edges_present = {}
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                frmV = self.get_vertexData(frm)
                weight = frmV.get_weight(destination)
                if (remove_edge == weight):
                    edges_present[source] = destination
        for source, destination in edges_present.items():
            print(self.vertexs_dict[source].neighbor[destination])
            self.vertexs_dict[source].neighbor.pop(destination)

    #   Remove a give vertex, v, and all its incident edges from G.
    def remove_vertex(self, v):
        # del G[v]
        self.vertexs_dict.pop(v);
        print(self.vertexs_dict.keys())
        for source in self.vertexs_dict:
            frm = self.vertexs_dict[source].name
            for destination in self.vertexs_dict[frm].neighbor:
                to = destination.name
                if (frm == to):
                    self.vertexs_dict[source].neighbor.pop(destination)
        return self.vertexs_dict


