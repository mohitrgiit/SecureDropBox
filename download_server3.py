#!/usr/bin/python

# coding: utf-8
# Check if Magic folder exists - if not create
#  Check bucket exists - if not create
#  If bucket exists - sync
#      Monitor folder
#      If moved in - upload   --- moved in for update also -- if key exists exception - update instead of 
#      If moved out - delete 
#  Sync script - check number of objects in bucket - if files more/less download/delete extra/missing file
#              -check file size - if different download file

import os
import sys
import boto
import appindicator
import pynotify
import gtk
#---------------------------------------------------------
'''
import boto
from boto.s3.connection import S3Connection
conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')
rs = conn.get_all_buckets()
for b in rs:
    print b.name
    
mybucket = conn.get_bucket('juibhagat')
rs = mybucket.list()
'''
# --------------------------------------------------------
'''
rs = ["/home/bhanu/MagicBox/file1","/home/bhanu/MagicBox/file2","/home/bhanu/MagicBox/file3"]
fo = open("./foo.txt", "wb")
for key in rs:
    for root,dirs,files in os.walk("/home/bhanu/MagicBox", topdown = True):
       for name in files:
          if key == os.path.join(root,name):
              fo.write(key)
              fo.write("\t")
              fo.write("Already there")
          else :
              fo.write(key)
              fo.write("\t")
              fo.write("Not in local folder....syncing...")
              fo.write("\n")

import boto
# Connect
from boto.s3.connection import S3Connection
conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')
'''



def main():
	import sys
	import os
	import boto
	import appindicator
	import pynotify
	import gtk
	sel_file = sys.argv[1]

	#Connect to your account
	from boto.s3.connection import S3Connection
	conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')

	#initialize sets to hold keys and files in local folder
	from sets import Set
	set_keys = Set([])
	set_files = Set([])



	all_filenames = list()
	selected_files = list()

	# Get keys in bucket
	mybucket = conn.get_bucket('itcs6320bucket2')
	rs = mybucket.list()

	i = 0
	for key in rs:
    		all_filenames.insert(i+1,key.name)

	for p in all_filenames:
  		print p	
	#Which files to download?
	j = 0
	for files in all_filenames: 
	
        	 if (files.startswith(sel_file) and files.endswith("R3")):
        	               selected_files.insert(j+1,files)
                   
        	 elif (files.startswith(sel_file) and files.endswith("R45")):
        	               selected_files.insert(j+1,files)
                       
        	 elif (files.startswith(sel_file) and files.endswith("R26")):
		 	      selected_files.insert(j+1,files)
                       

	print "List from selected files"
	for p in selected_files:
  		print p

	fo = open("./foo.txt", "wb")

	# Make a key object to use for download
	from boto.s3.key import Key
	k = Key(mybucket)

	#download these files ---> in s3 but not in local folder

	for item in selected_files:
  		if not (item.startswith(".") or item.endswith("~")):
     			k.key = item
     			k.get_contents_to_filename(os.path.join(os.path.abspath("./MagicBox"),item)) 
     			fo.write("downloaded file")
     			if not pynotify.init ("summary-only"):
       				sys.exit (1)
     			n = pynotify.Notification ("Downloaded " + item,"")
     			n.show()

	fo.close()



if __name__=="__main__":
    main()
