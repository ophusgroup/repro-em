---
title: Learning from crystallography
---

# Learning from crystallography

Crystallography is the strongest precedent available to us, and it is usually overlooked in favor of the structural biology archives. It should not be. Crystallography solved the validation problem, not just the deposition problem, and it solved it decades ago.

## What crystallography standardized

Four things, in an order worth copying.

A **file format** that carries data and metadata together, is human readable, and is defined by a published dictionary rather than by whatever a program happened to write.

A **controlled vocabulary**, so that a field name means the same thing in every file, and software can check that a required field is present.

**Automated validation**, run by a third party, producing a report that travels with the structure.

**Deposition tied to publication**, enforced by journals.

None of these required a single experiment type or a single instrument. That is the part that matters for us, because it is exactly the objection raised against standardizing materials TEM.

## CIF and checkCIF

The CIF is a self-describing text format in which every value is tagged with a name drawn from a published dictionary ([Hall, Allen and Brown, *Acta Cryst. A* 1991](https://doi.org/10.1107/S010876739101067X)). Because the dictionary defines the tags, a program can determine whether a file contains what it should, without knowing anything about the study.

checkCIF is what that buys. It is a free IUCr service that takes a CIF and returns a validation report of geometric, statistical, and consistency tests. Alerts are graded: level A flags a potentially serious problem, level B a potential problem, level C a minor one, and level G is informational. Authors submitting to *Acta Crystallographica* Sections C and E are required to run checkCIF and to respond to every alert.

Two features of this design are worth stealing outright.

**The validation is computed by someone other than the author.** A reviewer does not have to trust a methods section, because an independent service recomputed the checks from the deposited data.

**An alert is not an accusation.** Alerts routinely flag genuinely unusual structures, and the author's response is published alongside. This is what makes the system survivable in practice. A validation regime that treats every flag as misconduct will be resisted by everyone, and a regime that expects explanations will be tolerated.

Materials TEM has no checkCIF. We have no service that would take a deposited 4D-STEM dataset and report that the convergence angle is inconsistent with the recorded diffraction pattern, or that the stated dose is impossible at the stated dwell time and current. Every one of those checks is straightforward arithmetic on metadata we already claim to record.

## Where structures are deposited

The community sorted itself by molecule size rather than by technique.

Macromolecular structures go to the PDB. The wwPDB OneDep system now handles 3DED and MicroED explicitly, collecting the structure through the macromolecular crystallography framework with additional metadata describing electron diffraction data collection and processing.

Small-molecule structures go to the CSD, or to the COD, which is fully open. Inorganic structures go to the ICSD.

The result is that a structure has an accession code, and a paper reporting a structure without one does not get published. This single mechanism is worth more than every other item on this page.

## Where raw data goes, or does not

Here the precedent gets weaker, and the weakness is instructive.

Deposited structures are models with reduced intensities, not raw measurements. For 3DED and MicroED this means the frames, the actual diffraction movies, are not part of the required deposition. Groups that do publish them typically use Zenodo, and there is a 3DED/MicroED community there collecting such datasets, but this is a voluntary norm rather than a requirement.

So crystallography solved validation of the *model* while leaving archiving of the *measurement* optional. That gap matters more for us than for them, because dynamical scattering makes the reduction from electron diffraction frames to intensities far more model-dependent than in the X-ray case. Two groups reducing the same 3DED frames can reasonably disagree, and without the frames nobody can tell.

The lesson to carry into materials TEM is to not repeat this. Validate the derived product and archive the raw measurement. See [data](framework/data.md).

## Software

The 3DED community inherited the X-ray software stack, which is a large part of why it matured so quickly.

Data reduction uses XDS, DIALS, or PETS2, which handle peak finding, unit cell determination, geometry refinement, and intensity integration. Structure solution is usually SHELXT, with refinement in SHELXL, and SIR, Superflip, and Olex2 also in common use. Automated pipelines now chain these together for real-time solution during acquisition.

Two observations for our purposes. This community converged on a small number of shared tools that read a common format, and the tools are separable, so a group can substitute one stage without rewriting the pipeline. Materials TEM analysis is instead dominated by one-off scripts that read vendor formats directly and are never released.

The stack is also not uniformly open. SHELX is free for academics under a license rather than open source, and XDS is free but closed. Crystallography got a long way on shared and stable software without insisting on open source, and it now has stages of its pipeline that cannot be inspected. We should aim higher. See [analysis](framework/analysis.md).
