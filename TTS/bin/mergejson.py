import argparse, os, json
from argparse import RawTextHelpFormatter
from datetime import datetime

def mergejson_multiple(json_files, output_path):
    data = {}
    for json_file in json_files:
        with open(json_file) as f:
            data.update(json.load(f))
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)


parser = argparse.ArgumentParser(
    description="""Merge multiple json file keys and values into one json file.\n\n"""
    """
    Example runs:
    python TTS/bin/mergejson.py [array of json file paths] destination_file_path
    """,
    formatter_class=RawTextHelpFormatter,
)
parser.add_argument("array_json_files", type=str, help="list of json file paths to merge.")
parser.add_argument(
    "destination_file_path",
    type=str,
    help="Path to save the merged json file.",
)

args = parser.parse_args()

mergejson_multiple(args.array_json_files.split(','), os.path.join(args.destination_file_path, "merged." + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"))