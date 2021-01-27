#!/usr/bin/python

import os
import shutil

path = input("What is the path to the directory you want to delete from?: ")

for folders in os.listdir(path):
	# ignore hidden files
	if not folders.startswith('.'):

		# change the current directory
		os.chdir(path + "/" + folders)

		# stores current directory pathname
		parent_folder = os.getcwd()
		# print(parent_folder)

		# deletes the zipped folder
		if os.path.exists(parent_folder + '/zipped_' + folders + '_shapefiles'):
			shutil.rmtree(parent_folder + '/zipped_' + folders + '_shapefiles')
