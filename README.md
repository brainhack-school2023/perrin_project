# BrainHack School 2023 Project

# Effects of Sleepiness on Resting-State Connectivity

# TODO: Insert image (brain or meme?)
 
## About Me
 
[Perrin Thomas](https://github.com/thomas-pr)

<a href="https://github.com/Thomas-Pr">
   <img src="https://avatars.githubusercontent.com/u/102051242?v=4?s=100" width="100px;" alt=""/>
   <br /><sub><b>Isaac Perrin</b></sub>
</a>
 
Hello! My name is Thomas Perrin, I am currently studying to obtain a double degree in biomedical engineering at Polytechnique Montreal. At IMT Atlantique, my home institution in France, I studied mostly medical devices and medical images analysis. Yet, exploring neuroimaging and open-source tools so in-depth is a new and inspiring part of my journey in biomedical engineering!


# Project Definition

## Background
Sleep deprivation is commonplace in modern society, but little is known about the functional mechanisms and correlates of sleepiness in the awake brain. Sleepiness is a brain state with pervasive effects on cognitive and affective functioning (Killgore, 2010, Tamm et al., 2020). Adult functional neuroimaging (fMRI) studies have demonstrated associations between restricted sleep and amygdala-prefrontal functional connectivity (Reidy et al., 2016), with inhibition of top-down-control in emotion (Tamm et al., 2020). Therefore, it would be interesting to explore and predict whether a participant is sleep deprived or not based on a functional connectivity estimation.

## Main Question
*Can resting-state functional connectivity predict sleep deprivation?*

## Data (TODO: Add link to the dataset)
* Data used: Resting-State fMRI from the Stockholm Sleepy Brain Study: Effects of Sleep Deprivation on Cognitive and Emotional Processing in Young and Old. A functional brain imaging study where 86 healthy participants underwent MRI after normal sleep and partial sleep deprivation (only 3 hours of sleep) in a crossover design. Three experiments were performed investigating emotional mimicry, empathy for pain, and cognitive reappraisal, as well as resting state fMRI.
* Fit with the research question: This study aimed to investigate the effects of partial sleep deprivation (PSD) on resting state brain connectivity, emotional contagion, empathy, and emotional regulation.
* Obtained from: OpenNeuro. The full dataset is multimodal (T1- and T2-weighted structural images, diffusion images, raw polysomnography data, task-based and resting state fMRI images). I will only use rs-fMRI data for my project.

## Tools & Methods
* Git and GitHub for project management
* DataLad for retrieval and version control of data
* BIDS-validator to check updated dataset integrity
* FMRIPrep for data preprocessing
* Python for visualization (and possibly neuroimaging machine learning) 

## Objectives
* Familiarize myself with neuroimaging data organization and open science
practices
* Learn reproductible neuroimaging workflow from preprocessing to data
visualization
* Visualize and compare functional connectomes of resting-state networks
* Prospect: Build a machine learning model


# Progress Overview: Retrace my Steps

## 1. OpenNeuro: Select the Dataset
* The data was already converted from DICOM to NIfTI
* TODO: Number of subjects, etc.
* BIDS organization except for a few errors

## 2. DataLad: Version Control the Dataset
* The DataLad Notebook
* Run the code to fix BIDS errors
* (Optional: Use containers for maximal reproducibility)

## 3. BIDS-Validation: Reproducible Neuroimaging Organization
* FAIR
* Prepared to use with tools like fMRIPrep

## 4. fMRIPrep: Preprocessing Pipeline for fMRI Data
* TODO

## 5. Python: Visualization of the data
* TODO: Add two cool brain pictures (comparison normal sleep vs. sleep-deprived) once I have them

## (6. NiLearn: Build a Machine Learning model)
* TODO if enough time

## 7. Git & GitHub: Version Control the Project
* Updated throughout the previous steps.


# Deliverables
* A GitHub repository containing all the elements of the project (the repository you are currently in!)
* A markdown file for the project description (the file you are currently reading!)
* DataLad and Python code for updating the dataset to BIDS
* Bash code for fMRI preprocessing
* A requirements.txt file to specify the Python environment
* Jupyter notebook for visualization (and machine learning)

## Organization of the Repository
- data: Raw data for the project, not synced to source control because the dataset is too large.
- docs: Documentation, including Markdown and reStructuredText (reST).
- results: Results, including checkpoints, hdf5 files, pickle files, as well as figures and tables.
- scripts: Scripts (Python, bash, .ipynb notebooks).
- src: Reusable Python modules for the project (imports).
- tests: Tests for the code.


# Conclusion?



# References
* Gustav Nilsonne and Sandra Tamm and Paolo d’Onofrio and Hanna Å Thuné and Johanna Schwarz and Catharina Lavebratt and Jia Jia Liu and Kristoffer NT Månsson and Tina Sundelin and John Axelsson and Peter Fransson and Göran Kecklund and Håkan Fischer and Mats Lekander and Torbjörn Åkerstedt (2020). The Stockholm Sleepy Brain Study: Effects of Sleep Deprivation on Cognitive and Emotional Processing in Young and Old. OpenNeuro. [Dataset] doi: 10.18112/openneuro.ds000201.v1.0.3
* Killgore WD. Effects of sleep deprivation on cognition. Prog Brain Res. 2010;185:105-29. doi: 10.1016/B978-0-444-53702-7.00007-5. PMID: 21075236.
* Reidy BL, Hamann S, Inman C, Johnson KC, Brennan PA. Decreased sleep duration is associated with increased fMRI responses to emotional faces in children. Neuropsychologia. 2016 Apr;84:54-62. doi: 10.1016/j.neuropsychologia.2016.01.028. Epub 2016 Jan 25. PMID: 26821063.
* Tamm S, Schwarz J, Thuné H, Kecklund G, Petrovic P, Åkerstedt T, Fischer H, Lekander M, Nilsonne G. A combined fMRI and EMG study of emotional contagion following partial sleep deprivation in young and older humans. Sci Rep. 2020 Oct 21;10(1):17944. doi: 10.1038/s41598-020-74489-9. PMID: 33087746; PMCID: PMC7578048.

