'''
Created on Oct 31, 2017

@author: thom
'''
import make_graph
import csv

g = make_graph.Graph()


# read in stations from csv and put each station as node in graph
with open('StationsHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stations:
        g.add_vertex(row[0])
        
# add connections between nodes (=stations) into graph
with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stations:
        g.add_edge(row[0],row[1],int(row[2]))
        
        
# print graph
for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

for v in g:
    print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
        
print(g)
