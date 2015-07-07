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
	conn = S3Connection('iNsxWj-TBZqwkWbydXTN',
                            'ZHKL_srw304yh_yKX979O-cnzJ3DWF9vmNM_07vU',
                            host = 'objects.dreamhost.com',
                            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                           )

	#initialize sets to hold keys and files in local folder
	from sets import Set
	set_keys = Set([])
	set_files = Set([])

	# Get keys in bucket
	mybucket = conn.get_bucket('meinbucket')
	


	stagingpath = os.path.abspath("./.Staging")
	os.chdir(stagingpath)
	#Upload files
	L_getfiles = list()
        i = 0
	for files in os.listdir("."):
		#for i in range(3):
                        
               		if (files.startswith(sel_file) and files.endswith("R2")):
				 L_getfiles.insert(i+1,files)
               		elif (files.startswith(sel_file) and files.endswith("R14")):
			         L_getfiles.insert(i+1,files)
               		elif (files.startswith(sel_file) and files.endswith("R89")):
				 L_getfiles.insert(i+1,files)
			
	print "List from selected files"
	for p in L_getfiles:
  		print p  
  
	fo = open("./foo.txt", "wb")


	for item in L_getfiles:
  		if not (item.startswith(".") or item.endswith("~")):
   			
        		key = mybucket.new_key(item)
			file1 = open(item ,"r")
			str1 = file1.read()
        		key.set_contents_from_string(str1) 
   			if not pynotify.init ("summary-only"):
    				sys.exit (1)
   			n = pynotify.Notification ("Uploaded " + item,"")
   			n.show()
  
	fo.close()
        for key in mybucket.list():
          print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )


if __name__=="__main__":
    main()
