#!/Users/kidseven112002/Google Drive/Main_DB/6_training/Python python
#To find a file

import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#Program input
fpin = raw_input("what pattern are you looking to remove from files?: ")
dp = raw_input("What directory would you like to search? (Add the / at end): ")
fp = '*' + fpin + '*'
find(fp, dp)