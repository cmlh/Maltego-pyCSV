#!/usr/bin/python 
import sys
import csv
import os,sys,time,random
from MaltegoTransform import *

me = MaltegoTransform();
me.parseArguments(sys.argv);
csv_file = me.getValue();

csv_reader = csv.reader(open(csv_file), delimiter = ',');
sourceClients = []
for row in csv_reader:
	sourceClients.append(row[0]);

sourceClientsUnique = dict(map(lambda i: (i,1),sourceClients)).keys()
for s in sourceClientsUnique:

	myentity = me.addEntity("IPAddress",s);
	myentity.addAdditionalFields("file","CSV File",None,csv_file);
	
me.returnOutput();