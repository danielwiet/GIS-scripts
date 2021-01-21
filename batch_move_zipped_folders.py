# import modules needed
import os
import glob

path = input("What is the path to the directory: ")

desktop = os.path.join(os.path.expanduser('~'), 'Desktop', 'zipped_shapefiles')
print(desktop)
# os.mkdir(desktop)

for folders in os.listdir(path):
	# ignore hidden files
	if not folders.startswith('.'):
		# change into subdirectory
		os.chdir(path + "/" + folders)

        # stores current directory pathname
		retval = os.getcwd()
		# print(retval)

		zipped_shapefile_folders = glob.glob(retval + "/zipped*")
		# print(zipped_shapefile_folders)
		
		# following code keeps throwing [Errno 66] Directory not empty
		# for folder in zipped_shapefile_folders:
		# 	os.replace(folder, desktop)