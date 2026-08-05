---
title: MicroED
---

# MicroED

MicroED determines structures from crystals far too small for X-ray diffraction, by collecting electron diffraction while continuously rotating the crystal in a cryo-cooled TEM ([Shi et al., *eLife* 2013](https://doi.org/10.7554/eLife.01345)).

The name comes from the group that introduced it, and it is used mostly for macromolecular and pharmaceutical samples. Structures are deposited in the PDB, which now handles MicroED explicitly through OneDep, collecting the entry under the macromolecular crystallography framework with added metadata describing electron diffraction collection and processing.

## Why it is relevant here

MicroED is a materials-adjacent technique that acquired publication-enforced deposition standards, and it did so by adopting an existing framework rather than building a new one. It inherited the format, the validation, and the archive from crystallography, and the community accepted them because they already existed and already worked.

This is the cheapest path to a standard, and it is available to more of materials TEM than we usually admit. Any modality whose output is a structure or a reduced intensity set can plug into machinery that has been running for thirty years.

## Where it stops short

The deposited entry is a model, plus reduced intensities. The diffraction movies are not required, and are usually not archived. Anyone wanting to test whether a different reduction or a dynamical refinement changes the answer generally cannot, because the frames are gone.

See [3DED](3ded.md) and [where raw data goes](../crystallography.md).
