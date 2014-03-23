#!/usr/bin/python 
import sys
import csv
import os,sys,time,random
from MaltegoTransform import *
import EasyDialogs

me = MaltegoTransform();
me.parseArguments(sys.argv);
csv_file = me.getVar("file");
if (csv_file is None):
	defaultFile = "c:\stafflist.csv"
	csv_file = EasyDialogs.AskString("Which file do you want to use?",defaultFile);

if (csv_file is None):
	me.returnOutput();
	exit();
	


csv_reader = csv.reader(open(csv_file), delimiter = ',');
Emails = []
for row in csv_reader:
	Emails.append(row[0]);

EmailsUnique = dict(map(lambda i: (i,1),Emails)).keys()
for s in Emails:
	myentity = me.addEntity("EmailAddress",s);
	myentity.addAdditionalFields("file","CSV File",None,csv_file);
	

me.returnOutput();