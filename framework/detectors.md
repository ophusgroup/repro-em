---
title: Validated detectors
---

# Validated detectors

For better or worse, generative AI is here to stay. As discussed in [simulations](../materials-tem/simulations.md), the research community is incredibly good at simulating TEM data. With careful application of experimental artifacts and potentially using gen-AI tools, virtually any TEM or STEM experiment could be convincingly faked today.

This is not hypothetical. A commercial image generator trained on authentic microscopy data produced convincing fakes across six modalities including TEM and STEM, and in a survey of over 250 scientists, respondents told real from generated images at roughly chance ([Davydiuk et al., *Nat. Nanotechnol.* 2025](https://doi.org/10.1038/s41565-025-02009-9)).

And this is not including more subtle forms of fraud such as mislabeling samples, changing scalebars, rescaling spectroscopy axes, duplicating a region within or between figures, subtracting a background until a peak appears, or simply choosing the one field of view out of two hundred that shows the expected result. In biomedical publications, 3.8% of over 20,000 papers screened contained problematic image duplication, and around half of those showed signs of deliberate manipulation ([Bik et al., *mBio* 2016](https://doi.org/10.1128/mBio.00809-16)). There is no reason to think microscopy in materials science is cleaner. We have simply never looked.

What can we do to prevent fraud in TEM research, and more generally any experimental science?

## Cryptographic signatures

### Why watermarking will not work

Watermarking hides a signal inside the data itself, either in the low-order bits of each pixel or as a pattern in the frequency domain, so that the data carries a mark identifying where it came from.

This fails for TEM data on several counts. It modifies the measurement, and we need the counts to be exactly what the detector recorded, because perturbing the low-order bits of a counted image corrupts the Poisson statistics that quantitative analysis depends on. It does not survive normal handling, since cropping, binning, drift correction, and denoising are all legitimate operations that destroy an embedded mark. And most fundamentally, watermarking only marks images made by a cooperating generator. Our best simulation codes are open source, which is a strength of this field, and it means no watermark can ever be enforced on the fakes we actually need to worry about.

Watermarking tries to prove an image is fake. That contest cannot be won, because every detector for synthetic images is a training signal for the next generator.

### Signing the real thing instead

The workable approach is the opposite: prove that an image is real, by anchoring it to the hardware that recorded it.

The building block is already familiar from software distribution. A cryptographic hash such as SHA-256 reduces a file to a short fingerprint. Changing a single bit anywhere changes the fingerprint completely, and no one can construct a different file with the same one. This is why a package manager can verify that the code you downloaded is the code the author released.

A hash alone proves integrity, and says nothing about origin. Origin needs a signature. Each detector would carry a secure element holding a private key that never leaves the chip, and would sign a block containing the hash of the raw frames together with the acquisition metadata. Anyone can verify that signature against the manufacturer's published public key.

Signing data and metadata together is the important detail, and it is what "burning in" the metadata really requires. If the two can be separated, the signature protects the pixels while the calibration, dose, and sample identity remain free to drift.

A verified signature would establish that this exact byte sequence came from a specific detector, on a specific date, under a specific set of recorded operating conditions, and has not changed since. Institutional registration of instrument serial numbers extends this to location and laboratory. Binding to a specific person is weaker and probably belongs at the session level rather than in hardware, since operator identity is an institutional fact rather than a physical one.

### What signing does and does not buy

A signature anchors the start of the chain and nothing more. It cannot tell you that a sample is what the authors say it is, and it will not stop anyone from recording a genuine image of a mislabeled specimen. Provenance of the sample stays a human responsibility. See [metadata](metadata.md).

What it does buy is an unforgeable starting point, from which every processing step can sign its own output together with the hashes of its inputs. The result is a chain that can be walked from a published figure back to the detector. Fabricating an image gets easier every year. Fabricating a complete signed chain does not. See [chain of custody](chain-of-custody.md).

### What we should ask vendors for

- A secure element in the detector, with published public keys and a documented key rotation policy
- Signatures over the raw data and the acquisition metadata jointly
- Signatures preserved through format conversion, by signing the payload and carrying the signature alongside it
- An open, documented verification tool that does not require the vendor's software to run
- Trusted timestamps from an independent authority, so the acquisition date does not rest on the instrument's own clock

None of this is novel engineering. Secure elements are in every phone, and the standards for signing and timestamping are decades old. What is missing is the requirement. See [calls to action](../calls-to-action.md).
