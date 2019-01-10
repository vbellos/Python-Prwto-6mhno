#!/usr/bin/python
import os
fname = raw_input("Dwse full file path tou typou '/home/user/Documents/a.py': \n ")
f = open(fname,"r")
lines = f.readlines()
f.close()
f = open(fname,"w")
for line in lines:
  sxolio= "#" in line	
  if (sxolio == False):
    f.write(line)
   
f.close()    

