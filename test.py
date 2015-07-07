#!/usr/bin/python
import sys
import os
import boto
import appindicator
import pynotify
import gtk
a = appindicator.Indicator('test', os.path.join(os.path.abspath("."),"dalmation.jpeg"), appindicator.CATEGORY_APPLICATION_STATUS)
a.set_status( appindicator.STATUS_ACTIVE )
m = gtk.Menu()
ci = gtk.MenuItem( 'Download' )
qi = gtk.MenuItem( 'Display All Files' )
m.append(ci)
m.append(qi)
a.set_menu(m)
ci.show()
qi.show()

def responseToDialog(entry, dialog, response):
    dialog.response(response)

def check_S1():
    #Connect to your account
    from boto.s3.connection import S3Connection
    conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')
    chk = "true" # if connection present
    nonexistent = conn.lookup('itcs6320bucket1')
    if nonexistent is None:
     print "No such bucket!"
     chk = "false"
    else:
     print " is present"
     chk = "true"
    return chk

def check_S2():
   
    #Connect to your account
    from boto.s3.connection import S3Connection
    conn = S3Connection('iNsxWj-TBZqwkWbydXTN',
                        'ZHKL_srw304yh_yKX979O-cnzJ3DWF9vmNM_07vU',
                        host = 'objects.dreamhost.com',
                        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                       )
    chk = "true"# if connection present
    nonexistent = conn.lookup('meinbucket')
    if nonexistent is None:
     print "No such bucket!"
     chk = "false"
    else:
     print " is present"
     chk = "true"
    return chk


def check_S3():
    
    #Connect to your account
    from boto.s3.connection import S3Connection
    conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')
    chk = "true" # if connection present
    nonexistent = conn.lookup('itcs6320bucket2')
    if nonexistent is None:
     print "No such bucket!"
     chk = "false"
    else:
     print " is present"
     chk = "true"
    return chk

def check_S4():
   
    #Connect to your account
    from boto.s3.connection import S3Connection
    conn = S3Connection('iNsxWj-TBZqwkWbydXTN',
                        'ZHKL_srw304yh_yKX979O-cnzJ3DWF9vmNM_07vU',
                        host = 'objects.dreamhost.com',
                        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                       )
    chk = "true" # if connection present
    nonexistent = conn.lookup('minabucket')
    if nonexistent is None:
     print "No such bucket!"
     chk = "false"
    else:
     print " is present"
     chk = "true"
    return chk




def getText():
    #base this on a message dialog
    dialog = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    dialog.set_markup('Please enter the filename <b>name</b>:')
    #create the text input field
    entry = gtk.Entry()
    #allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Name:"), False, 5, 5)
    hbox.pack_end(entry)
    #some secondary text
    dialog.format_secondary_markup("This will be used for <i>identification</i> purposes")
    #add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    #go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text





def checkStatus(item):
  print "Hello"
  str1 = getText() 
  
  s1 = check_S1()
  s2 = check_S2()
  s3 = check_S3()
  s4 = check_S4()

  if(s1 == "true" and s2 == "true" and s3 == "true" and s4 == "true"):
     print " do default dexor 123"
     commandstring1 = "python download_server1.py %s" % (str1)
     commandstring2 = "python dh_download_server2.py %s" % (str1)
     commandstring3 = "python download_server3.py %s" % (str1)
     commandstring4 = "python dexoring123.py %s" % (str1)
     commandstring5 = "python FileSplitter.py -i %s -n 3 -j" % (str1)
     commands = [commandstring1,commandstring2,commandstring3,commandstring4]
     for command in commands:
    	if os.system(command) == 0:
    	# Check for failure and wait
    	 print "                           Completed downloading"
    	 continue
        else:
     	 print "ERROR"
     	 break
 
     os.chdir(os.path.abspath("./MagicBox"))
     os.system(commandstring5)
  else:
      	if(s1 == "false"):
       		print " dexor from server 234"
  		commandstring1 = "python download_server3.py %s" % (str1)
  		commandstring2 = "python dh_download_server2.py %s" % (str1)
  		commandstring3 = "python dh_download_server4.py %s" % (str1)
		commandstring4 = "python dexoring234.py %s" % (str1)
		commandstring5 = "python FileSplitter.py -i %s -n 3 -j" % (str1)
  		commands = [commandstring1,commandstring2,commandstring3,commandstring4]
  		for command in commands:
    			if os.system(command) == 0:
        		# Check for failure and wait
        		 print "                           Completed downloading"
        		 continue
    		        else:
        		 print "ERROR"
       			 break
 
  		os.chdir(os.path.abspath("./MagicBox"))
  		os.system(commandstring5)


       	if(s2 == "false" ):
    		print " dexor from server 134"
  		commandstring1 = "python download_server1.py %s" % (str1)
  		commandstring2 = "python download_server3.py %s" % (str1)
  		commandstring3 = "python dh_download_server4.py %s" % (str1)
		commandstring4 = "python dexoring134.py %s" % (str1)
		commandstring5 = "python FileSplitter.py -i %s -n 3 -j" % (str1)
  		commands = [commandstring1,commandstring2,commandstring3,commandstring4]
  		for command in commands:
    			if os.system(command) == 0:
        		# Check for failure and wait
        		 print "                           Completed downloading"
        		 continue
    		        else:
        		 print "ERROR"
       			 break
 
  		os.chdir(os.path.abspath("./MagicBox"))
  		os.system(commandstring5)
       	if(s3 == "false"):
    		print " dexor from server 124"
  		commandstring1 = "python download_server1.py %s" % (str1)
  		commandstring2 = "python dh_download_server2.py %s" % (str1)
  		commandstring3 = "python dh_download_server4.py %s" % (str1)
		commandstring4 = "python dexoring124.py %s" % (str1)
		commandstring5 = "python FileSplitter.py -i %s -n 3 -j" % (str1)
  		commands = [commandstring1,commandstring2,commandstring3,commandstring4]
  		for command in commands:
    			if os.system(command) == 0:
        		# Check for failure and wait
        		 print "                           Completed downloading"
        		 continue
    		        else:
        		 print "ERROR"
       			 break
 
  		os.chdir(os.path.abspath("./MagicBox"))
  		os.system(commandstring5)
       	if(s4 == "false"):
       		print " dexor from server 123"
  		commandstring1 = "python download_server1.py %s" % (str1)
  		commandstring2 = "python dh_download_server2.py %s" % (str1)
  		commandstring3 = "python download_server3.py %s" % (str1)
		commandstring4 = "python dexoring123.py %s" % (str1)
		commandstring5 = "python FileSplitter.py -i %s -n 3 -j" % (str1)
  		commands = [commandstring1,commandstring2,commandstring3,commandstring4]
  		for command in commands:
    			if os.system(command) == 0:
        		# Check for failure and wait
        		 print "                           Completed downloading"
        		 continue
    		        else:
        		 print "ERROR"
       			 break
 
  		os.chdir(os.path.abspath("./MagicBox"))
  		os.system(commandstring5)


  
ci.connect('activate', checkStatus)

def quit(item):
        #gtk.main_quit()
        os.system("python display.py")

qi.connect('activate', quit)

gtk.main()
