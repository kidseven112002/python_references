#!/user/kidseven112002/Google Drive/Main_DB/6_training/Python/ python
#Loop to find text in file and remove; search the current working directory

import os, fnmatch, sys

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#Yes/No loop query
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
            "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                            "(or 'y' or 'n').\n")

#Test query_yes_no question
#query_yes_no("Is cabbage yummier than cauliflower?")

#Program input
fpin = raw_input("what pattern are you looking to remove from files?: ")
dp = raw_input("What directory would you like to search? (Add the / at end): ")
fp = '*' + fpin + '*'
find(fp, dp)
modifiedfiles = []
x=0

for file in os.listdir(dp):
    if fnmatch.fnmatch(file, fp):
        fs = file.split(fpin)
        newfile = ''.join(fs)
        ans = query_yes_no("\nChange <" + file + "> to <" + newfile + ">?")
        if ans == True:
            os.rename(dp + file, dp + newfile)
            modifiedfiles.append(newfile)
            x+=1

print("\nThese are the new file names:")

for x in range(x):
    print(modifiedfiles[x])




