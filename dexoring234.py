import sys
import os



def sxor(s1,s2):
  return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

# xoring to get r4,5,6,7,8,9 if server 1,2,4 is available and server 3 is down.
def xor_s234_1(input1, input2):
        
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        # r2 ^ r25 = r5
	if(input1.endswith("R2") and input2.endswith("R25")):
                filename = input1.replace("R2","R5") 
         	print filename
		r5 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r5)
		print "Xoring done " + filename
	# r2 ^ r26 = r6
        elif(input1.endswith("R2") and input2.endswith("R26")):
                filename = input1.replace("R2","R6")
         	print filename
		r6 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r6)
		print "Xoring done " + filename
	# r3 ^ r37 = r7
	elif(input1.endswith("R3") and input2.endswith("R37")):
                filename = input1.replace("R3","R7")
         	print filename
		r7 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r7)
		print "Xoring done " + filename
	# r5 ^ r45 = r4
	if(input1.endswith("R5") and input2.endswith("R45")):
                filename = input1.replace("R5","R4")
         	print filename
		r4 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r4)
		print "Xoring done " + filename
	# r4 ^ r14 = r1
        elif(input1.endswith("R4") and input2.endswith("R14")):
                filename = input1.replace("R4","R1")
         	print filename
		r1 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r1)
		print "Xoring done " + filename
	# r1 ^ r19 = r9
	elif(input1.endswith("R1") and input2.endswith("R19")):
                filename = input1.replace("R1","R9")
         	print filename
		r9 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r9)
		print "Xoring done " + filename
	# r9 ^ r89 = r8
	elif(input1.endswith("R9") and input2.endswith("R89")):
                filename = input1.replace("R9","R8")
         	print filename
		r8 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(r8)
		print "Xoring done " + filename
       	
	

def generate_files(input1, input2):
        
	file1 = open(input1 ,"r")
	str1 = file1.read()
	
	file2 = open(input2, "r")
	str2 = file2.read()
	
        #f1,f2,f3
	if(input1.endswith("R5") and input2.endswith("R8")):
                filename = input1.replace("R5","-1")
         	print filename
		f1 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(f1)
		print "Xoring done " + filename
        elif(input1.endswith("R4") and input2.endswith("R7")):
                filename = input1.replace("R4","-2")
         	print filename
		f2 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(f2)
		print "Xoring done " + filename
	elif(input1.endswith("R6") and input2.endswith("R9")):
                filename = input1.replace("R6","-3")
         	print filename
		f3 = sxor(str1,str2)
		file3 = open(filename, "w")
		file3.write(f3)
		print "Xoring done " + filename






def main():
	import sys
	selected_file = sys.argv[1]
	L_Ri = list() #List for storing R1-9
	L_Rij = list() #List for storing files that end with R14.. 
	L3 = list()
	os.chdir("/home/jui/cloud")
	#L_Ri: Stores random files r1-9
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L_Ri.insert(i,files)
	#L_Rij: Stores random files that end with R14..
	for files in os.listdir("."):
		for i in range(9):
                    for j in range(9):
	  		filename = "R" +str(i+1)+str(j+1)

	                if (files.startswith(selected_file) and files.endswith(filename)):
	     			L_Rij.insert(j,files)               
	

	for p in L_Ri: print p
        for q in L_Rij: print q 

        for p in L_Ri: 
          for q in L_Rij:
	
               if(p.endswith("R2") and (q.endswith("R25"))):
                       xor_s234_1(p,q)
	       if(p.endswith("R2") and (q.endswith("R26"))):
                       xor_s234_1(p,q)
	       if(p.endswith("R3") and (q.endswith("R37"))):
                       xor_s234_1(p,q)

	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)
       

        for p in L3: 
          for q in L_Rij:
               if(p.endswith("R5") and (q.endswith("R45"))):
                       xor_s234_1(p,q)
               

	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)
        for p in L3: 
          for q in L_Rij:
	       if(p.endswith("R4") and (q.endswith("R14"))):
                       xor_s234_1(p,q)
	
	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)
        for p in L3: 
          for q in L_Rij:
	       if(p.endswith("R1") and (q.endswith("R14"))):
                       xor_s234_1(p,q)
	
	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)

        for p in L3: 
          for q in L_Rij:
	       if(p.endswith("R1") and (q.endswith("R19"))):
                       xor_s234_1(p,q)
	
	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)

        for p in L3: 
          for q in L_Rij:
	       if(p.endswith("R9") and (q.endswith("R89"))):
                       xor_s234_1(p,q)
	
	#L3: Stores generated random files 
	for files in os.listdir("."):
		for i in range(9):
                    	if (files.startswith(selected_file) and files.endswith("R"+str(i+1))):
	     			L3.insert(i,files)

       
        for p in L3: 
          for q in L3:

               if(p.endswith("R5") and (q.endswith("R8"))):
                       generate_files(p,q)
	       if(p.endswith("R4") and (q.endswith("R7"))):
                       generate_files(p,q)
	       if(p.endswith("R6") and (q.endswith("R9"))):
                       generate_files(p,q)   


if __name__=="__main__":
    main()
       










