# PhenoPackets Conceptual Overview

Prevailing clinical pipelines leverage only a tiny fraction of the data available, relying upon patient exome and genome data to characterize patients, and searching public databases to find potential similarities. This is possible because standard formats have been developed for these types of data (genome and variant), which enables automation, search and similarity matching.

Although great strides have been made in standardizing the representation of genetic information for exchange, there are no comparable standards to represent phenotypes (e.g. patient symptoms and disease features) or environmental factors.

The health of an individual organism results from complex interplay between its genes and environment. Although great strides have been made in standardizing the representation of genetic information for exchange, there are no comparable standards to represent phenotypes (e.g. patient symptoms and disease features) or environmental factors (Figure 1). Phenotypic abnormalities of individual organisms are currently described in diverse places and in diverse formats: publications, databases, health records, registries, clinical trials, and even social media. However, the lack of standardization, accessibility, and computability among these contexts makes it extremely difficult to effectively extract and utilize these data, hindering the understanding of genetic and environmental contributions to disease. We are a multi-disciplinary, international scientific team comprised of basic science researchers, data modelers, computer scientists, bioinformaticians, environmental scientists, and clinicians dedicated to maximizing the value of existing and new data. Here we propose a new unit of exchange for the open data marketplace that will make the sharing of phenotype data sustainable, persistent, and reusable without sacrificing the flexibility needed to express rapidly emerging threats to the environment and human health (e.g., Zika virus). This unit, called a “Phenopacket”, will contain the minimal amount of information necessary for describing one or more patients, cohorts, or populations in a computable way. The Phenopacket is citable, persistent, and available outside the paywall of journals, read and written by anyone: data repositories, patient registries, drug companies, environmental monitoring agencies, and even patients themselves, to enable crowdsourced analysis. We will develop the standard and initial software tools to read, write, and validate Phenopackets. The greater accessibility and computability of these data have the potential to revolutionize the field of healthcare analytics. 



## Standards Enable Computation

VCF for example, Sequence Similarity

PhenoTypes need an exchange format to enable cross-species analysis

PhenoTypes are difficult


## Why are PhenoTypes hard?


# PXF: Phenotype Exchange Format (BOSC 2016)

- One model, many encodings
	- YAML, JSON, RDF, TSV
- Species-agnostic
	- Microbes, plants, humans
	- Clinical and basic research
- Support variety of entities
	- Patients/individuals organisms, cohorts, populations
	- Diseases
	- Papers
	- Genes, genotypes, alleles, variants
- Simple for simple cases
	- Bag of terms model
- Incremental expressivity
	- Temporality and Causality
	- Quantitative and qualitative
	- Negation, severity, frequency, expressivity
- Ontology-smart
	- Rational composition (post-coordination)
	- Explicit Semantics

## PhenoPackets Features

- Findable
- Accessible outside paywalls and private data sources
- Attributable
- Interoperable and Computable
- Reusable, exchangeable across contexts and disciplines


## Today's Scientific Landscape

### Siloed information

### Bridges being built

### Tower of Babel

### Standard Ontologies


## The Phenotype Problem

### Phenotypes are coarse-grained observables

### That derive from pathways and processes

### That derive from gene expression

### That may be affected by gene variation


## The role of PhenoPackets





## What's Deep Phenotyping?

## What's Translational Research?


## What's a Phenotype?

It is important to understand the difference between the terms **disease** and **phenotype**. They are often used interchangeably, but that obscures the important relationship between the genetic *causes* of disease and the phenotypic *effects* of these underlying genetic phenomena.

We use **phenotype** to refer to a discrete feature, such as *hypoglycemia*, that is one observable component of a disease, such as diabetes mellitus type II.

The Phenotype Exchange Format (PXF) proposed here is designed to support “deep phenotyping”, a process wherein individual components of each phenotype are observed and documented[5](ref:5).

## What is an Ontology?

In order to describe things and communicate, a *community* agrees upon names for organisms, diseases, anatomy and phenotypes. The Tower of Babel problem is that multiple communities exist, each of which has developed their own nomenclature.

The PXF requires the use of a common ontology, a logically defined hierarchy of terms, that allows sophisticated algorithmic analysis over medically relevant abnormalities. **computable**

## What does Computable mean?

The PXF requires the use of a common ontology, a logically defined hierarchy of terms, that allows sophisticated algorithmic analysis over medically relevant abnormalities. **computable**

## The Human Phenotype Ontology

The Human Phenotype Ontology (HPO) [6](ref:6) was built for this purpose and has been used for genomic diagnostics, translational research, genomic matchmaking, and systems biology applications [7–14](ref:7-14). The HPO is developed in the context of the Monarch Initiative, an international team of computer scientists, clinicians, and biologists in the United States, Europe, and Australia; HPO is being translated into multiple languages to support international interoperability. Due to its extensive phenotypic coverage beyond other terminologies [15,16](ref:15,16), HPO has recently been integrated into the Unified Medical Language System (UMLS) to support deep phenotyping in a variety of mainstream health care IT systems.


## Like VCF, but for Phenotypes

While great strides have been made in exchange formats for sequence and variation data (e.g. Variant Call Format; VCF [1](ref:1), complementary standards for phenotypes and environment are urgently needed.

## Disease Diagnosis and Treatment

For individuals with rare and undiagnosed diseases, such standards could improve the speed and accuracy of diagnosis. For patients with common but hard-to-treat diseases, such standards can help us design personalized interventions and learn more about shared disease mechanisms [2](ref:2).



## It's about us

The health of an individual organism results from a complex interplay between its genes and environment.


## No Standards

Although great strides have been made in standardizing the representation of genetic information for exchange, there are no comparable standards to represent phenotypes (e.g. patient symptoms and disease features) and environmental factors.

## Diverse Sources and Formats

Phenotypic abnormalities of individual organisms are currently described in diverse places and in diverse formats: publications, databases, health records, registries, clinical trials, and even social media.


## Standardization, Accessibility, Computability

However, the lack of standardization, accessibility, and computability among these contexts makes it extremely difficult to effectively extract and utilize these data, hindering the understanding of genetic and environmental contributions to disease.

## We Propose

We propose that when phenotypic abnormalities of individuals are described, whether in publications, databases, health records, or social media, that these descriptions a) contain a minimum set of fields and b) get transmitted alongside genomic sequence data, such as in VCF, between clinics, authors, journals, and data repositories.  The structure of the data in the exchange standard will be optimized for integration from these distributed contexts. 


## Benefits

The implementation of such a system will allow the sharing of phenotype data prospectively, as well as retrospectively.  Increasing the volume of computable data across a diversity of systems will support large-scale computational disease analysis using the combined genotype and phenotype data.

## Data Size Necessity

It is necessary because study sizes of well over 100,000 patients are thought to be required to effectively assess the role of rare variation in common disease [3](ref:3) or to discover the genomic basis for a substantial portion of Mendelian diseases [4](ref:4).

## Welcome to the Future

It is timely because studies of this power are now becoming financially and technologically tractable.








