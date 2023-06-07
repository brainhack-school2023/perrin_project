#!/usr/bin/env python3

import os
import glob
import json
import csv
import pandas as pd

from pathlib import Path

# Note:
# It is recommended to craft the command such that it can run in the root directory of the dataset that the command will be recorded in. 
# However, as long as the command is executed somewhere underneath the dataset root, 
# the exact location will be recorded relative to the dataset root.


def fix_json_schema(input_path):
    """ Fix Error 1 by modifying CogAtlasID as url (in root files and not leaves)
    Error 1: [Code 55] JSON_SCHEMA_VALIDATION_ERROR
    Invalid JSON file. The file is not formatted according the schema.
    Example:
        Location: ds000201/sub-9001/ses-1/func/sub-9001_ses-1_task-arrows_bold.json
        Reason: Invalid JSON file. The file is not formatted according the schema.
        Evidence: .CogAtlasID should match format "uri"
    Fix source: URI formatting of the default "TODO" value for "CogAtlasID" #473 (https://github.com/nipy/heudiconv/pull/473)
    Example url: https://www.cognitiveatlas.org/concept/id/trm_557b4844ca14d/
    Other sources:
        BIDS Validator error - [Code 55] JSON_SCHEMA_VALIDATION_ERROR 
        https://neurostars.org/t/bids-validator-error-code-55-json-schema-validation-error-effectiveechospacing/3704
        CogAtlasID error for json files that don"t contain a CogAtlasID field (https://github.com/bids-standard/bids-validator/issues/1139)
        (code: 55 - JSON_SCHEMA_VALIDATION_ERROR) #1104 (https://github.com/bids-standard/bids-validator/issues/1104)
    """
    relative_path = os.path.join(input_path, "task-*_bold.json")
    task_json_files = sorted(glob.glob(relative_path))
    for filename in task_json_files:
        # Read .json file
        with open(filename, 'r') as ff:
            data = json.load(ff)
            # Apply only if it has not been fixed yet
            if "CogAtlasID" in data.keys() and "https://www.cognitiveatlas.org/concept/id/" not in data["CogAtlasID"]:
                new_format = "https://www.cognitiveatlas.org/concept/id/" + data["CogAtlasID"] + "/"
                data["CogAtlasID"] = new_format
            with open(filename, 'w') as ff:
                json_object = json.dumps(data, indent=3)
                ff.write(json_object)


def fix_beh_tsv(input_path):
    """ Fix for errors 2 and 3: merge even and odd rows which were separated before
    Error 2: [Code 22] TSV_EQUAL_ROWS
    All rows must have the same number of columns as there are headers.
    Example
        Location: ds000201/sub-9001/ses-1/beh/sub-9001_ses-1_task-PVT_events.tsv
        Reason: All rows must have the same number of columns as there are headers.
        Line: 2 row 1: 12.7

    Error 3: [Code 23] TSV_EMPTY_CELL
    Empty cell in TSV file detected: The proper way of labeling missing values is "n/a".
    Example:
        Location: ds000201/sub-9001/ses-1/beh/sub-9001_ses-1_task-PVT_events.tsv
        Reason: Missing value at column # 1
        Line: 3 row 2: n/a 0.395
    """
    relative_path = os.path.join(input_path, "sub-*/ses-*/beh/sub-*_task-PVT_events.tsv")
    beh_tsv_files = sorted(glob.glob(relative_path)) # os.path.join(dataset_dir, relative_path)
    for filename in beh_tsv_files:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter="\t")
            headers = next(reader)
            reader_df = pd.DataFrame(reader)
            # Apply only if it has not been fixed yet
            if (reader_df.head(1).values == None).any():
                even = reader_df[reader_df.index % 2 == 0].reset_index(drop=True)
                odd = reader_df[reader_df.index % 2 == 1].reset_index(drop=True)
                new_df = pd.concat([even.iloc[:, :1], odd.iloc[:, 1:]], axis=1)
                new_df.columns = headers
                # Save the modified .tsv file
                new_df.to_csv(filename, sep="\t", index=False)


## Error 4: [Code 90] SIDECAR_WITHOUT_DATAFILE
# A json sidecar file was found without a corresponding data file

# Error due to DataLad because the big files were not retrieved yet


def fix_scans_filename(input_path):
    """ Fix: remove lines fieldmap, imaginary, real
    Error 5: [Code 129] SCANS_FILENAME_NOT_MATCH_DATASET
    The filename in scans.tsv file does not match what is present in the BIDS dataset.
    """
    relative_path = os.path.join(input_path, "sub-*/ses-*/sub-*_ses-*_scans.tsv")
    beh_tsv_files = sorted(glob.glob(relative_path)) # os.path.join(dataset_dir, relative_path)
    for filename in beh_tsv_files:
        with open(filename, "r") as file:
            df = pd.read_csv(filename, delimiter="\t")
            values_to_remove = ["fieldmap", "imaginary", "real"]
            pattern = '|'.join(values_to_remove)
            new_df = df.loc[~df["filename"].str.contains(pattern, case=False)].reset_index(drop=True)
            # Save the modified .tsv file
            new_df.to_csv(filename, sep="\t", index=False)

def main(repo_path):
    input_path = repo_path / "input"
    # Fix error 1
    fix_json_schema(input_path)
    # Fix errors 2 and 3
    fix_beh_tsv(input_path)
    # Fix error 5
    fix_scans_filename(input_path)


if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)


