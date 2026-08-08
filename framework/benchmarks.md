---
title: Benchmarks
---

# Benchmarks

There are only two ways to validate a computational pipeline.

The first is to test on data with known ground truth, either from simulations or from a sample with an independent measurement of the answer. This is the stronger test, and it is limited by how well the test case represents the real experiment. A reconstruction that recovers a simulated object perfectly may still fail on real data whose noise and artifacts the simulation did not contain.

The second, and the more practical, is cross-validation. Hold some of the measurements out of the reconstruction, then check whether the result predicts them. This requires no ground truth and works on every real dataset, which is why it is the one we should be asking for.

## Data quality metrics

SPA cryo-EM solved this. Resolution is measured by the FSC between reconstructions from two independently refined halves of the data, and a number computed this way cannot be inflated by overfitting.

The lesson is structural rather than technical. Cryo-EM did not converge on FSC because it is the perfect metric, but because the field agreed on one number, computed one way, reported with every deposition, so that any two results can be compared. Materials TEM has no such number for any of its modalities.

We should also report the inputs to data quality rather than only the outputs: dose and dose rate, detector DQE and MTF, the SNR achieved, and the calibration uncertainties that propagate into every derived quantity. See [metadata](metadata.md).

## Cross-validation for inverse problems

Cross-validation transfers directly to the reconstruction methods used in materials TEM.

Tomography can be validated by comparing two reconstructions, each using half of the tilt projections. Ptychography can be validated by holding out probe positions: reconstruct the object and probe from eight ninths of the measurements, then use the recovered object to predict the intensities at the remaining ninth. Given how hard ptychographic reconstructions are to converge, holding out a small fraction is more realistic than splitting in half.

The reconstruction can be run twice. Once with data held out, to establish error bars by cross-validation, and again with all of the data for the published result. Repeating with different held-out subsets gives a better estimate of the spread.

This is the check the abstract asks for, stated concretely: reconstruct from a subset of the measurements, and verify that the forward model predicts the remaining measurements within the expected noise.

## Held-out measurement tests

A held-out test measures the thing we actually care about, which is whether the reconstruction has learned the object or the noise.

Three requirements make it meaningful. The held-out measurements must be excluded from every stage, including probe refinement, alignment, and hyperparameter selection. The prediction must be compared against the expected noise, since agreement much better than Poisson indicates leakage rather than success. And the held-out fraction must be reported, because withholding 1% is not the same test as withholding a third.

Reporting a held-out error alongside every reconstruction costs one extra run and tells a reader more than any figure.

## Reference datasets

Shared benchmark data is what lets independent groups compare methods on equal terms.

Two kinds are needed. Simulated datasets with known ground truth, spanning a realistic range of dose, thickness, and aberrations, let a method be scored against truth. Experimental datasets on well-characterized samples, with an independent measurement of the answer, test whether that score survives contact with a real instrument.

There is a good precedent from a neighboring field. A comparison of 71 elemental crystals across 15 density functional theory codes established that modern implementations agree with each other to within the differences between high-precision experiments ([Lejaeghere et al., *Science* 2016](https://doi.org/10.1126/science.aad3000)). That study is why a DFT result today can be trusted to be a property of the physics rather than of the software.

No equivalent study exists for multislice simulation codes, for ptychographic reconstruction engines, or for strain mapping from 4D-STEM. We do not currently know whether two groups analyzing the same dataset with different software would agree, because nobody has checked.
