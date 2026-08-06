---
title: Learning from crystallography
---

# Learning from crystallography

Crystallography is another useful example for our purposes, and one that is usually overlooked in favor of the structural biology archives. It addressed validation as well as deposition, and it did so several decades ago, using machinery that does not assume a single experiment type.

## What crystallography standardized

Four components were standardized, in an order worth noting. A file format that carries data and metadata together, is human readable, and is defined by a published dictionary rather than by the behavior of a particular program. A controlled vocabulary, so that a field name means the same thing in every file and software can determine whether a required field is present. Automated validation, run by a third party, producing a report that is distributed with the structure. Deposition tied to publication, enforced by journals.

None of these required agreement on a single kind of measurement, which is the objection most often raised against standardizing materials TEM.

## CIF and checkCIF

The Crystallographic Information File is a self-describing text format in which every value is tagged with a name drawn from a published dictionary, introduced by [Hall, Allen and Brown (1991)](https://doi.org/10.1107/S010876739101067X). Because the dictionary defines the tags, a program can determine whether a file contains the values it should, without knowing anything about the particular study.

checkCIF builds directly on that dictionary. It is a free service run by the IUCr that takes a CIF and returns a validation report of geometric, statistical, and consistency tests. Alerts are graded by severity, where level A indicates a potentially serious problem with the data, level B a potential problem, level C a minor issue, and level G is informational. Authors submitting to *Acta Crystallographica* Sections C and E are required to run checkCIF before submission and to respond to the alerts it returns.

Two features of this design are relevant to us. The validation is computed by a service other than the author, so a reviewer can read a report generated from the deposited data rather than relying on a methods section. Alerts are also treated as questions rather than accusations, since they routinely flag genuinely unusual structures, and the author's response is published alongside the entry. A validation regime that treated every flag as misconduct would likely be resisted, while one that expects an explanation has proven workable over many years.

Materials TEM currently has no equivalent of checkCIF. There is no service that would take a deposited 4D-STEM dataset and report that the convergence angle is inconsistent with the recorded diffraction pattern, or that the stated dose is not achievable at the stated dwell time and beam current. Checks of this kind are straightforward arithmetic on metadata we already claim to record.

## Where structures are deposited

The community sorted itself by molecule size rather than by technique. Macromolecular structures are deposited in the PDB, and the wwPDB OneDep system now handles 3DED and MicroED explicitly, collecting entries through the macromolecular crystallography framework with additional metadata describing electron diffraction collection and processing. Small-molecule structures are deposited in the CSD, or in the COD, which is fully open. Inorganic structures are deposited in the ICSD.

The practical result is that a structure carries an accession code, and a paper reporting a structure without one is not published. That requirement is what gives the technical standards their force.

## Where raw data goes, or does not

Deposited entries consist of models together with reduced intensities. For 3DED and MicroED this means that the diffraction movies themselves are not part of the required deposition. Groups that do publish frames typically use Zenodo, where a 3DED and MicroED community collects such datasets, but this remains a voluntary practice rather than a requirement.

This distinction matters more for electron diffraction than for X-ray work. Because electrons scatter strongly, the kinematical approximation relating measured intensity to structure factor holds only approximately, and dynamical refinement changes the result. The reduction from frames to intensities is therefore model-dependent, and two groups reducing the same frames can reasonably disagree. Without the frames, that disagreement cannot be examined.

For materials TEM we should do both, validating the derived product and archiving the raw measurement, rather than treating the two as alternatives. See [data](framework/data.md).

## Software

The 3DED community adopted the existing X-ray software stack, which is part of why the technique matured quickly. Data reduction is typically performed with XDS, DIALS, or PETS2, which handle peak finding, unit cell determination, geometry refinement, and intensity integration. Structure solution is usually carried out with SHELXT and refinement with SHELXL, and SIR, Superflip, and Olex2 are also in common use. Automated pipelines now chain these stages together for structure solution during acquisition.

Two observations follow for materials TEM. This community converged on a small number of shared tools that read a common format, and the tools are separable, so a group can substitute one stage without rewriting the pipeline. Analysis in materials TEM is instead dominated by one-off scripts that read vendor formats directly and are rarely released.

The stack is also not uniformly open. SHELX is free for academic use under a license rather than open source, and XDS is free but closed. Crystallography reached its present state on shared and stable software without requiring open source throughout, and it now has stages of its pipeline that cannot be inspected. See [analysis and plotting](framework/analysis.md).
