#!/usr/bin/env python
import os,sys

 
#Methods to split a file into equal sized chunks and generate chunksized random files
#R1,R2...,R6 - random files
#f1,f2,f3    - splits of input file
#R56
class GenerateSplits(object):
    def __init__(self,filepath,outputpath,numchunks):
        #location of file
        self.__filepath = filepath
        #location of folder to place the split files
        self.__outputpath = outputpath
        #Number of equal chunks to split file
        self.__numchunks = numchunks
        #chunksize
        self.__chunksize = 0
     
    def generate_random_files(self):
       #get file size
       fsize = os.path.getsize(self.__filepath)
       #Get the number of bytes to be padded
       extrabytes = fsize%self.__numchunks
       randomfilesize= (extrabytes + fsize )/ 3
       # Generate 6 random files
       for i in range(6):
            randomfilename =  os.path.basename(self.__filepath) + "R" + str(i+1) 
            commandstring = "dd if=/dev/urandom of=%s bs=1 count=%s " % (os.path.join(self.__outputpath,randomfilename),randomfilesize)
            os.system(commandstring)
        
    def split(self) :
       #Get filename
       filename = os.path.basename(self.__filepath)
       #Open file
       try:
            f = open(self.__filepath, 'rb')
       except :
            print 'failed to open'
       #get file size
       fsize = os.path.getsize(self.__filepath)
       #check if file is empty
       if fsize == 0 :
          sys.exit(1)
       #Get the number of bytes to be padded
       extrabytes = fsize%self.__numchunks
       #pad the file before splitting
       commandstring = "dd if=/dev/zero bs=1 count=%s >> %s " % (extrabytes,self.__filepath)
       os.system(commandstring)
       # Get size of each chunk
       self.__chunksize = int(float(fsize)/float(self.__numchunks))

       chunksz = self.__chunksize
       total_bytes = 0

       #Write files in staging folder
       for x in range(self.__numchunks):
            chunkfilename = filename + '-' + str(x+1) 

            # precaution for last chunk
            if x == self.__numchunks - 1:
                chunksz = fsize - total_bytes
            #Write chunk
            try:
              
                data = f.read(chunksz)
                print data
                total_bytes += len(data)
                print total_bytes
                print os.path.join(self.__outputpath,chunkfilename)
                chunkf = open(os.path.join(self.__outputpath,chunkfilename), 'wb')
                chunkf.write(data)
                chunkf.close()
            except :
                sys.exit(1)
                   
