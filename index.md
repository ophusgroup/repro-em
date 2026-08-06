---
title: repro-EM
site:
  hide_outline: true
  hide_title_block: true
---

# Open Formats, Standard Metadata, and Benchmarks

A reproducibility framework for materials electron microscopy.

Electron microscopy of materials is an unusually heterogeneous field. We study metals, ceramics, polymers, nanoparticles, 2D materials, and semiconductors, using imaging, diffraction, spectroscopy, tomography, and *in situ* methods, and we record everything from 2D images to 5D momentum-resolved spectrum images. Almost every experiment asks a different question, because what we usually want to measure is where the average structure breaks: a dopant atom, a dislocation core, an interface, or a phase front moving under an applied field.

That heterogeneity is why our field has no equivalent of the Protein Data Bank, and it is the objection raised whenever standardization is proposed. How can a field this diverse do reproducible science?

Other fields have already answered this, and they did not do it by making everyone perform the same experiment. Structural biology and crystallography converged on deposition tied to publication, validation computed by someone other than the author, and metrics that the whole community agrees to report. None of those mechanisms assumes a shared measurement, and all of them are available to us now.

Four things follow. We must adopt open, self-describing file formats with a versioned layout specification. We must record a minimal metadata package at acquisition, including the calibrations, because a measurement whose calibration is unknown is not a measurement. We must define benchmarks for reconstruction validity, which for inverse problems means cross-validation against held-out measurements. And we must be able to trace a published figure back to signed detector output, since in the age of generative AI, authenticity has become part of validation.

None of this requires new technology. It requires that we agree to ask for it.
