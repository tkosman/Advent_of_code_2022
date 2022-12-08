import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        

def count_score_of_files(droga):
    score = 0
    listOfFiles = getListOfFiles(droga)
    for elem in listOfFiles:
        if not '/.' in elem:
            file_stats = os.stat(elem)
            score += file_stats.st_size
    return score

# FILE NAME
path = 'hah'

all_dirs = [x[0] for x in os.walk(path)]

total_score = 0

for directory in all_dirs:
    wynik = count_score_of_files(directory)
    if wynik <= 100000:
        total_score += wynik

print(total_score)