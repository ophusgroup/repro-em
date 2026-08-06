---
title: Metadata
---

# Metadata

Without metadata, a dataset is only an array of numbers, and the test that a metadata package has to pass is a practical one. A researcher outside the original group, given the file and nothing else, should be able to determine what was measured, what the axes mean in physical units, and what dose the sample received. Very few materials TEM datasets currently in circulation would pass this test.

## The minimal package

Minimal means the fields you cannot interpret the array without. Everything else is desirable, and desirable fields do not get enforced.

| Field | Example |
|---|---|
| Modality | `4D-STEM` |
| Accelerating voltage | `300 kV` |
| Instrument | `Thermo Fisher Spectra 300`, probe corrected, lab instrument ID |
| Axis order and units | `(scan_y, scan_x, k_y, k_x)`, explicit, no convention assumed |
| Real-space sampling | `0.24 Å` per scan step |
| Reciprocal sampling | `0.82 mrad` per detector pixel |
| Convergence semi-angle | `25.1 mrad` |
| Collection angles | inner and outer, per detector, in mrad |
| Dose | fluence in e⁻/Å² and dose rate in e⁻/Å²/s |
| Sample | identifier resolving to a preparation record |
| Acquisition | date, operator, institution |
| Writer | software name and version that produced the file |

Each of these twelve fields is known to the instrument or the operator at acquisition time, and each is routinely lost before publication.

## Modality and acquisition parameters

Beyond the minimal package, each modality has a small set of parameters that determine what the numbers mean.

**Imaging.** Defocus and the measured aberration coefficients, with the method and date of the aberration measurement. Nominal magnification, dwell or exposure time, binning, scan shape and step size, scan rotation, and flyback time.

**Diffraction and 4D-STEM.** Camera length as calibrated rather than as labelled, DP center in detector pixels, detector orientation relative to the scan frame, and whether the detector ran in counting or integrating mode. For precession, the precession angle and frequency.

**Spectroscopy.** For EELS, the dispersion in eV per channel, the zero-loss position, the collection semi-angle, the spectrometer entrance aperture, and the energy resolution as measured from the zero-loss peak. For XEDS, the detector solid angle and take-off angle, the elevation and azimuth, and the quantification model with its k-factors or cross sections.

**Tomography and time series.** The tilt or time value of every frame, in acquisition order, along with whatever stimulus was applied. A tilt series stored without its per-frame angles is not recoverable.

## Required calibrations

This is where reproducibility usually fails, and it fails quietly.

A nominal value read off the instrument is not a calibration. Nominal magnification can be several percent from truth, nominal camera length worse, and both drift with lens history. Strain measured to 0.1% from a diffraction pattern calibrated to 3% is a number with no meaning.

### An example: the scan rotation

4D-STEM files do not record the rotation between the scan coordinate system and the diffraction coordinate system. This is a single angle, set by the lens excitations and therefore dependent on camera length and lens history, and it relates directions in real space to directions in reciprocal space.

It is known at the microscope, and no widely used format writes it. Every group that needs it recovers it afterwards from the data itself, typically by rotating until the curl of the measured field is minimized. That procedure has a 180° ambiguity, resolved by deciding whether curl or divergence should vanish, and choosing wrong reverses the sign of the result.

The consequence is the failure mode that matters most for reproducibility. Without the scan rotation, DPC vectors point in the wrong direction, strain axes are rotated, and orientation maps are wrong, and none of this announces itself. The analysis runs to completion and produces a confident answer.

This is also exactly the kind of thing an automated validation service would catch, in the same way that checkCIF catches inconsistent crystallographic data. See [learning from crystallography](../crystallography.md).

Every calibration should carry four things: the value, the method used to obtain it, an uncertainty, and the date it was performed.

| Calibration | Why it is required |
|---|---|
| Real-space pixel size | Every length, spacing, and area in the paper |
| Reciprocal pixel size | Every scattering angle, *d*-spacing, and strain value |
| Scan rotation | Relative orientation of scan and detector frames; sign errors flip DPC and strain maps |
| DP center | Center of mass, DPC, radial integration, and virtual detector placement |
| Detector gain and dark reference | Any quantitative intensity, including thickness from ADF |
| Counts to electrons | Dose, SNR, and Poisson noise models |
| EELS dispersion and zero loss | Every energy in the spectrum |
| Scan distortion and drift | Real-space accuracy at atomic resolution |

## Provenance: sample, instrument, operator

Provenance is what lets a reader trace a number back to a physical object and a moment in time.

**Sample.** Composition, source or synthesis route, and preparation method with its parameters. FIB thinning, ion milling, electropolishing, and drop casting each leave signatures in the data, and a reader who does not know which was used cannot separate artifact from result.

**Instrument.** Make, model, and the specific machine, since two instruments of the same model do not behave identically. Corrector state, holder type, and any non-standard optics such as a monochromator, phase plate, or aperture.

**Operator and session.** Who recorded the data, when, and under what session identifier. Session identity matters more than it sounds: it is what groups a dataset with the reference images, the calibration measurements, and the control sample recorded alongside it. Those companions are usually the only evidence that a measurement was sound, and they are almost always discarded.

