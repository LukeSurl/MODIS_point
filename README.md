# MODIS_point

A simple Python acitivity that reads monthy gridded MODIS .csv files and writes to screen the value of the field at a specifed lat/lon point

Compatible MODIS files are the monthyl CSV (not CSV for excel) downloaded from: https://neo.sci.gsfc.nasa.gov/ . Despite this repostiory's name it should work for gridded data that is not associated with MODIS.

User options are specified by the top section of the Python script. "field" must be a string in the filename that distingishes the files for this field from others. For example, the TERRA/MODIS active fires product has filenames of the form MOD14A1_M_FIRE_YYYY-MM-DD_rgb_3600x1800.CSV, and could be specified by either "FIRE" or "MOD14A1".

To excute, make the python script executable 
chmod +x MODIS_point.py 
then execute without arguments
./MODIS_point.py

==Contact==
Written by Luke Surl L.Surl@ed.ac.uk

==Example input and output==
12 files, of name MOD13A2_M_NDVI_2006-MM-01_rgb_3600x1800.CSV are in /group_workspaces/cems2/nceo_generic/nceo_ed/NDVI

file_dir = "/group_workspaces/cems2/nceo_generic/nceo_ed/NDVI/" #directory with all the data
===Options===
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

===Output===

Looking in /group_workspaces/cems2/nceo_generic/nceo_ed/NDVI/
For NDVI files
From 2006-01 to 2006-12
2006-01 : NDVI=0.20708661
2006-02 : NDVI=0.18740158
2006-03 : NDVI=0.16771653
2006-04 : NDVI=0.16771653
2006-05 : NDVI=0.16771653
2006-06 : NDVI=0.2031496
2006-07 : NDVI=0.2464567
2006-08 : NDVI=0.37637794
2006-09 : NDVI=0.3527559
2006-10 : NDVI=0.29370078
2006-11 : NDVI=0.25826773
2006-12 : NDVI=0.22283465



