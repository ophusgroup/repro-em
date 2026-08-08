---
title: Sharing data
---

# Sharing data

Archiving data and sharing data are related but distinct problems, in that an archive has to preserve the measurement while sharing has to make someone likely to look at it. A dataset that is deposited correctly and never opened satisfies the letter of every data policy without accomplishing very much.

The difference between the two is largely a matter of friction. If understanding a shared dataset requires installing a software stack, learning an undocumented layout, and writing code before a single image can be seen, then very few readers will attempt it and the data is public only in name.

## Interactive figures

The ideal sharing platform is an interactive HTML file, built from [anywidget](https://anywidget.dev/) or similar, that opens in a browser with nothing installed. The reader can change the virtual detector, move through a tilt series, rescale intensity, or pick a spectrum from a map. This represents a 4D-STEM dataset far better than any static figure, which is one choice out of thousands.

Metadata should travel with the widget, so scale bars, microscope parameters, and dose belong in the interface rather than in a caption elsewhere. Every such figure should link back to the raw data and the code that produced it. See [chain of custody](chain-of-custody.md).

## Streaming instead of downloading

Interactive exploration of a terabyte dataset does not require moving a terabyte. Chunked formats served over HTTP let a viewer fetch only the chunks currently on screen, which is exactly what Zarr was designed for. See [file formats](formats.md).

This changes what is practical to share. Full 4D-STEM datasets, complete tilt series, and whole *in situ* time series can be browsable from a link, with the reader downloading megabytes to look and the full archive still there for anyone who wants it.

## Tutorials and companion sites

For method developers, an example dataset paired with a runnable tutorial does more for adoption than any amount of documentation, because it removes the step where a new user has to assemble a working example. The [quantEM tutorials](https://github.com/electronmicroscopy/quantem-tutorials) follow this pattern.

The same applies to papers. A companion website built from GitHub Pages costs very little and gives readers somewhere to reach the data, code, tutorials, and interactive figures without going through a publisher. This site is itself an example.

## Journals are beginning to catch up

Interactive publication no longer has to sit outside the literature. [Elemental Microscopy](https://elementalmicroscopy.org), published by the Microscopy Society of America, is a free web-first journal whose articles carry live figures and runnable code rather than static images.

:::{figure} ../assets/screenshots/elemental-microscopy.png
:alt: An article listing in Elemental Microscopy, showing a microscopy figure beside the article title and authors
:class: rpe-shot

An article in Elemental Microscopy. Figures in this journal are live rather than static, and the articles carry the code that produced them.
:::

This removes the excuse that interactive work has nowhere to go. A figure can now be generated from the deposited data inside the article itself, rather than in a supplement or on a lab server that will disappear.

## Where it lives

A shared figure needs the same durability as the paper. That means a persistent identifier, a stable host, and a stated retention commitment. A widget on a lab web server is a broken link in five years.
