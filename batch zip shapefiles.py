# updated by dan wiet on 01/19/2121
# brian greer
# 4/2015
# http: // www.bgcarto.com/zip-all-shapefiles-in-directory-individually/
 
#import modules needed
import os
import glob
from zipfile import *

# define location of shapefiles and destination of zipped shapefiles
# source = r"/Users/danwiet/Desktop/coding/esri/past 4 months/20201116_HC"
#source = (path + "/" folder)
# dest = r"/Users/danwiet/Desktop/coding/esri/past 4 months/20201116_HC/zip"

path = input("What is the path to the parent folder: ")
# /Users/danwiet/Desktop/coding/esri/past 4 months

for folders in os.listdir(path):
	if not folders.startswith('.'):
		# print(folders)

		#change the current directory
		os.chdir(path + "/" + folders)
		
		#test current directory
		retval = os.getcwd()
		print(retval)

		# create destination directory if it does not exist
		if not os.path.exists(retval + "/zip"):
			os.makedirs(retval + "/zip")

		# #list all files with extension .shp
		shps = glob.glob(retval + "/*.shp")
		# #print(shps)

		# # create empty list for zipfile names
		ziplist = []
		
		# #populate ziplist list of unique shapefile root names by finding all files with .shp extension and removing extension
		for name in shps:
		# 	#prints full path for each shapefile
		# 	#print(name)
		# 	#retrieves just the files name for each name in shps
			file = os.path.basename(name)
		# 	#removes .shp extension/Users/danwiet/Desktop/coding/esri/past 4 months 
			names = file[:-4]
		# 	#adds each shapefile name to ziplist list
			ziplist.append(names)
		
		# #prints ziplist to confirm shapefile root names have been added
		# #print(ziplist)

		# #creates zipefiles in dest folder with basenames
		for f in ziplist:
		# 	# prints each item in the ziplist
		#	# print(f)
		# 	#creates the name for each zipefile based on shapefile root names
			file_name = os.path.join(retval + "/zip", f+".zip")
		# 	#print to confirm
		# 	#print(file_name)

		# 	#created the zipfiles with names defined above
			zips = ZipFile(file_name, "w")
		# 	#print(zips)
		# 	#files lists all files with the current basename (f) from ziplist
			files = glob.glob(str(f)+".*")
		# 	# iterate through each basename and add all shapefile components to the zipefile
			for s in files:
				#print(s)
				zips.write(s)
			zips.close()
