---
title: Calls to action
---

# Calls to action

Nothing on this site requires new technology. It requires that each part of the community ask for the same things at the same time, so the following are addressed to specific actors rather than to the field in general.

## Researchers

- **Publish everything.** Raw data, metadata, analysis code, scripts, and the plotting code that made the figures.
- **Deposit at publication.** Never "available upon reasonable request", which produces the data 6.8% of the time ([Gabelica et al. 2022](https://doi.org/10.1016/j.jclinepi.2022.05.019)).
- **Report cross-validation** for every reconstruction, alongside the result.
- **Buy verifiable.** Prioritize detectors and instruments that can sign their output and write complete metadata.
- **Cite data and software** as first-class research products, so that sharing them is an investment rather than a loss.

## Vendors

Microscope and detector manufacturers hold the start of the chain, and several of these are decisions only they can make.

- **Open formats.** A published specification and open APIs, so that reading our own data does not depend on reverse engineering.
- **Complete metadata,** written automatically at acquisition, including the calibrations. See [metadata](framework/metadata.md).
- **Programmatic control.** Full scripting access to the instrument, so experiments can be described in code and repeated.
- **Sign at the detector.** Hardware keys, published public keys, and a documented key rotation policy. See [validated detectors](framework/detectors.md).
- **Open verification.** Tools that let anyone check a signature without running vendor software.

## Publishers

- **Require accession codes.** No deposition, no publication, which is the mechanism that made the structural biology archives work.
- **Ban the phrase.** "Available upon reasonable request" fails 93% of the time and carries no information about whether data will actually be shared.
- **No black boxes.** Code, computational environment, and model weights open and inspectable.
- **Require validation.** Cross-validation reported alongside any reconstruction-based claim.
- **Review the data,** not only the figures, and give reviewers the time and credit that this requires.

## Funding agencies

Data management plans are already required by most agencies, and are neither funded nor enforced.

- **Fund curation explicitly** as a line item, rather than assuming it happens for free at the end of a project.
- **Enforce the plans** that are already required, by checking deposition at reporting time.
- **Resource the facilities** to curate centrally, since a facility can do this once for many users.
- **Support the archives** that materials EM will need, and the software that reads and writes the formats.

## Facilities and industry

- **Capture metadata at the instrument** by default, so that users do not have to reconstruct it later.
- **Provide deposition as a service,** in the same way that facilities already provide sample preparation and instrument time.
- **Publish under embargo where necessary,** with a fixed expiry and a registered identifier, rather than not at all. See [objections and exceptions](objections.md).
