---
title: Analysis code for the paper "RF shimming in the cervical spinal cord at 7T"

tags:
  - RF shimming
  - spinal cord
  - MRI
  - high field
  - 7T
authors:
  - name: Daniel Papp
    orcid: 0000-0003-1481-1413
    affiliation: 1
  - name: Kyle M. Gilbert
    orcid: 0000-0003-3026-5686
    affiliation: "2, 3"
  - name: Gaspard Cereza
    affiliation: 1
  - name: Alexandre D’Astous
    orcid: 0000-0003-0381-7334
    affiliation: 1
  - name: Nibardo Lopez-Rios
    orcid: 0000-0002-4791-8260
    affiliation: 1
  - name: Mathieu Boudreau
    orcid: 0000-0002-7726-4456
    affiliation: 1
  - name: Marcus Couch
    orcid: 0000-0002-2732-8941
    affiliation: 4
  - name: Pedram Yazdanbakhsh
    orcid: 0000-0003-4456-5997
    affiliation: 5
  - name: Robert L. Barry
    affiliation: "6, 7, 8"
  - name: Eva Alonso Ortiz
    orcid: 0000-0001-6590-7234
    affiliation: 1
  - name: Julien Cohen-Adad
    orcid: 0000-0003-3662-9532
    affiliation: "1, 9, 10"
affiliations:
 - name: NeuroPoly Lab, Institute of Biomedical Engineering, Polytechnique Montreal, Montreal, QC, Canada
   index: 1
 - name: Centre for Functional and Metabolic Mapping, The University of Western Ontario, London, ON, Canada
   index: 2
 - name: Department of Medical Biophysics, The University of Western Ontario, London, ON, Canada
   index: 3
 - name: Siemens Healthcare Limited, Montreal, QC, Canada
   index: 4
 - name: McConnell Brain Imaging Centre, Montreal Neurological Institute, McGill University, Montreal, QC, Canada
   index: 5
 - name: Athinoula A. Martinos Center for Biomedical Imaging, Department of Radiology, Massachusetts General Hospital, Charlestown, MA, USA
   index: 6
 - name: Harvard Medical School, Boston, MA, USA
   index: 7
 - name: Harvard-Massachusetts Institute of Technology Health Sciences and Technology, Cambridge, MA, USA
   index: 8
 - name: Mila - Quebec AI Institute, Montreal, QC, Canada
   index: 9
 - name: Functional Neuroimaging Unit, Centre de recherche de l'Institut universitaire de gériatrie de Montréal QC, Canada
   index: 10

date: 9 February 2024
bibliography: paper.bib

---

# Summary

Data was collected from five participants between two 7T sites with a custom 8Tx/20Rx parallel transmission (pTx) coil. We explored two RF shimming approaches from an MRI vendor and four from an open-source toolbox, showcasing their ability to enhance transmit field and signal homogeneity along the cervical spinal cord.

The results indicate significant improvements in B1+ efficiency and cerebrospinal fluid / spinal cord signal ratio across various RF shimming conditions compared to the vendor based methods.

The study's findings highlight the potential of RF shimming to advance 7T MRI's clinical utility for central nervous system imaging by enabling more homogenous and efficient spinal cord imaging. Additionally, the research incorporates a reproducible Jupyter Notebook, enhancing the study's transparency and facilitating peer verification. By also making the data openly accessible on OpenNeuro, we ensure that the scientific community can further explore, validate, and build upon our findings, contributing to the collective advancement in high-resolution imaging techniques.

![Overview of the RF shimming procedure. The top panel shows the RF coil used for the experiments, alongside the Tx coil geometry and the electromagnetic simulation results (on Gustav model) yielding the CP mode used for this coil. The bottom panel shows the RF shimming procedure (with approximate duration). First, GRE and tfl_rfmap scans are acquired (4min30s). Second, these images are transferred via ethernet socket from the MRI console onto a separate laptop running Shimming Toolbox and SCT (<1s). Third, the spinal cord is automatically segmented to produce a mask that is resampled into the space of the individual coil magnitude and phase images of the tfl_rfmap scan (~5s). Fourth, the RF shim weights are calculated according to the defined constraints for each shim scenario (1min total).
\label{fig:overview}](featured.png)

