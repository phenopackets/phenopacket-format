# Community

Historically, successful standards evolve gradually over time. They are not designed in the abstract, springing fully-formed from committee, but rather are developed incrementally as they are taken into the field and proven to successfully meet real-world challenges. Level 1 of the PXF is intentionally simple in order to ease wide adoption of the standard and thereby increase the value of the network of systems (see Figure 1) aiming to share Phenopackets for computational use.

The requirements for such a standard are:

1.	Computable. The standard must be both human and machine-interpretable, enabling computing operations and validation on the basis of defined relationships between diagnoses, lab measurements, genotypic information, and medications.

2.	Transferable. The standard must enable seamless transfer of data from a data source (e.g., a document describing the phenotype) to a data receiver (e.g., an application that receives and uses it). The standard can have multiple serializations, such as tab-separated-values, XML, or JSON.

3.	Utilize an ontology for phenotypes. The standard must enable “fuzzy matching”, that is, the use of algorithms that leverage the logic within an ontology to match sets of phenotypes that are related but not exact matches. This is currently mission critical for rare disease, and we believe will also greatly facilitate precision medicine.

Journals can aid use of the PXF standard by supporting data citation to Phenopackets, essentially a metadata record, which will be made available as a separate online document resolvable by a Digital Object Identifier (DOI)18. Phenopackets can be deposited in the journal, a public phenotype data repository such as the Monarch Initiative, or in generic data repositories such as FigShare. This approach ensures that the phenotype data described within a manuscript is made computable outside the pay-wall of journals, and can be cited within the original article via the DOI. The PXF has been adopted as a recommended or mandatory standard by journals including the CSH Molecular Case Studies, the Orphanet Journal of Rare Disease, and XXX.

It is hoped that public data repositories will begin to accept phenotype data provided in PXF. For example, the Monarch Initiative19 is already pulling Phenopacket data from the aforementioned journals and also provides an online editor tool for creating them. A variety of international efforts that aim to standardize genotype-phenotype data, such as the International Rare Diseases Research Consortium (IRDIRC) and the Global Alliance for Genomics and Health (GA4GH), support the use of this new PXF standard for sharing phenotypic data related to variant and other genomic health data.



# Discussion

In many ways, the phenotype data exchange community is in a position similar to that of the genetics community in the early days of public sequence databases. Although the content of sequence descriptions has changed over the years, this evolution is a sign of success, not failure. Early descriptions played key roles both in promoting the effective use of sequence data and in understanding how that data should be recorded and communicated. The Phenopacket standard proposed here is tailored to function in the context of rare disease, and for precision medicine in cancer and other common diseases. We are currently in an exciting position and the standardization and exchange of a broad range of phenotype data can trigger a new wave of advances in medical discovery and realize the goal of precision medicine. Further, patient-centered phenotyping approaches offer the opportunity, if not the necessity, for affected individuals and their families to be involved and integrated into the wider context that is the future of precision medicine.

The documentation and use of data for patients with challenging to diagnose rare and genetic conditions is different than for more common diseases. The realization of this vision and the phenotype exchange requirement described here will require substantial effort. Given the relative immaturity of existing efforts, further research and prototypes of data capture and exchange systems will be necessary to better understand the issues. Such explorations will likely be undertaken by ongoing research efforts, many which do not have the luxury of waiting for the completion of an emerging consensus model.



