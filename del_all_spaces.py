import os
import re
import argparse


'''
To do list:
    logging
    more exception handling
    subfolders?
    comments
'''


def list_files(dir):
    filelist = [file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]
    return filelist


def replace_spaces(filelist):
    for file in filelist:
        replace = re.sub(r' ', '_', file)
        if file != replace:
            os.rename(file, replace)


def parse_args():
    parser = argparse.ArgumentParser(description='Replace all spaces in filenames with underscores.')
    parser.add_argument('-d', dest='dir', action='store', required=True,
                        help='Directory in which filenames should be processed')
    parser.add_argument('-l', dest='log_on', action='store_true', help='Turns logging on or off')

    args = parser.parse_args()

    return args


args = parse_args()
try:
    os.chdir(args.dir)
    files = list_files(args.dir)
    replace_spaces(files)
except FileNotFoundError as e:
    print('Specified direstory does not exist.\nError message: %s' % e)