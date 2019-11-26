import sys
import hashlib
import hmac
import os
import datetime
import csv
import random  
import string 
from os import walk
from os.path import join
from shutil import copyfile

template_file = "RPMA_template.csv"
def main():
	if len(sys.argv) < 2:
		print ("Please input the source CSV filepath !! ")
	else:
		createcsv(sys.argv[1])
	
def getCuttrntTime():
    return datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%dT%H%M%S')
	
def createcsv(sourcecsvpath):
    count =0
    if os.path.exists(template_file) != True:
        print("Error. template file is not exist:"+template_file)
        exit()
    if os.path.exists(sourcecsvpath):
        outcsvfilename = getCuttrntTime()+".csv"
        copyfile(template_file,outcsvfilename)
        outcsvfile =  open(outcsvfilename, "a", newline='', encoding="utf-8")
        for root, dirs, files in walk(sourcecsvpath):
            for f in files:
               if f.endswith(".csv"):
                  testfilepath = join(root, f) 
                  testfile = open(testfilepath, "r")
                  lines = testfile.readlines() #读取所有行 
                  last_line = lines[-1] #取最后一行    
                  outcsvfile.write(last_line)
                  testfile.close()
                  count = count+1
        outcsvfile.close()
        print("Number of test record:"+str(count)+"        Output file: "+outcsvfilename)
    else:
        print("Please input the CORRECT source CSV filepath")
		
if __name__ == "__main__":
    main()