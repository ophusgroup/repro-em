---
title: Simulations
---

# Simulations

Luckily, we understand the physics of electron scattering very well. Therefore it is extremely common for researchers to simulate imaging and diffraction experiments. Spectroscopy simulations are less common though becoming more widespread, covering core loss EELS, plasmon and low loss EELS including phonons, and quantitative XEDS.

Simulations for 3D tomography and various 4DSTEM experiments such as nanobeam diffraction or ptychography are also very common.

The standard reference for the numerical methods is Kirkland's book ([Kirkland, Springer 2020](https://doi.org/10.1007/978-3-030-33260-0)).

## Codes

| Code | Reference | Notes |
|---|---|---|
| abTEM | [Madsen and Susi 2021](https://doi.org/10.12688/openreseurope.13015.2) | Python, open source, first-principles potentials |
| Prismatic | [Rangel DaCosta et al. 2021](https://doi.org/10.1016/j.micron.2021.103141) | C++ and Python, open source, GPU, PRISM algorithm |
| Dr. Probe | [Barthel 2018](https://doi.org/10.1016/j.ultramic.2018.06.003) | Free, closed source |
| MULTEM | [Lobato and Van Dyck 2015](https://doi.org/10.1016/j.ultramic.2015.04.016) | C++ with CUDA, open source, MATLAB interface |
| μSTEM | Allen, Findlay and co-workers | Fortran, includes inelastic and EELS |
| computem | [Kirkland 2020](https://doi.org/10.1007/978-3-030-33260-0) | C, the reference implementation from the book |

## Why this section belongs on this site

Simulations occupy an unusual position in the reproducibility argument, because they cut both ways.

They are a reliable source of ground truth. A simulated dataset has a known answer, which allows a reconstruction algorithm to be scored against truth rather than against another algorithm, and the benchmark suites this site argues for would largely be built on simulations. See [benchmarks](../framework/benchmarks.md).

They also contribute to the authenticity problem. We are good enough at this that a simulated micrograph with realistic noise, drift, and residual aberrations is difficult to distinguish from a measurement by eye, and that same capability defines the threat model. See [validated detectors](../framework/detectors.md).

## What a published simulation has to include

A simulation is fully determined by its inputs, so there is no excuse for one that cannot be repeated exactly. In practice, most published simulations cannot be, because the parameters that matter go unreported.

The minimum is the atomic structure file, the potential parameterization, the slice thickness, the real and reciprocal space sampling, the number and configuration of frozen phonons with the thermal displacement model, the full aberration set, the detector geometry, and the code with its version.

Sampling and slice thickness deserve specific mention because they are convergence parameters rather than physical ones, and an under-converged simulation produces a plausible wrong answer rather than an obvious failure. Reporting the convergence test takes a paragraph and removes the ambiguity.

A practical way to satisfy all of this is to publish the script. A simulation script with a pinned environment is a complete, executable specification, and it is usually shorter than the paragraph describing it.
