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
rs = ["/home/bhanu/cloud_/file1","/home/bhanu/cloud_/file2","/home/bhanu/cloud_/file3"]
fo = open("./foo.txt", "wb")
for key in rs:
    for root,dirs,files in os.walk("/home/bhanu/cloud_", topdown = True):
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

	# Get keys in bucket
	mybucket = conn.get_bucket('itcs6320bucket1')
	rs = mybucket.list()

	#Populate set of keys
	for key in rs:
	  set_keys.add(key.name)

	#Populate set of files
	stagingpath = os.path.abspath("./.Staging")
	os.chdir(stagingpath)
	#Upload files
	L_getfiles = list()
	i = 0
	for files in os.listdir("."):
		#for i in range(3):
                        
               		if (files.startswith(sel_file) and files.endswith("R1")):
				 L_getfiles.insert(i+1,files)
               		if (files.startswith(sel_file) and files.endswith("R67")):
			         L_getfiles.insert(i+1,files)
               		if (files.startswith(sel_file) and files.endswith("R38")):
				 L_getfiles.insert(i+1,files)
	for names in L_getfiles:
 		set_files.add(names)  
  
	fo = open("./foo.txt", "wb")

	# Make a key object to use for download
	from boto.s3.key import Key
	k = Key(mybucket)



	#upload these files --> in local folder but not in s3

	files_to_upload = set_files.difference(set_keys)

	if not files_to_upload:
	   fo.write("empty -- for upload - folder is in sync \n")
	else: 
 
	   for item in files_to_upload:
  		if not (item.startswith(".") or item.endswith("~")):
   			k.key = item
   			s = stagingpath + item
   			k.set_contents_from_filename(s) 
   			if not pynotify.init ("summary-only"):
    				sys.exit (1)
   			n = pynotify.Notification ("Uploaded " + item,"")
   			n.show()
  
	fo.close()

if __name__=="__main__":
    main()