# Statement of need

Advancing the development of 7T MRI for spinal cord imaging is crucial for the enhanced diagnosis and monitoring of various neurodegenerative diseases [@Kearney2015-py] and traumas [@David2019-jy]. However, a significant challenge at this field strength is the transmit field inhomogeneity . Such inhomogeneity is particularly problematic for imaging the small, deep anatomical structures of[@Ibrahim2001-xt;@Collins2005-za;@Roschmann1987-om;@Yang2002-ui] the cervical spinal cord, as it can cause uneven signal intensity and elevate the local specific absorption ratio, compromising image quality. This multi-site study explores several radiofrequency (RF) shimming techniques in the cervical spinal cord at 7T.

# 1. Data

The data can be downloaded from: https://openneuro.org/datasets/ds004906

The structure of the input dataset is as follows (JSON sidecars are not listed for clarity):

```{toggle}
~~~
ds004906
├── CHANGES
├── README
├── dataset_description.json
├── participants.json
├── participants.tsv
├── sub-01
│   ├── anat
│   │   ├── sub-01_acq-CP_T1w.nii.gz
│   │   ├── sub-01_acq-CP_T2starw.nii.gz
│   │   ├── sub-01_acq-CoV_T1w.nii.gz
│   │   ├── sub-01_acq-CoV_T2starw.nii.gz
│   │   ├── sub-01_acq-SAReff_T2starw.nii.gz
│   │   ├── sub-01_acq-patient_T2starw.nii.gz
│   │   ├── sub-01_acq-phase_T2starw.nii.gz
│   │   ├── sub-01_acq-target_T2starw.nii.gz
│   │   ├── sub-01_acq-volume_T2starw.nii.gz
│   └── fmap
│       ├── sub-01_acq-anatCP_TB1TFL.nii.gz
│       ├── sub-01_acq-anatCoV_TB1TFL.nii.gz
│       ├── sub-01_acq-anatSAReff_TB1TFL.nii.gz
│       ├── sub-01_acq-anatpatient_TB1TFL.nii.gz
│       ├── sub-01_acq-anatphase_TB1TFL.nii.gz
│       ├── sub-01_acq-anattarget_TB1TFL.nii.gz
│       ├── sub-01_acq-anatvolume_TB1TFL.nii.gz
│       ├── sub-01_acq-fampCP_TB1TFL.nii.gz
│       ├── sub-01_acq-fampCoV_TB1TFL.nii.gz
│       ├── sub-01_acq-fampSAReff_TB1TFL.nii.gz
│       ├── sub-01_acq-famppatient_TB1TFL.nii.gz
│       ├── sub-01_acq-fampphase_TB1TFL.nii.gz
│       ├── sub-01_acq-famptarget_TB1TFL.nii.gz
│       └── sub-01_acq-fampvolume_TB1TFL.nii.gz
├── sub-02
├── sub-03
├── sub-04
└── sub-05
~~~
```

# 2. Overview of processing pipeline

