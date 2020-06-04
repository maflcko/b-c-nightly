import argparse
from enum import Enum
import os
import pathlib
import sys
import urllib.request
import re
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--srcdir', type=str)
parser.add_argument('--builddir', type=str)
args = parser.parse_args()

def main():
    root_folder = os.path.abspath(os.path.dirname(__file__))
    src_dir = os.path.normpath(args.srcdir.replace('/c/Users/', 'C:\\Users\\'))
    build_dir = os.path.normpath(args.builddir.replace('/c/Users/', 'C:\\Users\\'))

    print(os.getenv('PYTHONIOENCODING'))
    print(sys.stdin.encoding)
    print(sys.stdout.encoding)
    assert 'UTF-8'.lower() == sys.stdin.encoding.lower() == sys.stdout.encoding.lower()
    print(src_dir)
    assert os.path.isdir(src_dir)  # Make sure to git clone bitcoin-core

    config_file = os.path.join(src_dir, 'test', 'config.ini')
    shutil.copyfile(os.path.join(root_folder, 'config.ini'), config_file)
    with open(config_file) as f:
        c = f.read() \
        .replace('__BUILDDIR__', build_dir) \
        .replace('__SRCDIR__', src_dir) \
        .replace('__EXEEXT__', '')
    with open(config_file, 'w') as f:
        f.write(c)

if __name__ == "__main__":
    main()