class EncodeSplits(object):
 def __init__(self,outputpath,filename):
   self.__filename = filename
   self.__outputpath = outputpath
 @staticmethod 
 def sxor(s1,s2):
   return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
 
 def generate_xor(self,input1, input2):
        os.chdir(self.__outputpath)
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        #f1,f2,f3 with r4,45,r6
        #f1 xor R5 = R8
        #f2 xor R4 = R7
        #f3 xor R6 = R9 
        #R6 xor R7 = R67
        #R3 xor R8 = R38
        #          = R14
        #          = R89,45,26,25,37,19
        #          =
	if(input1.endswith("-1") and input2.endswith("R5")):
                filename = input1.replace("-1","R8")
         	print filename
		r8 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
        elif(input1.endswith("-2") and input2.endswith("R4")):
                filename = input1.replace("-2","R7")
         	print filename
		r8 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
	elif(input1.endswith("-3") and input2.endswith("R6")):
                filename = input1.replace("-3","R9")
         	print filename
		r8 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
 
 def generate_xor2(self,input1, input2):
        os.chdir(self.__outputpath)
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        
	if(input1.endswith("R6") and input2.endswith("R7")):
                filename = input1.replace("R6","R67") 
         	print filename
		r67 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r67)
		print "Xoring done " + filename
        elif(input1.endswith("R3") and input2.endswith("R8")):
                filename = input1.replace("R3","R38")
         	print filename
		r38 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r38)
		print "Xoring done " + filename
	elif(input1.endswith("R1") and input2.endswith("R4")):
                filename = input1.replace("R1","R14")
         	print filename
		r14 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r14)
		print "Xoring done " + filename
	if(input1.endswith("R8") and input2.endswith("R9")):
                filename = input1.replace("R8","R89")
         	print filename
		r89 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r89)
		print "Xoring done " + filename
        elif(input1.endswith("R4") and input2.endswith("R5")):
                filename = input1.replace("R4","R45")
         	print filename
		r45 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r45)
		print "Xoring done " + filename
	elif(input1.endswith("R2") and input2.endswith("R6")):
                filename = input1.replace("R2","R26")
         	print filename
		r26 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r26)
		print "Xoring done " + filename
	elif(input1.endswith("R2") and input2.endswith("R5")):
                filename = input1.replace("R2","R25")
         	print filename
		r25 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r25)
		print "Xoring done " + filename
	if(input1.endswith("R3") and input2.endswith("R7")):
                filename = input1.replace("R3","R37")
         	print filename
		r37 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r37)
		print "Xoring done " + filename
        elif(input1.endswith("R1") and input2.endswith("R9")):
                filename = input1.replace("R1","R19")
         	print filename
		r19 = self.sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r19)
		print "Xoring done " + filename
  
 def run(self):
  selected_file = self.__filename
  L1 = list()
  L2 = list()
  L3 = list() 
  #L1: Stores random files r1-6
  for files in os.listdir(self.__outputpath):
		for i in range(6):
	  		if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L1.insert(i,files)
  #L2: Stores all the files
  for files in os.listdir(self.__outputpath):
		for i in range(3):
	  		if (files.startswith(selected_file) and files.endswith("-"+str(i+1))):
	     			L2.insert(i,files)
  #f1,f2,f3 with r4,45,r6
	#L2
  for p in L2: 
          for q in L1:
               if(p.endswith("-1") and (q.endswith("R5"))):
                       self.generate_xor(p,q)
               if(p.endswith("-2") and (q.endswith("R4"))):
                        self.generate_xor(p,q)
               if(p.endswith("-3") and (q.endswith("R6"))):
                        self.generate_xor(p,q)
  #L3: Store R1,R2,R3,r4,r5,r6,r7,r8,r9 in List 3	
  for files in os.listdir(self.__outputpath):
		for i in range(9):
	  		if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)
  
  for p in L3: 
          for q in L3:
               if(p.endswith("R6") and (q.endswith("R7"))):
                       self.generate_xor2(p,q)
               if(p.endswith("R3") and (q.endswith("R8"))):
                        self.generate_xor2(p,q)
               if(p.endswith("R1") and (q.endswith("R4"))):
                        self.generate_xor2(p,q)
	       if(p.endswith("R8") and (q.endswith("R9"))):
                       self.generate_xor2(p,q)
               if(p.endswith("R4") and (q.endswith("R5"))):
                        self.generate_xor2(p,q)
               if(p.endswith("R2") and (q.endswith("R6"))):
                        self.generate_xor2(p,q)
	       if(p.endswith("R2") and (q.endswith("R5"))):
                       self.generate_xor2(p,q)
               if(p.endswith("R3") and (q.endswith("R7"))):
                        self.generate_xor2(p,q)
               if(p.endswith("R1") and (q.endswith("R9"))):
                        self.generate_xor2(p,q)
   


 #Facade for Splitter and Encoder
class ArrayBPXOREncoder(object):
  def __init__(self,filepath,outputpath,numchunks):
     self.__split =  GenerateSplits(filepath,outputpath,numchunks)
     self.__encode = EncodeSplits(outputpath,os.path.basename(filepath))
  def run(self):
     self.__split.split()
     self.__split.generate_random_files()
     self.__encode.run()



def main():
       #exit if no filename
       if len(sys.argv) < 2:
         print 'Filename not provided'
         sys.exit(1)
       filename= sys.argv[1]
       #Update the location of magic folder here
       folderpath= os.path.abspath("./MagicBox")
       #Update the filepath
       filepath = os.path.join(folderpath,filename) 
       #Location of staging folder
       outputpath = os.path.abspath("./.Staging")
       #Encode the file into coded chunks
       encoder = ArrayBPXOREncoder(filepath,outputpath,3)
       encoder.run() 
               

if __name__=="__main__":
    sys.exit(main())
