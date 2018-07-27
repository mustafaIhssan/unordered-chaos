import os
from tqdm import tqdm

for dirpath, dirnames, filenames in tqdm(list(os.walk("."))):
    for filename in filenames:
        full_filename = os.path.join(dirpath, filename)
        new_filename  = ".{0}.png".format("".join(full_filename.split(".")[:-1]))
        os.rename(full_filename, new_filename)