---
title: SPA cryo-EM
---

# SPA cryo-EM

Single particle analysis (SPA) determines a 3D density map by averaging over many copies of the same object, each imaged in an unknown orientation. It is worth describing in some detail here, because it is the electron microscopy modality where deposition, validation, and raw data archiving have all become routine parts of publication.

## The experiment

The sample is vitrified on a grid, cooled quickly enough that the surrounding water forms amorphous ice rather than crystals. Grids are then screened, and usable regions are imaged by automated collection over a period of hours or days.

Dose is the constraint that shapes the rest of the experiment. Each particle can absorb only a few tens of electrons per square Ångström before the structure of interest is destroyed, so individual images are dominated by noise and the structure appears only after averaging over many thousands of particles. Each exposure is recorded as a movie rather than a single frame, which allows beam-induced motion to be corrected afterwards. A single session typically produces thousands of micrographs, from which millions of individual particle images can be extracted.

## The computational pipeline

The processing chain is longer than in most materials TEM work, and it typically proceeds as follows. Motion correction aligns the frames within each movie. CTF estimation fits the defocus and astigmatism of each micrograph. Particles are picked, extracted, and sorted by 2D classification, which removes damaged or incorrectly picked images. An initial model is then generated, 3D classification separates distinct conformational or compositional states, and refinement improves the particle orientations and the map together. Post-processing applies masking and sharpening, and an atomic model is built into the resulting density.

Each of these steps has parameters that change the result, which is the reason a deposited map on its own is not sufficient to check the work.

## Software

The tools below are a non-exhaustive list of what is in common use. Most of the pipeline is covered by open source software, and both the stage and the license are given because the licensing varies.

| Stage | Tool | Reference | License |
|---|---|---|---|
| Motion correction | MotionCor2 | [Zheng et al. 2017](https://doi.org/10.1038/nmeth.4193) | Free for academic use |
| Motion correction, preprocessing | [Warp](https://github.com/warpem/warp) | [Tegunov and Cramer 2019](https://doi.org/10.1038/s41592-019-0580-y) | Open source |
| CTF estimation | CTFFIND4 | [Rohou and Grigorieff 2015](https://doi.org/10.1016/j.jsb.2015.08.008) | Open source |
| Particle picking | [Topaz](https://github.com/tbepler/topaz) | [Bepler et al. 2019](https://doi.org/10.1038/s41592-019-0575-8) | Open source |
| Full pipeline | [RELION](https://github.com/3dem/relion) | [Scheres 2012](https://doi.org/10.1016/j.jsb.2012.09.006) | Open source, GPL |
| Full pipeline | [cryoSPARC](https://cryosparc.com/) | [Punjani et al. 2017](https://doi.org/10.1038/nmeth.4169) | Free for academic use, closed source |
| Full pipeline | [cisTEM](https://cistem.org/) | [Grant et al. 2018](https://doi.org/10.7554/eLife.35383) | Open source |
| Full pipeline | [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2) | [Tang et al. 2007](https://doi.org/10.1016/j.jsb.2006.05.009) | Open source |
| Workflow integration | [Scipion](https://scipion.i2pc.es/) | [de la Rosa-Trevín et al. 2016](https://doi.org/10.1016/j.jsb.2016.04.010) | Open source |
| Tomography, general | IMOD | [Kremer et al. 1996](https://doi.org/10.1006/jsbi.1996.0013) | Open source |
| Conformational heterogeneity | [cryoDRGN](https://github.com/ml-struct-bio/cryodrgn) | [Zhong et al. 2021](https://doi.org/10.1038/s41592-020-01049-4) | Open source |

Two points are relevant to the arguments made elsewhere on this site. First, nearly every stage of this pipeline has a capable open source implementation, and Scipion allows tools from different packages to be combined within a single recorded workflow. Second, cryoSPARC is very widely used and its source code cannot be inspected, so even a field that has largely solved deposition and validation still has a closed step in the middle of many published pipelines. See [analysis and plotting](../framework/analysis.md).

The methods for handling conformational heterogeneity are also worth noting for materials science. Rather than sorting particles into a small number of discrete classes, cryoDRGN learns a continuous distribution of conformations using a neural network, which is closer to the kind of structural variation we usually encounter in materials.

## Validation

Resolution is measured by the FSC between two reconstructions, each refined from one half of the data. The two halves are separated at the start and kept independent throughout refinement, so neither reconstruction can borrow information from the other and the correlation between them cannot be inflated by overfitting. Resolution is reported at the point where the correlation falls to 0.143, a threshold introduced by [Rosenthal and Henderson (2003)](https://doi.org/10.1016/j.jmb.2003.07.013), and the independent-halves protocol was formalized by [Scheres and Chen (2012)](https://doi.org/10.1038/nmeth.2115).

An important feature of this arrangement is that the metric is produced by the refinement procedure itself rather than applied as a separate check afterwards, so an author cannot omit it without changing how the reconstruction was run. Beyond the single global number, local resolution estimates describe how reliability varies across the map, and map-model FSC tests whether the built atomic model agrees with the density.

## Deposition

Three archives divide the work between them. The EMDB holds 3D maps, the PDB holds fitted atomic coordinates, and EMPIAR holds raw movies and intermediate data. Deposition to the EMDB and PDB is required for publication, while deposition to EMPIAR remains voluntary.

Since February 2022, depositing half-maps has been mandatory for single particle entries, and they must be unfiltered, unmasked, and unsharpened. This requirement is worth adopting elsewhere, because the archive asks not only for the result but for the specific intermediate products that allow the validation to be recomputed independently. The wwPDB then generates a validation report during biocuration, covering the map and, where a model is present, the agreement between map and model, and that report remains attached to the entry for reviewers and readers.

## File formats

| Product | Format | Notes |
|---|---|---|
| Movies and micrographs | MRC, TIFF, EER | EER is a compressed event representation written by the detector |
| Maps and half-maps | MRC, CCP4 | Long-established open specification |
| Atomic models | mmCIF, PDBx | Dictionary-defined, inherited from crystallography |
| Processing metadata | STAR | Tagged text, also inherited from crystallography |

Both the model format and the metadata format were adopted from crystallography rather than designed from scratch, which is part of why they were adopted quickly. See [learning from crystallography](../crystallography.md).

## What transfers to materials TEM

Four elements of this system could be applied to materials TEM without assuming a single experiment type: a validation metric computed from deposited data by someone other than the author, a requirement to deposit the intermediate products that make that computation possible, a separate archive for raw data so that reprocessing with later methods remains possible, and deposition tied to publication, which is what gives the other three any practical force.

The gap to note is that EMPIAR deposition is voluntary, so the raw movies behind most published maps were never archived. See [data](../framework/data.md).

