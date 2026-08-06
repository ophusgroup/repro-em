---
title: File formats
---

# File formats

## Recommendations

**Zarr 3.0, written as a zipstore.** One file or many can be written into a single `.zip` package, it handles arbitrary datatypes and very large arrays performantly, and metadata travels in the same container as the data.

Zarr earns the primary recommendation because of how it reads. Chunks are independent objects, so a reader can pull one scan region out of a terabyte dataset over HTTP without downloading the rest. This is what makes browsable published data practical, and it is why cloud and HPC workflows have converged on it. See [sharing data](sharing.md).

**HDF5 as the secondary recommendation.** Widely adopted, well supported in every language we use, and an excellent single-file archival container. Its weakness is concurrent and remote access, where the single-file design that makes it good for archiving works against it.

Both are open, self-describing, N-dimensional array containers with chunking and compression, which is the actual requirement. Either is enormously better than what most of us publish today.

Choosing a container is only part of the problem. A Zarr file with undocumented axis order and no calibrations is as unreadable as a proprietary one, so the format recommendation only means something alongside a layout specification and a metadata schema. See [data](data.md) and [metadata](metadata.md).

One implementation of this approach is the `AutoSerialize` mechanism in [quantEM](https://github.com/electronmicroscopy/quantem), which writes arbitrary classes and data types into a single compressed Zarr `.zip` file, lets the user choose which objects and datasets are included, and is fast enough to sit inside a machine learning workflow.

## Common TEM file types

Drawn from the formats supported by [RosettaSciIO](https://hyperspy.org/rosettasciio/supported_formats/index.html), the reader underneath HyperSpy and much of the Python EM ecosystem.

| Format | Extension | Origin | Open | Read | Write |
|---|---|---|---|---|---|
| Gatan DigitalMicrograph | `dm3`, `dm4` | Gatan | No | Yes | No |
| Velox | `emd` | Thermo Fisher | No | Yes | No |
| TIA | `emi`, `ser` | Thermo Fisher | No | Yes | No |
| Bruker composite | `bcf` | Bruker | No | Yes | No |
| JEOL | `asw`, `pts`, `img`, `map` | JEOL | No | Yes | No |
| Quantum Detectors Merlin | `mib` | Medipix | No | Yes | No |
| TVIPS | `tvips` | TVIPS | No | Yes | Yes |
| DENS | `dens`, `csv`, `log` | DENSsolutions | No | Yes | No |
| MRC | `mrc` | Community | Yes | Yes | No |
| MRCZ | `mrcz` | Community | Yes | Yes | Yes |
| TIFF | `tif` | Standard | Yes | Yes | Yes |
| NeXus | `nxs` | Standard | Yes | Yes | Yes |
| EMD (NCEM) | `emd` | Berkeley NCEM | Yes | Yes | Yes |
| HSpy | `hspy` | HyperSpy, on HDF5 | Yes | Yes | Yes |
| ZSpy | `zspy` | HyperSpy, on Zarr | Yes | Yes | Yes |

The read and write columns are worth comparing directly. **Every proprietary format in this table can be read and not written**, while every open format can be both.

That asymmetry follows directly from how the support was built. Vendor formats are readable because volunteers reverse-engineered them, and reverse engineering gets you far enough to read a file but not far enough to write one safely. It also means that support is unversioned and unwarranted: when a vendor changes their format in a software update, files silently stop opening, and the fix arrives whenever someone has time.

Two rows deserve specific attention. **Velox `emd` and NCEM `emd` are different formats with the same name and the same extension.** One is proprietary and one is open, both are built on HDF5, and neither is readable by software expecting the other, so a reader who downloads an `.emd` file cannot tell from the name what they have. This is the kind of collision that occurs when a community has no format governance.

## Simulation file types

Simulation outputs need the same treatment as experimental data, and mostly do not get it.

The Python codes are in reasonable shape. abTEM writes Zarr, and Prismatic writes HDF5, so both produce self-describing containers that carry their parameters. Most of the older and faster codes, including Dr. Probe, μSTEM, and Kirkland's computem, write custom binary arrays with a separate text parameter file. Those files are readable if you have the code and the parameter file, and are meaningless a few years later without both.

For simulations, the harder reproducibility problem lies upstream of the container. The input is a physics configuration with a large number of consequential parameters: the potential parameterization, slice thickness, real and reciprocal sampling, the frozen phonon configurations and their number, the thermal displacement model, the aberrations, and the detector geometry. Any of these can change the result substantially, and they are frequently reported as "multislice simulations were performed."

A published simulation should ship its complete input configuration in a form that regenerates the output. For the Python codes this is a script and a pinned environment. See [analysis](analysis.md) and [simulations](../materials-tem/simulations.md).
