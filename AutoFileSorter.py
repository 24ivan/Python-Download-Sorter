#24Ivan
#This is a short code that automatically sends the files in my download directory to a more specific folder.
#If it has cover letter in the name, send it to my cover letter folder
#If it has a '(number)' in the name, it is a duplicate and should be sent to the duplicate folder in /downloads.
#If it is a file that ends in .mov, .mp4, .gif, send it to the videos folder. If the file ends in .png ,jpeg, send it the pictures folder
import os
import shutil
import fnmatch
from pathlib import Path

#SOURCE AND DESTINATION FOLDERS, modify according to your own directory names
source = "C:/Users/Ivan/Downloads"
CoverLetterFolder = "C:/Users/Ivan/OneDrive - Brock University/Careers/Cover Letters"
duplicateFolder = 'C:/Users/Ivan/Downloads/Duplicates'
videoFolder = "C:/Users/Ivan/Videos"
picturesFolder = "C:/Users/Ivan/OneDrive - Brock University/Pictures"

files = os.listdir(source)

def checkFilePath(target, file):
    expectedPath = Path(target + "/" + file)
    occupied = expectedPath.exists()
    return occupied     

if not os.path.exists(duplicateFolder):
    os.makedirs(duplicateFolder)

for file in files:
    sourceFile = source + "/" + file
    if fnmatch.fnmatch(file, '*Cover Letter.pdf'):
        if not os.path.exists(CoverLetterFolder): #if a cover letter directory does not exist, create one
            os.makedirs('C:/Users/Ivan/Downloads/Cover Letters') #The cover letter folder directory will now be in downloads by default
            CoverLetterFolder = 'C:/Users/Ivan/Downloads/Cover Letters' #update the var
        else:    print(sourceFile)
        occupied = checkFilePath(CoverLetterFolder, file) 
        if not occupied:
            shutil.move(sourceFile, CoverLetterFolder)
        else:
            shutil.move(sourceFile, duplicateFolder)
        continue
    
    if fnmatch.fnmatch(file, '*(?).*'): #check for duplicate files, which will usually have (1), (2), ... (10) in their names
        shutil.move(sourceFile, duplicateFolder)
        continue

    if file.endswith(('.mov', '.mp4', '.gif')):
        print(file)
        occupied = checkFilePath(videoFolder, file) #return true if the directory already contains a file with the same name, as the source file
        if not occupied:
            shutil.move(sourceFile, videoFolder)
        else: 
            shutil.move(sourceFile, duplicateFolder)
        continue

    if file.endswith(('.png', '.jpg', '.jpeg')):
        print(file)
        occupied = checkFilePath(picturesFolder, file)
        if not occupied:
            shutil.move(sourceFile, picturesFolder)
        else: 
            shutil.move(sourceFile, duplicateFolder)
        continue



        

                      
