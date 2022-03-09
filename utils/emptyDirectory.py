import os
import shutil

"""
    Clears the FIlES and RESULTS directories
"""


def empty_directory():
    print("Emptying the directories")
    shutil.rmtree(os.path.join(os.path.dirname(__file__), '../results/'))
    shutil.rmtree(os.path.join(os.path.dirname(__file__), '../files/'))
    os.mkdir(os.path.join(os.path.dirname(__file__), '../results/'))
    os.mkdir(os.path.join(os.path.dirname(__file__), '../files/'))
    print("Done")
