"""Runs all of the scripts and commands necessary to build the website from
scratch and to deploy it via FTP."""

import os

# move to the directory of this script, so it can execute system commands in appropriate
# directories
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# clean and build website
os.chdir("..")
os.system("tree -C -d")
os.system("bundle exec jekyll clean --trace")
os.system("bundle exec jekyll build --trace")
os.chdir("scripts")

# clean cashes and log files
import clean
# upload the website
import upload
