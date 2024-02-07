# rf-shimming-7t

[![DOI Badge](https://img.shields.io/badge/DOI-10.18112%2Fopenneuro.ds004906-blue)](https://openneuro.org/datasets/ds004906)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shimming-toolbox/rf-shimming-7t/blob/mb/neurolibre/data_processing.ipynb)
[![Open in MyBinder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/shimming-toolbox/rf-shimming-7t/mb/neurolibre?labpath=content%2Findex.ipynb)

Reproducible Notebook for the paper "RF shimming in the cervical spinal cord at 7T"

## Run with Google Colab

Click on the badge "Open in Colab" ☝️. The notebook takes about 2 hours to run on Google Colab (without a paid subscription that gives access to more powerful resource).

## Run on a BinderHub (eg. NeuroLibre, Mybinder) or with repo2binder 

Click on the badge "Open in MyBinder" ☝️. This environment setup downloads the data and the output of notebook previously run on Google Colab, and by default the notebook will only run the analysis cells (i.e. not the SCT-related commands).

If you'd like to re-run the processing from scratch, change the `notebook = 'neurolibre-figures'` line in the first cell to `notebook = 'neurolibre-clean'`. This will delete the processed files and then re-run the entire processing pipeline. Note that some cells take a lot of RAM, and may fail on certain systems.

## Run locally with Jupyter Notebook

Install [Spinal Cord Toolbox](https://spinalcordtoolbox.com/user_section/installation.html)

Clone this repository
~~~
git clone https://github.com/shimming-toolbox/rf-shimming-7t.git
git checkout mb/neurolibre
cd rf-shimming-7t
~~~

Install Python dependencies (assuming Python is already installed)
~~~
pip install -r binder/requirements.txt
~~~

Download data
~~~
cd content
repo2data -r ../binder/data_requirement.json
~~~


Run notebook
~~~
jupyter notebook index.ipynb
~~~

