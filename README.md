# rf-shimming-7t

[![DOI Badge](https://img.shields.io/badge/DOI-10.18112%2Fopenneuro.ds004906-blue)](https://openneuro.org/datasets/ds004906)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shimming-toolbox/rf-shimming-7t/blob/mb/neurolibre/data_processing.ipynb)
[![launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/shimming-toolbox/rf-shimming-7t/mb/neurolibre?labpath=content%2Findex.ipynb)

Reproducible Notebook for the paper "RF shimming in the cervical spinal cord at 7T"

## Run with Google Colab

Click on the badge "Open in Colab" ☝️. The notebook takes about 2 hours to run on Google Colab (without a paid subscription that gives access to more powerful resource).

## Run in a Docker container (NeuroLibre, MyBinder, repo2ocker)

### NeuroLibre

> [!NOTE]
> This repo isn't on NeuroLibre's whitelist yet, to cannot access it's binderhub until reviewed/published there.


### MyBinder

> [!NOTE]
> MyBinder sometimes crashes during Docker build. NeuroLibre servers are preferred.

Click on the badge "launch binder" ☝️. This environment setup downloads the data and the output of notebook previously run on Google Colab, and by default the notebook will only run the analysis cells (i.e. not the SCT-related commands).

If you'd like to re-run the processing from scratch, change the `notebook = 'neurolibre-figures'` line in the first cell to `notebook = 'neurolibre-clean'`. This will delete the processed files and then re-run the entire processing pipeline. Note that some cells take a lot of RAM, and may fail on certain systems.

### repo2docker

To run locally on your computer, you must first have Docker installed, running, and have created an account. Follow the instructions [here](https://www.docker.com/get-started/).

Then, you need to install [repo2docker](https://github.com/jupyterhub/repo2docker). Install via pip: `pip install jupyter-repo2docker`

To launch a Docker session from this repo, run `repo2docker --ref mb/neurolibre https://www.github.com/shimming-toolbox/rf-shimming-7t`. After it's completed, it will provie you with a weblink, copy and open this link in a browser to open the Jupyter Notebook session.

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

