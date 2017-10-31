'''

import csv
RainNL, Heuristieken, oktober-november-december 2017

'''

import csv

class station:
    def __init__(self, name, connected_stations, travel_times):
        self.name = name
        self.connected_stations = connected_stations
        self.travel_times = travel_times
            
    def travel_time(self, station1, station2):
        print('hoi')
        
        
amsterdam = station("amsterdam", "haarlem", 1)


            
    

with open('ConnectiesHolland.csv', newline='') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stations:
        print(', '.join(row))
        
        