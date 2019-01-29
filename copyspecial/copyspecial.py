#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir, special_name):
  filenames = os.listdir(dir)
  pat = r'__\w+__'
  target_filename = [filename for filename in filenames if (re.search(pat, filename))]
  # print target_filename
  return map(lambda name:os.path.abspath(name), target_filename)

def copy_to_dir(file_list, todir):
  for file in file_list:
    new_file = os.path.join(todir, os.path.basename(file))
    print file, " --- ", new_file
    shutil.copy(file, new_file)

def zip_file(file_list, zipdir):
  zip_cmd = "zip " + zipdir
  for file in file_list:
    zip_cmd += ' ' + file
  print zip_cmd
  (status, output) = commands.getstatusoutput(zip_cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(status)
  print output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  file_list = get_special_paths('.',"__something__")
  print file_list

  # copy_to_dir(file_list, todir)

  zip_file(file_list, tozip)


if __name__ == "__main__":
  main()
