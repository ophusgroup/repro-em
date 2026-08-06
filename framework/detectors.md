---
title: Validated detectors
---

# Validated detectors

For better or worse, generative AI is here to stay. As discussed in [simulations](../materials-tem/simulations.md), the research community is incredibly good at simulating TEM data. With careful application of experimental artifacts and potentially using gen-AI tools, virtually any TEM or STEM experiment could be convincingly faked today.

This has already been demonstrated in practice. A commercial image generator trained on authentic microscopy data produced convincing fakes across six modalities including TEM and STEM, and in a survey of over 250 scientists, respondents told real from generated images at roughly chance ([Davydiuk et al., *Nat. Nanotechnol.* 2025](https://doi.org/10.1038/s41565-025-02009-9)).

Our own community has run the same test on itself. In a study published in *Microscopy and Microanalysis*, researchers correctly identified real images 63% of the time and generated images 78% of the time, but that accuracy fell to 50% once real and generated images were mixed together ([Zecca et al., *Microsc. Microanal.* 2023](https://doi.org/10.1093/micmic/ozad093)). Performance at chance on mixed data is the relevant number, because mixed data is what a reader or a reviewer actually encounters.

And this is not including more subtle forms of fraud such as mislabeling samples, changing scalebars, rescaling spectroscopy axes, duplicating a region within or between figures, subtracting a background until a peak appears, or simply choosing the one field of view out of two hundred that shows the expected result. In biomedical publications, 3.8% of over 20,000 papers screened contained problematic image duplication, and around half of those showed signs of deliberate manipulation ([Bik et al., *mBio* 2016](https://doi.org/10.1128/mBio.00809-16)). No comparable screen has been run on materials microscopy, so we have no reason to assume our literature is any cleaner.

What can we do to prevent fraud in TEM research, and more generally any experimental science?

## Cryptographic signatures

### Why watermarking will not work

Watermarking hides a signal inside the data itself, either in the low-order bits of each pixel or as a pattern in the frequency domain, so that the data carries a mark identifying where it came from.

This approach runs into several problems with TEM data. It modifies the measurement, and we generally need the recorded counts to be exactly what the detector produced, since perturbing the low-order bits of a counted image corrupts the Poisson statistics that quantitative analysis depends on. An embedded mark also does not survive normal handling, because cropping, binning, drift correction, and denoising are all legitimate operations that destroy it. Watermarking additionally marks only those images produced by a cooperating generator, and since the widely used simulation codes are open source, a watermark cannot be enforced on the images we would most want to identify.

Watermarking is in general an attempt to demonstrate that an image is synthetic, which is a difficult position to hold over time, because any detector for synthetic images can be used as a training signal for the next generation of models.

### Signing the real thing instead

The workable approach is the opposite: prove that an image is real, by anchoring it to the hardware that recorded it.

The building block is already familiar from software distribution. A cryptographic hash such as SHA-256 reduces a file to a short fingerprint. Changing a single bit anywhere changes the fingerprint completely, and no one can construct a different file with the same one. This is why a package manager can verify that the code you downloaded is the code the author released.

A hash alone proves integrity while saying nothing about origin, which is what a signature adds. Each detector would carry a secure element holding a private key that never leaves the chip, and would sign a block containing the hash of the raw frames together with the acquisition metadata. Anyone can verify that signature against the manufacturer's published public key.

Signing data and metadata together is the important detail, and it is what "burning in" the metadata really requires. If the two can be separated, the signature protects the pixels while the calibration, dose, and sample identity remain free to drift.

A verified signature would establish that this exact byte sequence came from a specific detector, on a specific date, under a specific set of recorded operating conditions, and has not changed since. Institutional registration of instrument serial numbers extends this to location and laboratory. Binding to a specific person is weaker and probably belongs at the session level rather than in hardware, since operator identity is an institutional fact rather than a physical one.

### What signing does and does not buy

A signature anchors the start of the chain and does no more than that. It cannot establish that a sample is what the authors say it is, and it will not prevent anyone from recording a genuine image of a mislabeled specimen, so the provenance of the sample itself remains a human responsibility. See [metadata](metadata.md).

What signing does provide is a starting point that cannot be forged, from which each processing step can sign its own output together with the hashes of its inputs, producing a chain that can be followed from a published figure back to the detector. Producing a convincing individual image is becoming steadily easier, while producing a complete and internally consistent signed chain requires compromising the hardware itself. See [chain of custody](chain-of-custody.md).

### What we should ask vendors for

- A secure element in the detector, with published public keys and a documented key rotation policy
- Signatures over the raw data and the acquisition metadata jointly
- Signatures preserved through format conversion, by signing the payload and carrying the signature alongside it
- An open, documented verification tool that does not require the vendor's software to run
- Trusted timestamps from an independent authority, so the acquisition date does not rest on the instrument's own clock

None of this requires novel engineering, since secure elements are already present in consumer hardware and the standards for signing and timestamping have been in use for decades. We want to encourage detector manufacturers to implement hardware signing, and journals and funding agencies to expect it, so that authenticity can be checked rather than assumed. See [calls to action](../calls-to-action.md).
