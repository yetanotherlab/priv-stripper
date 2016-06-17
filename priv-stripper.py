#!/usr/bin/env python

import argparse, os, sys


def main(argv):
    recurse, locations = parse_args(argv)
    print recurse, locations
    for location in locations:
        recurse_dir(location)
    else:
        strip_priv(location)

def parse_args(argv):
    parser = argparse.ArgumentParser(description='Removes any PRIV tags from the given file or directory')
    parser.add_argument('-r', '--recurse', action='store_true', dest='recurse', default=False, help='recurse into child directories')
    parser.add_argument('location', nargs='+', help='a file or directory to process')
    args = parser.parse_args()
    return args.recurse, args.location


def recurse_dir(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            strip_priv(os.path.join(root, name))
        for name in dirs:
            recurse_dir(os.path.join(root, name))


def strip_priv(file):
    print 'Stripped PRIV tag from ', file
    # TODO Make this happen


def priv_exists(file):
    """
    Determines if the given file's metadata contains a PRIV frame.
    """
    print 'Found PRIV tag in file', file
    # TODO Make this happen
    return True


if __name__ == '__main__':
    main(sys.argv[1:])
