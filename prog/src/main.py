import pathlib
from termcolor import colored
import sys


def walk_tree(directory, base_dir, level_counter=1):
    path = pathlib.Path(directory)
    print_files(path, base_dir, level_counter)
    dirs = [dir for dir in sorted(path.glob('*')) if dir.is_dir()]
    level_counter += 1
    for fold in dirs:
        print((level_counter - 1) * '|-', colored(fold.name, 'cyan', attrs=['bold']))
        walk_tree(fold, base_dir, level_counter)


def print_files(curr_dir, base_dir, level_counter):
    files = [item.name for item in sorted(curr_dir.glob('*')) if item.is_file()]
    for item in files:
        print(level_counter * '|-', item)


def main():
    walk_tree(sys.argv[1], sys.argv[1])


if __name__ == "__main__":
    main()
