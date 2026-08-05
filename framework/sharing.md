---
title: Sharing data
---

# Sharing data

Archiving data and sharing data are different problems. An archive has to preserve the measurement; sharing has to get someone to look at it. A dataset that is deposited correctly and never opened has satisfied the letter of every data policy and accomplished nothing.

The gap is friction. If understanding a shared dataset requires installing a stack, learning a layout, and writing code before seeing a single image, almost no one will do it, and the data is public in name only.

## Interactive figures

The ideal sharing platform is an interactive HTML file, built from [anywidget](https://anywidget.dev/) or similar, that opens in a browser with nothing installed. It can show imaging data, 3D reconstructions, 3D ptychography, and spectrum images, with the reader free to change the virtual detector, move through a tilt series, rescale intensity, or pick a spectrum from a map.

This is a much better representation of a 4D-STEM dataset than any static figure, because the static figure is one choice out of thousands and the interactive one lets the reader make their own.

Metadata travels with the widget. Scale bars, microscope parameters, and dose belong in the interface itself, rather than in a caption sitting in a separate document.

Every such figure should link back to the raw data and to the code that produced it, so that a reader who wants to go past exploring can reproduce it. See [chain of custody](chain-of-custody.md).

## Streaming instead of downloading

Interactive exploration of a terabyte dataset does not require moving a terabyte. Chunked formats served over HTTP let a viewer fetch only the chunks currently on screen, which is exactly what Zarr was designed for. See [file formats](formats.md).

This changes what is practical to share. Full 4D-STEM datasets, complete tilt series, and whole *in situ* time series can be browsable from a link, with the reader downloading megabytes to look and the full archive still there for anyone who wants it.

## Where it lives

A shared figure needs the same durability as the paper. That means a persistent identifier, a stable host, and a stated retention commitment. A widget on a lab web server is a broken link in five years.