During the data acquisition stage, RF shimming was done using the [Shimming Toolbox](https://github.com/shimming-toolbox/shimming-toolbox) {cite:p}`DAstous2023` during the acquisition stage.

The post-processing pipeline uses the [Spinal Cord Toolbox](https://spinalcordtoolbox.com) {cite:p}`DeLeener201724`.

For each subject:

- Process anat/T2starw (GRE)
  - Segment the spinal cord (SC)
  - Label vertebral levels using existing manual disc labels
  - Create a mask of the cerebrospinal fluid (CSF)
  - Extract the SC/CSF magnitude signal to assess the stability of the flip angle across shim methods
- Process fmap/TFL (flip angle maps)
  - Register each B1 map (CP, CoV, etc.) to the GRE scan
  - Apply the computed warping field to bring the segmentation and vertebral levels to the B1 map
  - Convert the B1 map to nT/V units
  - Extract the B1 map value within the SC

>Slow processes are indicated with the emoji ⏳

# 3. Requirements

* Install [Spinal Cord Toolbox](https://spinalcordtoolbox.com/user_section/installation.html) {cite:p}`DeLeener201724`, eg

```shell
# Install SCT ⏳
!git clone --depth 1 https://github.com/spinalcordtoolbox/spinalcordtoolbox.git
!yes | spinalcordtoolbox/install_sct
os.environ['PATH'] += f":/content/spinalcordtoolbox/bin"
```

* Download the project repository

```shell
git clone https://github.com/shimming-toolbox/rf-shimming-7t.git
cd rf-shimming-7t
git checkout main
```

* Install requirements

```shell
pip install -r binder/requirements.txt
```

* Download data

```shell
cd content
repo2data -r ../binder/data_requirement.json
```

# 4. Environment setup

In a Python shell, import the necessary modules and define variables.

# 5. Process anat/T2starw (GRE)

Run segmentation on GRE scan.

Copy CSF masks from the derivatives folder.

For more details about how these masks were created, see: [https://github.com/shimming-toolbox/rf-shimming-7t/issues/67](https://github.com/shimming-toolbox/rf-shimming-7t/issues/67).

Crop GRE scan for faster processing and better registration results.

Label vertebrae on GRE scan.

Register *_T2starw to CoV_T2starw.

Extract the signal intensity on the GRE scan within the spinal cord between levels C3 and T2 (included), which correspond to the region where RF shimming was prescribed.

Prepare data for figure  of CSF/SC signal ratio from T2starw scan.

Perform statistics.

# 6. Process fmap/TFL (flip angle maps)

Register TFL flip angle maps to the GRE scan.

Warping spinal cord segmentation and vertebral level to each flip angle map.

Convert the flip angle maps to B1+ efficiency maps [nT/V] (inspired by code from Kyle Gilbert).

The approach consists in calculating the B1+ efficiency using a 1ms, pi-pulse at the acquisition voltage, then scale the efficiency by the ratio of the measured flip angle to the requested flip angle in the pulse sequence.

Extract B1+ value along the spinal cord between levels C3 and T2 (included).

Prepare data for figure of B1+ values along the spinal cord across shim methods.

Perform statistics.

# 7. Paper figures

Prepare RF shimming mask for figure.

Create figure of B1+ maps.

![B1+ efficiency for one participant (sub-05) across all seven RF shimming conditions. The top left panel shows the tfl_b1map magnitude image with an overlay of the mask that was used to perform RF shimming. Text inserts show the mean (in nT/V) and CoV (in %) of B1+ efficiency along the spinal cord between C3 and T2.
\label{fig:fig2}](fig2_b1plus_map.png)


![B1+ efficiency (A) and CSF/Cord signal ratio from the GRE scan (B) across subjects and across different RF shimming conditions. Data were measured in the spinal cord from C3 to T2 vertebral levels. To match the x-ticks across subjects, the C2-C3 and the T2-T3 intervertebral discs of each subject were aligned with that of the PAM50 template [@DELEENER2018170], and the curves were linearly scaled.
\label{fig:fig3}](fig3_plotly.png)


# Acknowledgements

Funded by the Canada Research Chair in Quantitative Magnetic Resonance Imaging [950-230815], the Canadian Institute of Health Research [CIHR FDN-143263], the Canada Foundation for Innovation [32454, 34824], the Fonds de Recherche du Québec - Santé [28826], the Natural Sciences and Engineering Research Council of Canada [RGPIN-2019-07244], the Canada First Research Excellence Fund (IVADO and TransMedTech), the Courtois NeuroMod project and the Quebec BioImaging Network [5886, 35450], and MITACS Accelerate Fellowship.


## References

