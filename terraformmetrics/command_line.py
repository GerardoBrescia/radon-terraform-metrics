import argparse
import os
import json

import lark

from terraformmetrics.metrics_extractor import extract_all

VERSION = "0.0.1"


def get_parser():
    description = 'Extract metrics from Terraform scripts.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(action='store', dest='src', help='source file (playbook or tasks file) or directory')
    parser.add_argument('--omit-zero-metrics', dest='omit_zero_metrics', action='store_true',
                        help='omit metrics with value equal 0')
    parser.add_argument('-d', '--dest', help='destination path to save results')
    parser.add_argument('-o', '--output', action='store_true', help='shows output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)

    return parser


def load_file(path: str) -> str:
    """ Returns a String object representing the content of the file at <path>, if any; None otherwise """
    if os.path.isfile(path):
        content = ''
        with open(path, 'r') as file:
            content = file.read()

        return content


def load_dir(input_dir: str) -> dict:
    """
    Find all terraform file in the input directory and return a dictionary of k:v pairs where k is the filepath and \
        the v the content of the file at that path
    """

    dirs_stack = []

    for item in os.listdir(input_dir):
        dirs_stack.append(os.path.join(input_dir, item))

    tf_files = []

    while len(dirs_stack) > 0:
        item = dirs_stack.pop()

        if os.path.isfile(item):
            _, file_extension = os.path.splitext(item)

            if file_extension in ['.tf']:
                tf_files.append(item)

        elif os.path.isdir(item):
            for sub_item in os.listdir(item):
                dirs_stack.append(os.path.join(item, sub_item))

    scripts = dict()

    for file_path in tf_files:
        scripts[file_path] = load_file(file_path)

    return scripts


# funzione per caricare la risorsa di partenza
def load_source(path: str) -> dict:
    if os.path.isfile(path):
        return {path: load_file(path)}
    elif os.path.isdir(path):
        return load_dir(path)

    return dict()


#funzione che permette di salvare il risultato
def save_output(json_data, out_path):
    if not os.path.isfile(out_path):
        data = []
    else:
        with open(out_path, 'r') as json_file:
            data = json.load(json_file)

    data.append(json_data)

    with open(out_path, 'w') as out_file:
        json.dump(data, out_file, sort_keys=True)


def cli():
    args = get_parser().parse_args()

    scripts = load_source(args.src)
    for file_path, script in scripts.items():

        try:
            metrics = extract_all(script)
            metrics['filepath'] = file_path

            if args.omit_zero_metrics:  # Show only non-zero metrics
                metrics = {k: v for k, v in metrics.items() if v != 0}

            if args.dest:
                save_output(metrics, args.dest)

            # Pretty-print json to screen (always print if args.dest in not defined)
            if args.output or not args.dest:
                metrics_2_json = json.dumps(metrics, indent=4, sort_keys=True)
                print(metrics_2_json)

        except TypeError:
          print('\033[91m' + f'{file_path} is not a valid HCL2 file.' + '\033[0m')
        except Exception as e:
            print(f'An unknown error has occurred: {str(e)}')
