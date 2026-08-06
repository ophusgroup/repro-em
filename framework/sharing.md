---
title: Sharing data
---

# Sharing data

Archiving data and sharing data are related but distinct problems, in that an archive has to preserve the measurement while sharing has to make someone likely to look at it. A dataset that is deposited correctly and never opened satisfies the letter of every data policy without accomplishing very much.

The difference between the two is largely a matter of friction. If understanding a shared dataset requires installing a software stack, learning an undocumented layout, and writing code before a single image can be seen, then very few readers will attempt it and the data is public only in name.

## Interactive figures

The ideal sharing platform is an interactive HTML file, built from [anywidget](https://anywidget.dev/) or similar, that opens in a browser with nothing installed. It can show imaging data, 3D reconstructions, 3D ptychography, and spectrum images, with the reader free to change the virtual detector, move through a tilt series, rescale intensity, or pick a spectrum from a map.

This is a much better representation of a 4D-STEM dataset than any static figure, because the static figure is one choice out of thousands and the interactive one lets the reader make their own.

Metadata travels with the widget. Scale bars, microscope parameters, and dose belong in the interface itself, rather than in a caption sitting in a separate document.

Every such figure should link back to the raw data and to the code that produced it, so that a reader who wants to go past exploring can reproduce it. See [chain of custody](chain-of-custody.md).

## Streaming instead of downloading

Interactive exploration of a terabyte dataset does not require moving a terabyte. Chunked formats served over HTTP let a viewer fetch only the chunks currently on screen, which is exactly what Zarr was designed for. See [file formats](formats.md).

This changes what is practical to share. Full 4D-STEM datasets, complete tilt series, and whole *in situ* time series can be browsable from a link, with the reader downloading megabytes to look and the full archive still there for anyone who wants it.

## Tutorials and companion sites

For method developers, an example dataset paired with a runnable tutorial does more for adoption than any amount of documentation, because it removes the step where a new user has to assemble a working example themselves. The [quantEM tutorials](https://github.com/electronmicroscopy/quantem-tutorials) are one example of this pattern.

The same applies to individual papers. A companion website built from GitHub Pages costs very little to produce, and it gives readers somewhere to reach the data, the code, the tutorials, and the interactive figures without going through a publisher. This site is itself an example, and large language models have made assembling one considerably faster.

## Journals are beginning to catch up

Interactive publication no longer has to sit outside the literature. [Elemental Microscopy](https://elementalmicroscopy.org), published by the Microscopy Society of America, is a free web-first journal of reviews and tutorials in which articles carry live figures and runnable code rather than static images, built on open source scientific publishing tooling.

:::{figure} ../assets/screenshots/elemental-microscopy.png
:alt: An article listing in Elemental Microscopy, showing a microscopy figure beside the article title and authors
:class: rpe-shot

An article in Elemental Microscopy. Figures in this journal are live rather than static, and the articles carry the code that produced them.
:::

This matters for the argument on this page because it removes the excuse that interactive work has nowhere to go. A reader can now be given an article in which the figure they are looking at is generated from the deposited data, in the journal itself, rather than in a supplement or on a lab server that will disappear.

## Where it lives

A shared figure needs the same durability as the paper. That means a persistent identifier, a stable host, and a stated retention commitment. A widget on a lab web server is a broken link in five years.
