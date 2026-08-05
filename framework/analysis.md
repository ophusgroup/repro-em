---
title: Analysis
---

# Analysis

Software MUST be open source. If a reader cannot read the code that produced a number, they cannot check the number, and the result is a claim rather than a measurement. This is not a preference about licensing. It is the difference between a result that can be verified and one that has to be believed.

The same rule applies to machine learning. A trained model is part of the analysis, so training data, training code, and weights must all be open. A network whose weights are published without its training set is still a black box, because its failure modes cannot be predicted or tested.

## Software versions and environments

An analysis is defined by its code and by everything the code was standing on. Numerical results move between library versions, and results that depend on the GPU or the thread count are more common than most of us would like.

Publish the pinned environment, not a list of package names. A lock file, a conda environment export, or a container image are all acceptable. A `requirements.txt` with unpinned versions is not, because it will resolve differently in a year and silently produce different numbers.

Containers are the strongest option available today, and they are what the abstract asks for: a complete runnable record that a reader can execute without reconstructing anyone's laptop.

## Parameters and random seeds

Every parameter that affects the output has to be recorded, including the ones chosen by hand at the terminal and never written down. In practice this means the analysis should be driven by a configuration file that is published with the result, so there is no gap between what was run and what was reported.

Stochastic methods need their seeds. Reconstruction algorithms with random initialization, stochastic gradient methods, dropout, and Monte Carlo sampling all give different answers on re-runs. Publishing the seed makes a run exactly repeatable.

Repeatability is the floor, not the goal. If the result changes meaningfully when the seed changes, the seed is not the fix. Report the spread across seeds, and treat the variation as an uncertainty on the result.

## Notebooks and scripts

Notebooks are excellent for communicating an analysis and poor at guaranteeing it. Cells can be run out of order, and the stored output can come from code that no longer exists in the file.

Publish notebooks with their outputs cleared and a test that runs them top to bottom. If a notebook does not produce the published figure on a clean run, it does not document the analysis.

For anything that takes more than a few minutes, move the computation into a script or module with the notebook calling it. This makes the analysis testable, keeps it out of the presentation layer, and lets the expensive part run somewhere other than a laptop.
