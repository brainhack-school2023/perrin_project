import os
import glob
import csv
import pandas as pd



dataset_dir = '../data/ds000201/'

## Error 1: [Code 55] JSON_SCHEMA_VALIDATION_ERROR
# Invalid JSON file. The file is not formatted according the schema.
# Example:
#   Location: ds000201/sub-9001/ses-1/func/sub-9001_ses-1_task-arrows_bold.json
#   Reason: Invalid JSON file. The file is not formatted according the schema.
#   Evidence: .CogAtlasID should match format "uri"

# Fix (in root files):
task_json_files = sorted(glob.glob(os.path.join(dataset_dir, 'task-*_bold.json')))
print('task_json_files:', task_json_files[0:2])
"""
for filename in task_json_files:
  delete "CogAtlasID" or modify with url
"""

# Fix source: BIDS Validator error - [Code 55] JSON_SCHEMA_VALIDATION_ERROR 
# https://neurostars.org/t/bids-validator-error-code-55-json-schema-validation-error-effectiveechospacing/3704
# Other sources:
#   CogAtlasID error for json files that don't contain a CogAtlasID field (https://github.com/bids-standard/bids-validator/issues/1139)
#   (code: 55 - JSON_SCHEMA_VALIDATION_ERROR) #1104 (https://github.com/bids-standard/bids-validator/issues/1104)


## Error 2: [Code 22] TSV_EQUAL_ROWS
# All rows must have the same number of columns as there are headers.
# Example
#   Location: ds000201/sub-9001/ses-1/beh/sub-9001_ses-1_task-PVT_events.tsv
#   Reason: All rows must have the same number of columns as there are headers.
#   Line: 2 row 1: 12.7

## Error 3: [Code 23] TSV_EMPTY_CELL
# Empty cell in TSV file detected: The proper way of labeling missing values is "n/a".
# Example:
#   Location: ds000201/sub-9001/ses-1/beh/sub-9001_ses-1_task-PVT_events.tsv
#   Reason: Missing value at column # 1
#   Line: 3 row 2: n/a 0.395

# Fix for errors 2 and 3: merge even and odd rows which were separated before
def fix_beh_tsv(dataset_dir):
    relative_path = 'sub-*/ses-*/beh/sub-*_task-PVT_events.tsv'
    beh_tsv_files = sorted(glob.glob(os.path.join(dataset_dir, relative_path)))
    for filename in beh_tsv_files[0:1]:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            headers = next(reader)
            reader_df = pd.DataFrame(reader)
            even = reader_df[reader_df.index % 2 == 0].reset_index(drop=True)
            odd = reader_df[reader_df.index % 2 == 1].reset_index(drop=True)
            new_df = pd.concat([even.iloc[:, :1], odd.iloc[:, 1:]], axis=1)
            new_df.columns = headers
            # Save the modified .tsv file
            new_df.to_csv(filename, sep='\t')
            # new_df.to_csv(filename[:-4] + '_bis.tsv', sep='\t')

## Error 4: [Code 90] SIDECAR_WITHOUT_DATAFILE
# A json sidecar file was found without a corresponding data file

# Error due to DataLad because I did not get the files yet?


## Error 5: [Code 129] SCANS_FILENAME_NOT_MATCH_DATASET
# The filename in scans.tsv file does not match what is present in the BIDS dataset.
# Fix: remove lines fieldmap, imaginary, real
def fix_scans_filename(dataset_dir):
    relative_path = 'sub-*/ses-*/sub-*_ses-*_scans.tsv'
    beh_tsv_files = sorted(glob.glob(os.path.join(dataset_dir, relative_path)))
    for filename in beh_tsv_files[0:1]:
        with open(filename, 'r') as file:
            df = pd.read_csv(filename, delimiter='\t')
            values_to_remove = ['fieldmap', 'imaginary', 'real']
            pattern = '|'.join(values_to_remove)
            new_df = df.loc[~df['filename'].str.contains(pattern, case=False)].reset_index(drop=True)
            # Save the modified .tsv file
            # new_df.to_csv(filename, sep='\t')
            new_df.to_csv(filename[:-4] + '_bis.tsv', sep='\t')


# Fix errors 2 and 3
# fix_beh_tsv(dataset_dir)

# Fix error 5
# fix_scans_filename(dataset_dir)