import os
from difflib import SequenceMatcher
import sys

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

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)

Usage:
python rename.py
"""

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_most_sim(target):
    max_sim = 0
    max_sim_id = False
    for img_id in img_labels:

        this_sim = similar(target, img_id)
        if this_sim > max_sim:
            max_sim = this_sim
            max_sim_id = img_id
            
    return [max_sim, max_sim_id]
 
segments_path = "../other-categories-seg/"
images_path   = "../othercategories/"

seg_labels = [label for label in os.listdir(segments_path)]
img_labels = [label for label in os.listdir(images_path)]

path =  os.getcwd()


i = 0
j = 0
for seg_id in seg_labels:
    if (seg_id in img_labels):
#         print("{} - have image : {}".format(seg_id, seg_id in img_labels))
        i = i + 1
    else:
        sim, im_id = get_most_sim(seg_id)
        question = "{} | {} ({})".format(seg_id,im_id,sim)
        if query_yes_no(question): 
            os.rename(im_id, seg_id)
            # print(images_path + im_id,  segments_path +seg_id)           

        else:
            j = j + 1
        
print("correct {} : wrong {}".format(i, j))