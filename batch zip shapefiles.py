# brian greer 4/2015
# http: // www.bgcarto.com/zip-all-shapefiles-in-directory-individually/
# updated by dan wiet on 01/19/2021

#import modules needed
import os
import glob
from zipfile import ZipFile


path = input("What is the path to the parent folder: ")

for folders in os.listdir(path):
	# ignore hidden files
	if not folders.startswith('.'):

		# change the current directory
		os.chdir(path + "/" + folders)
		
		# stores current directory pathname
		retval = os.getcwd()

		# create destination directory if it does not exist
		if not os.path.exists(retval + "/zipped_" + folders + "_shapefiles"):
			os.makedirs(retval + "/zipped_" + folders + "_shapefiles")

		# list all files with extension .shp
		shps = glob.glob(retval + "/*.shp")

		# create empty list for zipfile names
		ziplist = []
		
		# populate ziplist list of unique shapefile root names by finding all files with .shp extension and removing extension
		for name in shps:
			# retrieves just the files name for each name in shps
			file = os.path.basename(name)
			# removes .shp extension/Users/danwiet/Desktop/coding/esri/past 4 months 
			names = file[:-4]
			# adds each shapefile name to ziplist list
			ziplist.append(names)

			# creates zipefiles in dest folder with basenames
		for f in ziplist:
			# creates the name for each zipefile based on shapefile root names
			file_name = os.path.join(retval + "/zipped_" + folders +
			                         "_shapefiles", f+".zip")

			# creates the zipfiles with names defined above
			zips = ZipFile(file_name, "w")
			# files lists all files with the current basename (f) from ziplist
			files = glob.glob(str(f)+".*")
			# iterate through each basename and add all shapefile components to the zipefile
			for s in files:
				zips.write(s)
			zips.close()
