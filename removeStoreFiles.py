#remove DS_Store files

import glob
import os

directories = ['X:/*', 'Y:/*', 'T:/*', 'M:/*']

for directory in directories:
    folders = glob.glob(directory)

    for folder in folders:
        for path, subdirs, files in os.walk(folder):
            for name in files:
                file = os.path.join(path, name)
                if 'DS_Store' in file:
                    os.remove(file)