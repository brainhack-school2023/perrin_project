# Dataset setup

Create a dataset
```
datalad create -c yoda --dataset preprocess
```

Copy the fix script to code (inside the data directory)
```
cp ../scripts/bids_fix.py preprocess/code/bids_fix.py
```

Enter the dataset
```
cd preprocess
```

Save the fix script move
```
datalad save -m "Copy BIDS fix script in code"
```

Obtain the dataset (rename to be more intuitively comprehensible)
```
datalad clone git@github.com:OpenNeuroDatasets/ds000201.git input/
```
or (no GitHub account)
```
datalad clone https://github.com/OpenNeuroDatasets/ds000201.git
```
or (Datalad superdataset)
```
datalad clone ///openneuro/ds000201
```

Save changes to datalad dataset
```
datalad save -m "Clone dataset from OpenNeuro"
```

Summary of total content present locally
```
datalad status --annex all
```

# Fix BIDS errors

Run script to fix BIDS errors (execute inside of preprocess directory)
```
datalad run -m "Fix BIDS errors in original dataset" \
-o "task-*_bold.json" \
-o "sub-*/ses-*/beh/sub-*_task-PVT_events.tsv" \
-o "sub-*/ses-*/sub-*_ses-*_scans.tsv" \
python3 code/bids_fix.py
```

# Preprocessing with fMRIPrep

Download data only for first subject (execute inside of input directory)cd 
```
datalad get sub-9001/ses-*/anat/* \
sub-9001/ses-*/fmap/* \
sub-9001/ses-*/func/*-rest_* \
```

Activate fmrprep on NeuroDesk
```
ml fmriprep
```

Run preprocessing
```
datalad run fmriprep input/ output/ participant \
--participant-label 9001 --task-id rest \
--skip-bids-validation --fs-license-file --low-mem
```
