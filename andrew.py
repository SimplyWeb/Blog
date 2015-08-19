import glob
import os
import sys
import fileinput
import shutil
import fnmatch
import io
import csv


base_source_dir = 'C:\\SourceFiles\\'
base_target_dir = 'C:\\TargetFiles\\'

#The source pattern inside the files
sourcePatternList = []

#The new prefix for file rename 
prefixList = []

#target list
targetDirList = []

sourceDirectoryList = []

                               
gpsTrack = open("C:\\Users\\502436850\\Documents\\filename_convention.txt", "r")
    
#define reader and process header
csvReader = csv.reader(gpsTrack)
header = next(csvReader)
sourceDirectoryIndex = header.index('sourceDir')
sourcePatternIndex= header.index("sourcePattern")
targetDirIndex= header.index("targetDir")
prefixIndex = header.index("prefix")

#loop thru lines in file to get index           
for row in csvReader:
     sourceDirectory = (row[sourceDirectoryIndex]).strip()
     sourcePattern = (row[sourcePatternIndex]).strip()
     targetDir = (row[targetDirIndex]).strip()
     prefix = (row[prefixIndex]).strip()
     sourceDirectoryList.append(sourceDirectory)
     sourcePatternList.append(sourcePattern)
     targetDirList.append(targetDir)
     prefixList.append(prefix)

print('Search for files in %s\n' % os.path.realpath(base_source_dir))
print(sourcePatternList)
print(targetDirList)
print(prefixList)
print(sourceDirectoryList)


for dirpath, dirnames, files in os.walk(base_source_dir):

    for originalfilename in files:
          
        with open(dirpath+'/'+originalfilename, 'r+') as searchfile:

            #If the dirpath is in ack_nak subdirectory,
            #Then search, read source pattern, and send files to target directories.      
            if(dirpath in base_source_dir+sourceDirectoryList[0]+'//'):
                print('\n'+originalfilename+'\n')
                
                for line in searchfile:
                      
                    if sourcePatternList[0] in line:
                                               
                                 try:
                                    
                                     shutil.copy2(dirpath+'\\'+originalfilename,
                                                            dirpath+'\\ARCHIVE\\'+
                                                            originalfilename+'.source' )
                                     
                                   
                                     shutil.move(dirpath+'\\'+originalfilename,
                                                            base_target_dir+targetDirList[0]+'\\'+
                                                            prefixList[0]+
                                                            originalfilename )
                                     
                                        
                                 except Exception as e:
                    
                                        print('Moving...'+ str(e))

                                       
                    elif sourcePatternList[2] in line:
                                 
                                 
                                 try:

                                     shutil.copy2(dirpath+'\\'+originalfilename,
                                                           dirpath+'\\ARCHIVE\\'+
                                                           originalfilename+'.source' )
                                     
                                   
                                     shutil.move(dirpath+'\\'+originalfilename,
                                                            base_target_dir+targetDirList[0]+'\\'+
                                                            prefixList[2]+
                                                            originalfilename)
                                     
                                 except Exception as e:
                                     
                                     print('Moving...'+ str(e))

           searchfile.close()





