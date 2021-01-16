# iterate over all files and reformat image links from ![[#1|#2]] -> [![#1](glob_search('assets/#2'))
import sys
import re
import glob
import fileinput

LINK_PATTERN = re.compile(r'\[(.*?)\]\((.*?)\)')

def findTarget(match):
    glob_term = match.group(2).strip('/').replace('/', '.')
    glob_result = glob.glob('*' + glob_term + '*')
    if len(glob_result) == 0:
        return glob_term
    else:
        res = glob_result[0]
        if res.endswith('.md'):
            res = res[:-3]
        return res

def substituteLink(match):
    target = findTarget(match)
    return r'[[' + match.group(1) + '|' + target + r']]'

def replaceLinksInFile(filepath):
    with fileinput.input(filepath, inplace=True, backup='.bak') as f:
        for line in f:
            while LINK_PATTERN.search(line):
                line = LINK_PATTERN.sub(substituteLink, line)
            print(line, end='')

if __name__ == '__main__':

    for filepath in glob.iglob(sys.argv[1], recursive=True):
        print('updating: ' + filepath)
        replaceLinksInFile(filepath)