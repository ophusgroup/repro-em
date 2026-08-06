---
title: Cryo-tomography
---

# Cryo-tomography

Cryo-electron tomography reconstructs 3D volumes from tilt series of vitrified specimens, and where the specimen contains many copies of the same object, subtomogram averaging recovers a higher resolution structure from them.

It is worth a separate page because it is the one case in this comparison that archives the raw measurement rather than stopping at the result.

## Deposit, validate, enforce

Subtomogram averages are deposited in the EMDB, and the raw tilt series go to EMPIAR. Validation follows the same logic as single particle work, with FSC computed between independently refined halves, and half-maps have been mandatory for subtomogram averaging entries since February 2022. Deposition carries the same accession code requirement that journals enforce for any other structure.

## Why the upstream archive matters

EMPIAR holds raw and intermediate data rather than finished results, which changes what the community can do with a published dataset ([Iudin et al., 2023](https://doi.org/10.1093/nar/gkac1062)). Methods developed years after acquisition can be tested against real data, competing reconstructions of the same tilt series can be compared directly, and a disputed result can be re-examined rather than argued about.

The CryoET Data Portal extends this further by providing standardized annotations alongside the deposited data, so that a new method can be benchmarked without each group first reproducing the annotation work ([Ermel et al., *Nat. Methods* 2024](https://doi.org/10.1038/s41592-024-02477-2)).

## What transfers to materials TEM

Materials tomography has the same structure as this problem and almost none of the infrastructure. A tilt series is a raw measurement, the tomogram is a model-dependent reconstruction of it, and the reconstruction is where most of the interpretation happens.

Two practices are worth adopting directly. Archive the tilt series rather than only the tomogram, since the reconstruction can always be redone from the projections and never recovered from the volume. And validate by splitting the projections, reconstructing from each half, and comparing, which is the tomographic form of the cross-validation this site argues for. See [benchmarks](../framework/benchmarks.md).
