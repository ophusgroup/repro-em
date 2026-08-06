---
title: 3DED
---

# 3DED

3DED is the same measurement as MicroED, made by a different community with different vocabulary. Where MicroED came from structural biology, 3DED grew out of the materials and chemical crystallography side, and is applied to zeolites, MOFs, minerals, pharmaceuticals, and inorganic phases.

The naming is correspondingly fragmented, and the same experiment appears as 3DED, continuous rotation electron diffraction, electron diffraction tomography, automated diffraction tomography, and precession-assisted variants, depending on the group and the decade. Structures usually go to the CSD or the COD rather than the PDB.

That fragmentation is itself worth noting. One physical measurement acquired at least five names and two deposition venues, purely because two communities developed it in parallel. Materials TEM has the same problem across most of its modalities, and it is a reproducibility problem rather than a cosmetic one, because a reader searching for comparable measurements cannot find them.

## Dynamical scattering

3DED has one complication that X-ray crystallography does not. Electrons scatter strongly, so the kinematical approximation that relates measured intensity to structure factor is only approximately true. Dynamical refinement improves accuracy substantially and can determine absolute configuration, and it also makes the path from frames to structure considerably more model-dependent.

This is precisely the case where archiving raw frames matters most. When the reduction is model-dependent, the reduced intensities are a result rather than a measurement, and depositing only the reduced data hides the step most likely to be wrong.

## Software

Data reduction with XDS, DIALS, or PETS2. Structure solution with SHELXT, refinement with SHELXL, and Olex2, SIR, or Superflip in common use. Automated pipelines now chain acquisition, reduction, and solution together for real-time structure determination at the microscope.

Being able to name the standard tools for a technique in three sentences is an achievement most of materials TEM cannot match.
