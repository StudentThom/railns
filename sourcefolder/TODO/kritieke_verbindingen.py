'''
Created on Oct 31, 2017

@author: thom
'''

import csv


with open('StationsHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    kritieke_stations = []
    
    for row in stations:
        #print(', '.join(row))
        if row[3] == "Kritiek":
            print(row[0])
            kritieke_stations.append(row[0])
     
        
print(kritieke_stations)
        

with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    kritieke_verbindingen = []
    for row in stations:
        #print(', '.join(row))
        if (row[0] in kritieke_stations) or (row[1] in kritieke_stations):
            kritieke_verbindingen.append({"station1": row[0], "station2": row[1], "reistijd": int(row[2])})
            

print(kritieke_verbindingen)


