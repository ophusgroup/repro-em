---
title: Publishing
---

# Publishing

## Scientific publications

Publish ALL data. Raw experimental data, the full processing pipeline, and all of the software, open source so that it can be independently verified. No black boxes, meaning no step whose source code we are not allowed to read. Machine learning is fine, and we must be able to see how it was trained, with open training data and open weights.

The full pipeline needs to be validated. See [chain of custody](chain-of-custody.md).

No publication should ever be accepted with the dreaded words "data available upon reasonable request."

That phrase has been measured, and it does not survive contact with evidence. Of 1,792 manuscripts whose availability statement said the authors were willing to share, 93% of authors either declined or never responded, and only 6.8% actually produced the data when asked ([Gabelica et al., *J. Clin. Epidemiol.* 2022](https://doi.org/10.1016/j.jclinepi.2022.05.019)).

The statement also carries very little information. Across 875 papers in *Nature* and *Science*, requests succeeded 39.4% of the time on average, and papers promising data on request were no more likely to deliver it than papers promising nothing at all. The authors' conclusion is that such statements are inefficient and should not be allowed by journals ([Tedersoo et al., *Sci. Data* 2021](https://doi.org/10.1038/s41597-021-00981-0)).

Availability also decays with time. Across 516 papers spanning two decades, the odds of recovering a usable dataset fell about 17% for every year since publication ([Vines et al., *Curr. Biol.* 2014](https://doi.org/10.1016/j.cub.2013.11.014)). A promise to share on request therefore has a half-life of roughly four years, which is shorter than the useful life of most of our datasets.

Data must therefore be deposited at publication, while it still exists and while someone still knows what it is.

## Dark data

It's an open secret that almost all microscopy data ever recorded is unpublished. Much of this data is useless, but some of it is not. Authors should not publish a "representative micrograph" but rather publish the full range of recorded data so that readers can judge for themselves.

Selection is a common route by which honest error enters the literature. Nobody picks the field of view that undermines their argument, and nobody has to be dishonest for that to bias a result. A grain boundary that looked wrong gets attributed to preparation damage, a region that did not show the expected contrast gets called unrepresentative, and neither judgment is ever written down or seen by a reader.

Publishing the full set now costs very little. Storage is cheap, chunked formats make large datasets browsable without downloading them, and the reader who wants to check whether "representative" was fair can simply look. See [sharing data](sharing.md).

Dark data also has value the original authors cannot extract. Reprocessing archives with methods that did not exist at acquisition time is now a routine source of results in structural biology, and it is only possible because the raw data was kept. Every unpublished 4D-STEM dataset sitting on a lab drive represents a ptychographic reconstruction that nobody will get the chance to attempt.
