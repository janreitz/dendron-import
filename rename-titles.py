# iterate over all files and rename the title to match the last term in the dot separated filename
import sys
import glob
import fileinput

def titleFromFilepath(filepath):
    return filepath.split('.')[-2].capitalize()

def replaceTitleInFile(filepath):
    with fileinput.input(filepath, inplace=True, backup='.bak') as f:
        for line in f:
            if line.startswith("title: "):
                line = "title: " + titleFromFilepath(filepath) + '\n'
            print(line, end='')

def replaceImageLinks(filepath):
    

if __name__ == '__main__':
    for filepath in glob.iglob(sys.argv[1], recursive=True):
        print(filepath)
        replaceTitleInFile(filepath)
