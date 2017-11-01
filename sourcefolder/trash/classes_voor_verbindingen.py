'''
Created on Oct 31, 2017

@author: thom
'''
import csv

class verbindingen:
    
    def __init__(self, station1, station2, travel_time):
        self.station1 = station1
        self.station2 = station2
        self.travel_time = travel_time
            
            
with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 1
    for row in stations:
        print(', '.join(row))
        print(row)
        #verbindingen.append({"station1": row[0], "station2": row[1], "reistijd": int(row[2])})
        temp = verbindingen(row[0],row[1],row[2])
        print(temp)
     #    exec("verbinding%d = %s" %(i, temp))

print(verbindingen)