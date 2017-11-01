'''
Created on Nov 1, 2017

@author: dimitri
source:http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
'''

# moet deze in dit file, of in make_graph?
# constructs the shortest path starting from the target ('e') using predecessors
def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

# the algorithm iterates over every vertex in graph
# iteration order is controlled by priority queue, but
# actually in this version heapq is used
import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    # (all other nodes are still set to infinity (see make_graph.py))
    start.set_distance(0)

    # Set initial node as current
    # Create list of unvisited nodes called unvisited list (unvisited_queue)
    # consisting of all the nodes
    # Put tuple pair (distance, v) into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    # turn unvisited_queue into heap (=  binary trees for which every parent node has a value less than or equal to any of its children)
    heapq.heapify(unvisited_queue)


    while len(unvisited_queue):
        # Pops and returns a vertex with the smallest distance
        # start node is 0, others are infinity, so start node is popped and returned
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        # visited is now True not False
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            # if not visited
            # calculate tentative disance of current and unvisited neighbor
            # example: current is distance 6, and edge connecting it with neighbor
            # is 2, than distance is 6+2=8.
            new_dist = current.get_distance() + current.get_weight(next)

            # if newly calculated distance smaller than current assigned value of neighbor
            if new_dist < next.get_distance():
                # set distance of neighbor to new distance
                next.set_distance(new_dist)
                # set previous of neighbor from None to current
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' %(path[::-1])