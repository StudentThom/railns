'''
Created on Oct 31, 2017

@author: thom

retrieved from http://www.bogotobogo.com/python/python_graph_data_structures.php
'''

"""
Vertex class.

Initializes a vertex class.
"""
# For Dijkstra
import sys

class Vertex:

    # initialise variables
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        # For Dijkstra:

        # to keep track of total cost from start node to destination,
        # the distance (instance) variable is used
        # contains current total weight of smallest weight path from start to dest
        # the value distance determines the order of objects in the
        # priority queue/heapq (see dijkstra.py)
        # Set distance to infinity (= very large number) for all nodes
        self.distance = sys.maxint

        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    # print initializer, pretty print statement (try printing a vertex!)
    # printing a Vertex('node') "prints node adjacent: []"
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    # adds neighbour to the neighbour list
    # adds them as an integer weight!
    # add new neighbour with its weight
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    # returns list of pointers to neighbouring vertex class objects
    def get_connections(self):
        return self.adjacent.keys()

    # returns the name of the node nodename.get_id()
    def get_id(self):
        return self.id

    # retrieves the weight of a vertex
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def get_critical(self, neighbor_critical):
        return self.adjacent[neighbor_critical]

    # All def below in class Vertex for Dijkstra:

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True


"""
Graph class.

Initializes a graph class.
Stores all vertex names, and the number of verteces.
"""
class Graph:
    # initialise graph variables
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    # ???
    def __iter__(self):
        return iter(self.vert_dict.values())

    # adds vertexes
    def add_vertex(self, node):
        self.num_vertices += 1

        # make new vertex
        # Vertex(node) initialises new vertex
        new_vertex = Vertex(node)

        # add new vertex to dict
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None


    # add edge
    def add_edge(self, frm, to, cost = 0):

        # if from is new vertex, add to dict
        if frm not in self.vert_dict:
            self.add_vertex(frm)

        # if to is new vertex, add to dict
        if to not in self.vert_dict:
            self.add_vertex(to)

        # in Vertex class frm, add neighbour Vertex class to, with weight cost
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

        # in Vertex class to, add neighbour Vertex class frm, with weight cost
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
        

    # returns a list of all vertices
    def get_vertices(self):
        return self.vert_dict.keys()