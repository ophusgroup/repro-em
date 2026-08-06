---
title: Samples
---

# Samples

Sample preparation is frequently the least well documented part of a TEM experiment, and it often has a large effect on whether a result can be reproduced. Two groups running the same instrument at the same settings can disagree substantially because one prepared the specimen by FIB lift-out and the other by crushing.

## Hard matter

Alloys, ceramics and oxides, semiconductors, catalysts, 2D materials, and quantum materials.

These are usually the most beam-stable samples, so we can afford long dwell times, focal series, tilt series, and repeated measurement of the same region. That stability is what makes them the natural starting point for a reproducibility framework. A measurement that cannot be repeated on a stable oxide will not be repeatable on anything.

Preparation matters more than it is usually credited. FIB lift-out introduces gallium implantation, amorphous surface damage, and thickness variation along the lamella. Crushed powders give clean surfaces but uncontrolled orientations and thicknesses. Electropolishing and ion milling each leave their own artifacts. Sample thickness in particular is required to interpret almost any quantitative measurement, and is frequently neither measured nor reported.

## Soft matter

Organic molecules, macromolecules and polymers, solid electrolytes, halide perovskites, and metal-organic frameworks.

Experiments on this class of materials are often defined by their minor or extreme sensitivity to the electron beam. The measurement changes the sample while it is being made, so total dose and dose rate are not optional metadata. A HAADF image of a halide perovskite at 10 e⁻/Å² and the same image at 1000 e⁻/Å² are measurements of two different materials.

Dose limits also force the low-SNR regime, and low SNR is where denoising and reconstruction choices begin to determine the result. This is exactly where held-out validation earns its keep.

 See [benchmarks](../framework/benchmarks.md).

## Liquids

Samples in water or other solvents, ionic liquids, and liquid electrolytes, usually in a sealed cell or a graphene liquid cell.

Liquid samples are even more likely to be modified by interaction with the electron beam. Radiolysis generates radicals and gas bubbles, shifts local pH, and can drive the nucleation and growth we are trying to observe. The required metadata expands to include cell geometry, window material and thickness, liquid path length, flow rate, and applied potential.

Liquid and *in situ* experiments are among the harder cases for reproducibility, because the specimen is a system evolving in time rather than a fixed structure. The full time series is the measurement, and publishing one extracted frame discards it.
