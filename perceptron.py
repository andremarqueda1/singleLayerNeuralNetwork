# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:06:30 2020

Python 3.x required.

Simple Perceptron (Single layer Neural Network)
"""


import csv 

"""Lectura de SandwichAnts CSV.
Para su posterior procesamiento"""
print ("****READING INPUT VALUES*****")
weight,trial,bread,filling,butter,ants=[],[],[],[],[],[]#Declaring the variables that will host each column value
columnNumber=0 #Defining the column number (Number of trials+the header)
with open('SandwichAnts.csv',newline='\n') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        if (columnNumber==0):
            columnNumber+=1
            header=row[:]
        else:
            trial.append(int (row[0]))#Casting as integer
            bread.append(row[1])
            filling.append(row[2])
            if (row[3]=="yes"):
                butter.append(True)
            else:
                butter.append(False)
            ants.append(row[4])
            
            columnNumber+=1
            
print("Randomizing weights")

print(header)
for i in range (columnNumber-1):
    print(trial[i],bread[i],filling[i],butter[i],ants[i],sep="\t")
    


