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
    critical_stations = []

    for row in stations:
        g.add_vertex(row[0])

        #print(', '.join(row))
        if row[3] == "Kritiek":
            print(row[0])
            critical_stations.append(row[0])

# add connections between nodes (=stations) into graph
with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stations:
        g.add_edge(row[0],row[1],int(row[2]))

critical_lines = 0

# print graph
# w, v are entire vertex object
# wid, vid are the names of the vertices
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print(w)
        print(wid)

        # check wether station name is critical
        if vid in critical_stations:

            # for every neighbour, add 1 critical line
            for n in g.get_vertex(vid).get_connections():
                critical_lines += 1
            print('( %s , %s, %3d), CRITICAL'  % ( vid, wid, v.get_weight(w)))

        # check wether station name is critical
        elif wid in critical_stations:
            # for every neighbour, add 1 critical line
            for n in g.get_vertex(wid).get_connections():
                critical_lines += 1
            print('( %s , %s, %3d), CRITICAL'  % ( vid, wid, v.get_weight(w)))

        else:
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

# print connections
for v in g:
    print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

# count unique critical lines, later placed in make_graph.py as its own function
count = 0
critical_lines = []

# loop through vertices
for v in g:
    # get name element
    from_id = v.get_id()

    # check if name is in critical_stations
    if from_id in critical_stations:

        # get name element of all connections
        for w in v.get_connections():
            to_id = w.get_id()

            # check if name is in critical_stations
            if to_id in critical_stations:
                l = [to_id, from_id]

                # for every unique critical line
                # double check on self made graph, the only double critical line found was:
                # (Den Haag Centraal, Gouda), (Gouda, Den Haag Centraal)
                if not l in critical_lines or not l[::-1]:
                    critical_lines.append([from_id, to_id])
                    count += 1

            else:
                # to station is not critical station, but from station is critical
                count += 1

print(critical_lines)
print(count)
