#!/usr/bin/env python

import gtk, pango

class TextViewAdvanced:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(600, 600)
        
        vbox = gtk.VBox(False, 5)
        scrolledwindow = gtk.ScrolledWindow()
        scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        hbox = gtk.HBox(False, 5)
        
        texttagtable = gtk.TextTagTable()
        self.textbuffer = gtk.TextBuffer(texttagtable)
        self.textview = gtk.TextView(self.textbuffer)
        self.textview.set_wrap_mode(gtk.WRAP_WORD)
        
        button_bold = gtk.Button("EXIT", gtk.STOCK_BOLD)
        button_italic = gtk.Button("Italic", gtk.STOCK_ITALIC)
        button_underline = gtk.Button("Underline", gtk.STOCK_UNDERLINE)
        
        self.texttag_bold = gtk.TextTag("bold")
        self.texttag_bold.set_property("weight", pango.WEIGHT_BOLD)
        texttagtable.add(self.texttag_bold)
        self.texttag_italic = gtk.TextTag("italic")
        self.texttag_italic.set_property("style", pango.STYLE_ITALIC)
        texttagtable.add(self.texttag_italic)
        self.texttag_underline = gtk.TextTag("underline")
        self.texttag_underline.set_property("underline", pango.UNDERLINE_SINGLE)
        texttagtable.add(self.texttag_underline)
        
        #hbox.pack_start(button_bold)
        #hbox.pack_start(button_italic)
        #hbox.pack_start(button_underline)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button_bold.connect("clicked", self.bold_text)
        button_italic.connect("clicked", self.italic_text)
        button_underline.connect("clicked", self.underline_text)
        
        window.add(vbox)
        vbox.pack_start(scrolledwindow, True, True, 0)
        vbox.pack_start(hbox, False, False, 0)
        scrolledwindow.add(self.textview)

        #file = open("gtk.txt", "r")
        #self.textbuffer.set_text(file.read())
        #file.close()
        from boto.s3.connection import S3Connection
	conn = S3Connection('AKIAIHELJGCR4FDM5KKA','w6Vs+iZ4iaparJvPQFXyrAB27ACAqOI2ddJdw3mO')


	


	all_filenames = list()
        selected_files = list()

        str1 = " "
	# Get keys in bucket
	mybucket = conn.get_bucket('itcs6320bucket1')
	rs = mybucket.list()

	i = 0
	for key in rs:
    		all_filenames.insert(i+1,key.name)
        
	j = 0
	for files in all_filenames: 
	
        	 if (files.endswith("R1")):
			       filename = files.replace("R1"," ") 
        	               selected_files.insert(j+1,filename)
        	 if (files.endswith("R67")):
			       filename = files.replace("R67"," ") 
        	               selected_files.insert(j+1,filename)
        	 if (files.endswith("R38")):
			       filename = files.replace("R38"," ") 
        	               selected_files.insert(j+1,filename)
        	
        	 
        newList = list(set(selected_files))
        
        
	for p in newList:
  		str1 = str1 + "  " + p   
        
        self.textbuffer.set_text(str1)
             
        

      
        
        window.show_all()
    
    def bold_text(self, widget):
        if self.textbuffer.get_selection_bounds() != ():
            start, end = self.textbuffer.get_selection_bounds()
            self.textbuffer.apply_tag(self.texttag_bold, start, end)
    
    def italic_text(self, widget):
        if self.textbuffer.get_selection_bounds() != ():
            start, end = self.textbuffer.get_selection_bounds()
            self.textbuffer.apply_tag(self.texttag_italic, start, end)
    
    def underline_text(self, widget):
        if self.textbuffer.get_selection_bounds() != ():
            start, end = self.textbuffer.get_selection_bounds()
            self.textbuffer.apply_tag(self.texttag_underline, start, end)

TextViewAdvanced()
gtk.main()

