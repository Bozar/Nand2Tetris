import sys
from pathlib import Path


# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
def readFile(folder, fileName):
    file = open(Path(sys.path[0], folder) / fileName)
    content = file.read()
    split = content.split('\n')
    file.close()

    return split


def writeFile(folder, fileName, content):
    file = open(Path(sys.path[0], folder) / fileName, 'w')
    file.write(content)
    file.close
