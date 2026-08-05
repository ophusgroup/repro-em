---
title: Methods
---

# Methods

Materials science TEM studies can be broadly separated into TEM and STEM.

In TEM, a broad and nearly parallel beam illuminates the sample, and the objective lens forms an image of the whole illuminated region at once. Every pixel is recorded in parallel, so acquisition is fast and the dose rate is low. Contrast comes from interference of the exit wave, and the transfer of that wave into the recorded image is described by the CTF of the objective lens. The standard reference is the Williams and Carter textbook ([Williams and Carter, Springer 2009](https://doi.org/10.1007/978-0-387-76501-3)).

In STEM, the same lens focuses the beam into a small probe, which is scanned across the sample. Each probe position is measured in series, and the image is built up pixel by pixel from detectors placed below the sample. Because each position produces a full scattering distribution, many channels can be recorded from a single scan: several annular detectors, a spectrometer, and a pixelated camera can all run at once ([Ophus, *Annu. Rev. Mater. Res.* 2023](https://doi.org/10.1146/annurev-matsci-080921-092646)).

Both modes are limited by the aberrations of the objective lens. Hardware correctors now routinely remove spherical and non-round aberrations in TEM ([Haider et al., *Nature* 1998](https://doi.org/10.1038/33823)) and STEM ([Krivanek et al., *Ultramicroscopy* 1999](https://doi.org/10.1016/S0304-3991(99)00013-3)). This pushed resolution below 1 Å, and it also added a large set of tunable optical parameters. A corrected instrument cannot be described by voltage and magnification alone, which matters for everything that follows.

## Imaging

There are many different kinds of imaging data in TEM. In the plane-wave illumination mode, we can record images containing only phase contrast (sometimes called HRTEM), or use an aperture to select the unscattered wave (bright field) or a subset of the scattered waves (dark field). We can also record diffraction patterns, typically selected area diffraction (SAD) where we use an aperture to illuminate a small portion of the sample.

In STEM, we can also use a variety of different detectors. A BF-STEM image integrates the entire unscattered beam, while an ABF-STEM image uses a donut shaped detector to record the outer edge of the unscattered beam. An ADF-STEM image records part of the scattered electron beam, and can be further divided into low-angle, medium-angle, and high-angle ADF (LAADF, MAADF, and HAADF).

STEM imaging also includes multipixel detectors. These could be combined BF / ADF detectors, or segmented rings such as those used in DPC imaging.

We can also record more exotic data channels. In EBIC, the sample is a working device with electrical contacts, and we measure the current the beam generates in it at each probe position, which maps junctions and recombination at active defects. In CL we collect the light emitted by the sample, either as a panchromatic intensity or as a full spectrum per pixel. We can also detect secondary and backscattered electrons for surface and composition contrast, and in a biased or heated holder the sample's electrical response is recorded as a channel alongside the image.

Researchers often will record a sequence of images. These can be for statistical reasons, or to stitch together many individual micrographs into a larger whole. Sometimes they will change microscope parameters, for example a focal series of HRTEM or STEM, or simply a time series while a stimulus such as heating or biasing is applied to the sample. These time series experiments are referred to as *in situ* or *operando* experiments.

## Diffraction

Diffraction measurements record the distribution of scattering angles rather than an image. In TEM this is SAD, NBED, or PED. In STEM, recording a full DP at every probe position gives 4D-STEM, a four-dimensional array of two scan dimensions and two detector dimensions.

4D-STEM deserves separate mention because it subsumes most of the detector geometries above. Any annular detector can be synthesized from the data after the fact, along with DPC, iDPC, strain maps, orientation maps, and ptychographic phase reconstruction. The physical detector is replaced by a choice made in software, which is the shift that makes recording analysis parameters as important as recording instrument settings.

## Spectroscopy

EELS measures the energy lost by transmitted electrons, giving composition, bonding, oxidation state, and with a monochromator, phonon and optical response. XEDS measures characteristic X-rays for elemental composition. Both are usually acquired as spectrum images, one spectrum per scan position.

Spectroscopic data carries its own calibration burden. An EELS dataset without the dispersion and the zero-loss reference is not interpretable, and an XEDS map without the detector geometry and the quantification model behind it is a picture rather than a measurement.

## Tomography

Tilt series reconstruct 3D structure from projections taken over a range of sample orientations. In materials TEM this covers ADF-STEM tomography, atomic electron tomography, spectroscopic tomography, and increasingly 3D ptychography.

Every tomogram is the output of an inverse problem, and the reconstruction is at least as consequential as the acquisition. See [computational imaging](../framework/computational-imaging.md).
