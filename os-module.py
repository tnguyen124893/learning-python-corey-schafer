import os
from datetime import datetime
# Learn to use module OS
    #1 Get current working directory: os.getcwd()
    #2 Change directory: os.chdir()
    #3 Create folder:
        #Create a single folder: os.mkdir()
        #Create a folder and intermediate folders: os.makedirs() --> Recommended
    #4 Delete folder:
        #Delete only this folder: os.rmdir() --> Recommended
        #Delete this folder and all intermediate folders before it: os.removedirs()
    #5 List folders: os.listdir()
    #6 Rename file: os.rename()
    #7 Get attributes of a file: os.stat()
    #8 Go throught all directories and files
        # for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        #     print('Current Path:', dirpath)
        #     print('Directories:', dirnames)
        #     print('Files:', filenames)
        #     print()
    #9 Get environment variable: os.environ.get()
    #10 Working with file path: os.path
os.chdir('/Users/tungnguyen/Learning & Job/')

file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')
print(file_path)