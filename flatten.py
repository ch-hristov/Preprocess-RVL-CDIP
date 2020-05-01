import shutil
import os.path
import sys


directory_target = sys.argv[1]

import os
import itertools
import shutil

def generate_filename(extension):
    xx = str(uuid.uuid4()) + extension
    return xx

def move(destination):
    all_files = []
    guid = 0
    for root, _dirs, files in itertools.islice(os.walk(destination), 1, None):
        for filename in files:
            final_destination = os.path.join(root,filename)
            os.rename(final_destination,os.path.dirname(final_destination) + str(guid) + '.png')
            all_files.append(os.path.dirname(final_destination) + str(guid) + '.png')
            guid= guid + 1

    for filename in all_files:
        shutil.move(filename, os.path.join(destination,os.path.basename(filename)))

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]


directories = get_immediate_subdirectories(directory_target)
for dir in directories:
    move(directory_target + os.path.sep + dir)