#!/usr/bin/python 
import sys
import csv
import os,sys,time,random
from MaltegoTransform import *

me = MaltegoTransform();
me.parseArguments(sys.argv);
csv_file = me.getVar("file");
sourceClient = me.getValue();

csv_reader = csv.reader(open(csv_file), delimiter = ',');
destinationClients = []
for row in csv_reader:
	if (row[0] == sourceClient):
		destinationClients.append(row[1] + ":" + row[2]);

destinationClientsUnique = dict(map(lambda i: (i,1),destinationClients)).keys()
for s in destinationClientsUnique:
	myentity = me.addEntity("IPAddress",s);
	myentity.addAdditionalFields("file","CSV File",None,csv_file);
	
me.returnOutput();