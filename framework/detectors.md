---
title: Validated detectors
---

# Validated detectors

For better or worse, generative AI is here to stay. As discussed in (link to simulation page), the research community is incredibly good at simulating TEM data. With careful application of experimental artifacts and potentially using gen-AI tools, virtually any TEM or STEM experiment could be convincingly faked today.

And this is not including more subtle forms of fraud such as mislabeling samples, changing scalebars, scaling spectroscopy axes (more examples)!

What can we do to prevent fraud in TEM research, and more generally any experimental science?


## Cryptographic Signatures

-explain how hidden watermarks or data watermarks work.
-explain why that won't work for TEM data.

-explain how software packages are validated with a hash code.
-each manufacturer could use a hardware chip to digitically sign each recorded image or spectra. Then any researcher could verify that a given image was:
-recorded on a specific detector
-recorded on a specific day
-recorded at a specific location
-anything else we need - potentially even by a specific person?  Or the microscope in a given operating condition, "burning in" the metadata to the raw data file?




