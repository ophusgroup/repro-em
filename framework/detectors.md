---
title: Validated detectors
---

# Validated detectors

For better or worse, generative AI is here to stay. As discussed in [simulations](../materials-tem/simulations.md), the research community is incredibly good at simulating TEM data. With careful application of experimental artifacts and potentially using gen-AI tools, virtually any TEM or STEM experiment could be convincingly faked today.

This has been tested. Our own community ran the experiment and found that researchers identified real images 63% of the time and generated images 78% of the time, but that accuracy fell to 50% once the two were mixed together ([Zecca et al., *Microsc. Microanal.* 2023](https://doi.org/10.1093/micmic/ozad093)). Mixed data is what a reviewer actually encounters, so chance performance is the number that matters. A separate survey of over 250 scientists reached the same conclusion across six modalities ([Davydiuk et al., *Nat. Nanotechnol.* 2025](https://doi.org/10.1038/s41565-025-02009-9)).

And this is not including more subtle forms of fraud such as mislabeling samples, changing scalebars, rescaling spectroscopy axes, duplicating a region between figures, or choosing the one field of view out of two hundred that shows the expected result. In biomedical publications, 3.8% of over 20,000 papers screened contained problematic image duplication ([Bik et al., *mBio* 2016](https://doi.org/10.1128/mBio.00809-16)). No comparable screen has been run on materials microscopy.

What can we do to prevent fraud in TEM research, and more generally any experimental science?

## Cryptographic signatures

### Why watermarking will not work

Watermarking hides a signal inside the data itself, either in the low-order bits of each pixel or as a pattern in the frequency domain, so that the data carries a mark identifying where it came from.

This runs into three problems with TEM data. It modifies the measurement, and perturbing the low-order bits of a counted image corrupts the Poisson statistics that quantitative analysis depends on. It does not survive normal handling, since cropping, binning, drift correction, and denoising all destroy an embedded mark. And it only marks images from a cooperating generator, so with our simulation codes open source, it cannot be enforced on the images we would most want to identify.

More fundamentally, watermarking tries to demonstrate that an image is synthetic, which is a hard position to hold: any detector for synthetic images becomes a training signal for the next generation of models.

### Signing the real thing instead

The workable approach is the opposite: prove that an image is real, by anchoring it to the hardware that recorded it.

The building blocks are familiar from software distribution. A cryptographic hash such as SHA-256 reduces a file to a short fingerprint, where changing a single bit changes the fingerprint completely. A hash proves integrity while saying nothing about origin, which is what a signature adds.

Each detector would carry a secure element holding a private key that never leaves the chip, and would sign a block containing the hash of the raw frames together with the acquisition metadata. Anyone can verify that signature against the manufacturer's published public key. Signing data and metadata jointly is the detail that matters: if the two can be separated, the signature protects the pixels while the calibration, dose, and sample identity remain free to drift.

A verified signature establishes that this exact byte sequence came from a specific detector, on a specific date, under recorded operating conditions, and has not changed since.

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
