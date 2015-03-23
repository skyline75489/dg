#! /usr/bin/env python

import sys
import pathlib
import argparse
import json


def read_json(file_path):
    with open(file_path) as f:
        try:
            r = json.loads(f.read())
        except ValueError:
            print("Error: JSON file is not valid.")
            sys.exit(1)
        return r


def generate_dir_with_json(json, dir_path):
    current_path = pathlib.Path(dir_path)
    for i in json:
        if isinstance(i, str):
            output_path = current_path.joinpath(i)
            output_path.open('w')
        elif isinstance(i, dict):
            for key in i:
                output_path = current_path.joinpath(key)
                output_path.mkdir()
                generate_dir_with_json(i[key], output_path)


def main():
    parser = argparse.ArgumentParser(
        description="A dir generator"
    )
    parser.add_argument('-d', '--dir', type=str,
                        help='set target dir path. defaults to ./',
                        default='./')
    parser.add_argument('-f', '--file', type=str,
                        help='set config file path. defaults to ./index.json',
                        default='./index.json')
    args = parser.parse_args()
    file_path = args.file
    dir_path = args.dir
    json = read_json(file_path)
    generate_dir_with_json(json, dir_path)

if __name__ == '__main__':
    main()
