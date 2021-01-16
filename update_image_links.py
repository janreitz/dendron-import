# iterate over all files and reformat links from [#1](/#2) -> [[#1|#2]]
import sys
import re
import glob
import fileinput

IMAGE_LINK_PATTERN = re.compile(r'\!\[\[(.*?)\|(.*?)\]\]')

def find_new_target(match):
    # extract a glob pattern from the old link target
    glob_term = match.group(2).split('.')[-2]

    # glob search in the assets/ directory
    glob_result = glob.glob('assets/' + glob_term + '*')
    #print('glob term:' + glob_term + ' yielded: ' + str(glob_result))
    if len(glob_result) == 0:
        return glob_term
    else:
        target = glob_result[0]
        #print(f"Found possible target: '{target}'")
        return target

def retarget_link(match):
    target = find_new_target(match)
    return r'![' + match.group(1) + r'](' + target + r')'

def replaceLinksInFile(filepath):
    with fileinput.input(filepath, inplace=True, backup='.bak', mode='r') as f:
        for i, line in enumerate(f):
            #print(f'Searching in Line {i}: {line}')
            while IMAGE_LINK_PATTERN.search(line):
                #print(f"found a link in '{filepath}' Line {i}")
                line = IMAGE_LINK_PATTERN.sub(retarget_link, line)
            print(line, end='')

if __name__ == '__main__':

    for filepath in glob.iglob(sys.argv[1], recursive=True):
        print(f"Searching image links in: '{filepath}'...")
        replaceLinksInFile(filepath)
