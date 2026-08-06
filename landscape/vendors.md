---
title: Vendors
---

# Vendors

Instrument and detector manufacturers occupy the most consequential position in this landscape, because they determine what the rest of us can do. They control the file formats our data is written in, the metadata the instrument records, the degree of programmatic access we have, and whether the detector can attest to its own output.

The evidence for that control is visible in what our software can and cannot do. Every proprietary format in common use can be read and not written, because support exists only through reverse engineering by volunteers. Every open format can be both. See [file formats](../framework/formats.md).

That asymmetry has practical consequences beyond inconvenience. Reverse-engineered support is unversioned and unwarranted, so when a vendor changes a format in a software update, files silently stop opening and the fix arrives whenever someone has time to work it out. A field cannot build an archive on formats that behave this way.

The position is also improving in places. Some detector manufacturers now write HDF5-based containers, several expose scripting interfaces, and the pressure from 4D-STEM data volumes has forced more openness than existed a decade ago. The remaining requests are specific rather than sweeping: a published format specification, complete metadata written at acquisition, full programmatic control, and hardware signing of detector output. See [calls to action](../calls-to-action.md).

None of these are research problems. Camera manufacturers have already deployed hardware signing across their professional lines, so the question for EM vendors is whether their customers ask for it. See [validated detectors](../framework/detectors.md).
