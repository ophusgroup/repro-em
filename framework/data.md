---
title: Data
---

# Data

The raw data recorded by the detector is the measurement itself, and everything else on this site concerns the path from that measurement to a published claim. It is therefore worth being precise about what we mean by raw data, and about what has to be stored alongside it.

## What counts as raw

Raw means the closest thing to the detector output that can be written to disk. For a counting detector this is the electron event list or the counted frames, before summing. For an integrating camera it is the frames before gain and dark correction, or if the instrument will not release those, the earliest product it will.

Every step past that point is a choice: binning, summing, gain correction, drift correction, cropping, and conversion to 8 or 16 bit. These are usually reasonable choices, and they are also irreversible. Published data should preserve whatever the instrument permitted, and state plainly where the raw record actually begins.

Raw data is immutable. Corrections, alignments, and calibrations are recorded as separate products that reference it, never written back over it.

## The layout specification

An N-dimensional array is ambiguous without a statement of what its dimensions are. A 4D-STEM dataset can appear as `(scan_y, scan_x, k_y, k_x)` or `(k_y, k_x, scan_y, scan_x)`, with either origin convention and either handedness, and nothing in the file distinguishes them. Groups routinely lose a day to a transposed or mirrored dataset, and sometimes publish one.

Each modality needs a versioned, documented layout specification giving the dimension order, the physical meaning and units of every axis, the origin convention, and the sign convention for angles and rotations. Versioned matters, because the specification will change and files written under the old one must remain readable.

## Size

Materials TEM now routinely produces datasets that are inconvenient to move. A 4D-STEM scan can reach hundreds of gigabytes, an *in situ* time series more, and a tomographic 4D-STEM experiment more again.

Three things make this tractable:

**Sparse and counted representations.** At low dose, most detector pixels are empty. Storing electron events rather than dense frames often gives an order of magnitude or more, with no loss.

**Chunked compression.** Both Zarr and HDF5 compress per chunk and read per chunk, so a reader can pull one scan region out of a terabyte file without downloading the rest. See [file formats](formats.md).

**Honesty about what was kept.** If the full raw dataset genuinely cannot be published, publish the reduced product, state exactly what reduction was applied, and preserve the raw with an identifier and a stated retention period. Size is a real constraint, and it argues for publishing a documented reduction rather than for publishing nothing.
