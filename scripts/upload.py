from ftplib import FTP, error_perm
import os
from getpass import getpass


def remove_content():
    """Recursively removes all non-permanent content."""
    permanent_files = ["info.php", ".gitkeep"]
    permanent_folders = ["subdom", "domains"]

    # for all subdirectories of the current directory
    for content in ftp.nlst():
        # if it's a file
        if "." in content:
            # and the content isn't permanent
            if content not in permanent_files:
                # if it's a file, delete it
                ftp.delete(content)

                print("DELETED FILE:\t\t" + ftp.pwd() + "/" + content)
        else:
            # move down to the directory and recursively call remove_content
            ftp.cwd(content)
            remove_content()

            # move up a directory and delete the folder, if it doesn't already exist
            ftp.cwd("..")
            if content not in permanent_folders:
                ftp.rmd(content)

            print("DELETED DIRECTORY:\t" + ftp.pwd() + "/" + content)


def add_content():
    """Recursively adds the content from the _site folder to the website."""
    ignore = ["scripts", "Gemfile", "Gemfile.lock", "LICENSE.txt", "README.md", "Rakefile"]
    # move to the _site
    os.chdir(os.path.join("..", "_site"))

    # get all directories
    directories = []
    for directory in [dir[0] for dir in os.walk(".")]:
        if directory[2:] != "" and directory[2:] not in ignore:
            directories.append(directory[2:].replace("\\", "/"))

    # upload (create) all directories
    for directory in sorted(directories):
        if directory not in ftp.nlst():
            ftp.mkd(directory)
            print("CREATED DIRECTORY:\t" + directory)

    # get all files
    files = [
        os.path.join(root, name)[2:].replace("\\", "/")
        for root, dirs, files in os.walk(".")
        for name in files
    ]

    # remove files which should be ignored
    for file in sorted(files):
        for ignored in ignore:
            if ignored in file.split("/"):
                print("IGNORE FILE:\t\t" + file)
                files.remove(file)

    # upload all files
    for file in files:
        ftp.storbinary("STOR " + file, open(file, "rb"))
        print("CREATED FILE:\t\t" + file)

try:
    print("searching for login file")
    login_file  = open("login_info.txt", "r")
    login_info = login_file.read().split()
    print("login file loaded successfuly")
    print("Logging as " + login_info[1])
except Exception as e:
    print("searching for login file failed")
    print("Enter login info manualy")
    login_info = [input("IP: "), input("login: "), getpass("password: ")]

# repeatedly attempt to connect to the server
while True:

    try:
        print("trying to connect to " + login_info[0])
        with FTP(login_info[0], login_info[1], login_info[2]) as ftp:
            print("Connected!")
            print(ftp.cwd("www"))

            # remove all content that isn't permanent
            remove_content()

            # add all content from _site folder which is not ignored
            add_content()

            # disconnect from the server and terminate the script
            print(ftp.quit())
            quit()
    except Exception as e:
        print(e)
        input()