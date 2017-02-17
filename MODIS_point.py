#!/usr/bin/env python
"""MODIS_point.py - Extracts MODIS information for a single point from CSVs"""

import sys
from os import listdir
from os.path import isfile, join
import csv

#user options begin =================================
file_dir = "/group_workspaces/cems2/nceo_generic/nceo_ed/NDVI/" #directory with all the data

#time span
first_year=2006
first_month=1
last_year=2006
last_month=12

#field of interest
field = "NDVI"

#file resolution in degrees
resolution = 0.1

#location
lat = 13.09 #north is postive
lon = 2.11  #east is positive

#user options ends ====================================

print "Looking in %s" %file_dir
print "For %s files" %field
print "From %i-%s to %i-%s" %(first_year,str(first_month).zfill(2),last_year,str(last_month).zfill(2))

files_in_dir = [f for f in listdir(file_dir) if isfile(join(file_dir, f))] #all files in folder 
if files_in_dir == []:
    print "No files at all found in %s" %file_dir
    sys.exit()
    
    
field_files = [f for f in files_in_dir if field in f]
if field_files == []:
    print "No files found that contain %s in their file name" %field
    sys.exit()

    
for year in range(first_year,last_year+1): #loop years
    #figure out month range
    if year < last_year:
        this_last_month = 12
    else:
        this_last_month = last_month
    if year > first_year:
        this_first_month = 1
    else:
        this_first_month = first_month
    for month in range(this_first_month,this_last_month+1): #loop months
        this_file_l = [f for f in field_files if "%i-%s" %(year,str(month).zfill(2)) in f]
        if len(this_file_l) < 1:
            print "No file found for %i-%s" %(year,str(month).zfill(2))
            sys.exit()
        elif len(this_file_l) > 1:
            print "More than one file found for %i-%s (this is a problem)" %(year,str(month).zfill(2))
            print this_file_l
            sys.exit()
        else:
            this_file = this_file_l[0]
        
        file_object = open(join(file_dir,this_file),"rb")
        data = list(csv.reader(file_object, delimiter=','))
        file_object.close()
        
        i =int((lon+180)/resolution)
        j =int((90-lat)/resolution)
        
        if float(data[j][i]) == 99999.:
            print "%i-%s : %s=%s" %(year,str(month).zfill(2),field,"OCEAN, ICE, OR NO DATA")
        else:
            print "%i-%s : %s=%s" %(year,str(month).zfill(2),field,data[j][i])
        del data
        
