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
        
# put critical stations into one array
with open('StationsHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    kritieke_stations = []
    
    for row in stations:
        #print(', '.join(row))
        if row[3] == "Kritiek":
            print(row[0])
            kritieke_stations.append(row[0])
        
# add connections between nodes (=stations) into graph
with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stations:
        # check whether connection is critical
        if row[0] in kritieke_stations or row[1] in kritieke_stations:
            g.add_edge(row[0],row[1],int(row[2]),1)
        else:
            g.add_edge(row[0],row[1],int(row[2]),0)
        
        
# print graph
for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d, %d)'  % ( vid, wid, v.get_weight(w), v.get_critical(w)))

for v in g:
    print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
        
print(g)

