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
    orcid: 
    affiliation: 1
  - name: Kyle M. Gilbert
    orcid: 
    affiliation: "2, 3"
  - name: Gaspard Cereza
    orcid: 
    affiliation: 1
  - name: Alexandre D’Astous
    orcid: 
    affiliation: 1
  - name: Mathieu Boudreau
    orcid: 
    affiliation: 1
  - name: Marcus Couch
    orcid: 
    affiliation: 4
  - name: Pedram Yazdanbakhsh
    orcid: 
    affiliation: 5
  - name: Robert L. Barry
    orcid: 
    affiliation: "6, 7, 8"
  - name: Eva Alonso Ortiz
    orcid: 
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
 - name: Harvard-Massachusetts Institute of Technology Health Sciences & Technology, Cambridge, MA, USA
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


# Statement of need

Advancing the development of 7T MRI for spinal cord imaging is crucial for the enhanced diagnosis and monitoring of various neurodegenerative diseases [@Kearney2015-py] and traumas [@David2019-jy]. However, a significant challenge at this field strength is the transmit field inhomogeneity . Such inhomogeneity is particularly problematic for imaging the small, deep anatomical structures of[@Ibrahim2001-xt;@Collins2005-za;@Roschmann1987-om;@Yang2002-ui] the cervical spinal cord, as it can cause uneven signal intensity and elevate the local specific absorption ratio, compromising image quality. This multi-site study explores several radiofrequency (RF) shimming techniques in the cervical spinal cord at 7T.


# Figures

![Overview of the RF shimming procedure. The top panel shows the RF coil used for the experiments, alongside the Tx coil geometry and the electromagnetic simulation results (on Gustav model) yielding the CP mode used for this coil. The bottom panel shows the RF shimming procedure (with approximate duration). First, GRE and tfl_rfmap scans are acquired (4min30s). Second, these images are transferred via ethernet socket from the MRI console onto a separate laptop running Shimming Toolbox and SCT (<1s). Third, the spinal cord is automatically segmented to produce a mask that is resampled into the space of the individual coil magnitude and phase images of the tfl_rfmap scan (~5s). Fourth, the RF shim weights are calculated according to the defined constraints for each shim scenario (1min total)..
\label{fig:overview}](featured.png)


# Acknowledgements

Funded by the Canada Research Chair in Quantitative Magnetic Resonance Imaging [950-230815], the Canadian Institute of Health Research [CIHR FDN-143263], the Canada Foundation for Innovation [32454, 34824], the Fonds de Recherche du Québec - Santé [28826], the Natural Sciences and Engineering Research Council of Canada [RGPIN-2019-07244], the Canada First Research Excellence Fund (IVADO and TransMedTech), the Courtois NeuroMod project and the Quebec BioImaging Network [5886, 35450], and MITACS Accelerate Fellowship.


## References

