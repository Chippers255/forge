import os
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Do you want to setup here? (y/n)")
    while True:
        ans = input("Do you want to setup in this folder? (y/n): ")
        if ans == "y":
            break
        elif ans == "n":
            exit(0)
    print()
    print("Forge template will be created in {0}".format(os.getcwd()))
    

# end def main


if __name__ == "__main__":
    main()