import datetime
import pathlib
from termcolor import colored
import sys
import numpy as np
import json


def walk_tree(directory, base_dir, level_counter=1):
    path = pathlib.Path(directory)
    print_files(path, base_dir, level_counter)
    dirs = [dir for dir in sorted(path.glob('*')) if dir.is_dir()]
    level_counter += 1
    for fold in dirs:
        print((level_counter - 1) * '|-', colored(fold.name, 'cyan', attrs=['bold']))
        walk_tree(fold, base_dir, level_counter)


def dir_iterator(directory, base_dir, dictionary: dict):
    path = pathlib.Path(directory)
    dic = {}
    dirs = [dir for dir in sorted(path.glob('*')) if dir.is_dir()]
    for dir in dirs:
        key_value = dir_iterator(dir, base_dir, dictionary)
        dic[dir.name] = key_value

    if len(dirs) == 0:
        return add_files(path, base_dir)
    else:
        accumulator(base_dir, dic, path)
        # return {path.name: dic}
        return dic


def accumulator(base_dir, dictionary, direc):
    """'Appends' so to speak the contents or a directory
    to an exisiting dictionary"""
    dir_conts = add_files(direc, base_dir)
    keys = list(dir_conts.keys())
    values = list(dir_conts.values())
    for pos in range(len(keys)):
        dictionary[keys[pos]] = values[pos]
    return dictionary


def dir_dict(path, base_dir):
    """takes a directory and returns its contents' information
    as a dictionary"""
    return {path.name: add_files(path, base_dir)}


def print_files(curr_dir, base_dir, level_counter):
    files = [item.name for item in sorted(curr_dir.glob('*')) if item.is_file()]
    for item in files:
        print(level_counter * '|-', item)


def add_files(curr_dir, base_dir):
    dictionary = {}
    for item in sorted(curr_dir.glob('*')):
        if item.is_file():
            dictionary[item.name] = build_dict(item, base_dir)
    return dictionary


def create_printout(dic: dict):
    print('-' * 100)
    print(f'{"Filename and relative location: " : <35}{dic["location"] : <20}')
    print(f'{"Size in kilobytes " : <35}{dic["size"] : <20}')
    print(f'{"last modified " : <35}{dic["last-modified"] : <20}')


def build_dict(file_object: pathlib.Path, base_dir):
    file_dict = {}
    if file_object.is_file():
        file_dict["type"] = "file"
        time = datetime.datetime.fromtimestamp(file_object.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_dict["last-modified"] = time
        file_dict["size"] = round((file_object.stat().st_size / 1000), 1)
        file_dict["name"] = file_object.name
        path = str(file_object.resolve()).split(base_dir)
        file_dict["location"] = path[-1]
        create_printout(file_dict)
    return file_dict


def alt():
    location = '/home/ralof/Documents/spare_time/Python/projects/chk_files'
    test_loc = location + '/test_dir'
    walk_tree(test_loc, test_loc)
    directory_structure = {}
    directory = location + '/test_dir'
    directory_structure = dir_iterator(directory, directory, directory_structure)
    np.save(location + '/prog/saves/dir_structure.npy', directory_structure)
    json.dump(directory_structure, open(location + '/prog/saves/dir_structure.json', 'w'))


def normal():
    walk_tree(sys.argv[1], sys.argv[1])
    directory_structure = {}
    directory_structure = dir_iterator(sys.argv[1], sys.argv[1], directory_structure)
    np.save('prog/saves/dir_structure.npy', directory_structure)
    json.dump(directory_structure, open('prog/saves/dir_structure.json', 'w'))


def main():
    if len(sys.argv) != 2:
        alt()
    else:
        normal()


if __name__ == "__main__":
    main()
