---
title: Computational imaging
---

# Computational imaging

Almost every result published in this field has been computed. Even a "raw" micrograph has been gain corrected, dark subtracted, scaled, and cropped before anyone looks at it. There is no clean line between data and reconstruction, only a continuum of how much the answer depends on the algorithm.

That continuum is the reason computational imaging cannot be treated as a specialist topic. The question is not whether an experiment used computation. It is how far the published figure sits from the measurement, and whether the reader can retrace the distance.

## Simple

A cropped field of view. Rescaled intensity, corrected calibrations, a rotation, a bin. Operations that a reader would reproduce identically given the same input, and that change what the image shows without changing what it means.

These are still transformations, and they still belong in the record. A crop is a selection, and selection is where bias enters. See [plotting](plotting.md).

## Intermediate

An aligned time series. A drift-corrected image stack. Differential phase contrast. Denoising. Background subtraction and peak fitting in a spectrum.

Here the algorithm starts to matter. Two rigid-registration implementations will give different alignments on low-SNR data, DPC depends on the assumed detector geometry and scan rotation, and a sign error flips the field. The result is reproducible only if the method, its parameters, and the calibrations it consumed are all published.

## Complex

SPA cryo-EM, MicroED and 3DED, electron tomography, and ptychography.

These are inverse problems. We do not measure the object, we measure something the object produced, and we recover the object by iteratively adjusting a model until its predictions match the measurements. The reconstruction is a solution consistent with the data, and it is not unique. Different initializations, different regularization, and different stopping points give different answers, all of which fit the measurements to within noise.

This is what makes the complex end qualitatively different. A reader cannot judge the result by looking at it, because a wrong reconstruction and a right one are both smooth, plausible images. Validation has to be quantitative. See [benchmarks](benchmarks.md).

## What has to be published

For anything at the intermediate level or beyond:

**The forward model.** What physics was assumed. Multislice or a projection approximation, whether partial coherence was modeled, whether the probe was refined alongside the object, and what was held fixed.

**Regularization and priors.** Every constraint applied, including positivity, smoothness, sparsity, support constraints, and any learned prior. Regularization is what makes an underdetermined problem solvable, and it is also what puts features into a reconstruction that were never in the data.

**Hyperparameters.** Step sizes, iteration counts, batch sizes, regularization weights, and the stopping criterion. Stopping early is itself a regularizer and is rarely reported.

**Initialization.** The starting object and probe, and the random seed. See [analysis](analysis.md).

**The runnable record.** Ideally a container that takes the archived raw data and produces the published reconstruction, so a reader can verify rather than reimplement.

## Linking back to the source

A tomogram or a ptychographic phase image is a derived product, and it should be published with a resolvable link to the data it came from and the code that made it. Deposited without that link, it is a picture. With it, it is a measurement someone else can check.
