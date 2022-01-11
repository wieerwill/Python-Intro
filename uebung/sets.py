# Öffne die ../data/names.csv - Datei als .csv-Datei und berechne die Anzahl der verschiedenen Vornamen, die in dieser Datei aufgelistet sind

import csv

names = set()

with open('../data/names.csv', newline='') as csvfile:
    namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in namereader:
        if counter != 0:
            names.add(row[1])
        counter = counter + 1
print(len(names))