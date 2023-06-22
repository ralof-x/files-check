import datetime
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


def build_dict(file_object: pathlib.Path, base_dir):
    file_dict = {}
    if file_object.is_file():
        file_dict["type"] = "file"
        timestamp = file_object.stat().st_mtime
        time = datetime.datetime.fromtimestamp(file_object.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_dict["last-modified"] = time
        file_dict["size"] = round((file_object.stat().st_size / 1000), 1)
        file_dict["name"] = file_object.name
        path = str(file_object.resolve()).split(base_dir)
        file_dict["location"] = path[-1]
    return file_dict


def main():
    walk_tree(sys.argv[1], sys.argv[1])


if __name__ == "__main__":
    main()
