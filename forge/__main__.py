import os
import sys


def make(path):
    if not os.path.exists(path):
        os.makedirs(path)
# end def make


def create_folders(cwd):
    # Create Data Folders
    make(os.path.join(cwd, "data", "raw"))
    make(os.path.join(cwd, "data", "interim"))
    make(os.path.join(cwd, "data", "processed"))
    make(os.path.join(cwd, "data", "output"))

    # Create Docs Folder
    make(os.path.join(cwd, "docs"))

    # Create Models Folder
    make(os.path.join(cwd, "models"))

    # Create Notebooks Folder
    make(os.path.join(cwd, "notebooks"))

    # Create Reports Folder
    make(os.path.join(cwd, "reports", "images"))

    # Create Source Folder
    make(os.path.join(cwd, "src", "data"))
    make(os.path.join(cwd, "src", "metrics"))
    make(os.path.join(cwd, "src", "models"))
    make(os.path.join(cwd, "src", "processing"))
    make(os.path.join(cwd, "src", "utils"))
# end def create_folder


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    cwd = os.getcwd()

    print("Do you want to setup here? (y/n)")
    while True:
        ans = input("Do you want to setup in this folder? (y/n): ")
        if ans == "y":
            break
        elif ans == "n":
            exit(0)
    print()
    print("Forge template will be created in {0}".format(cwd))
    create_folders(cwd)
# end def main


if __name__ == "__main__":
    main()