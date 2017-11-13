# PhenoPackets

[![](http://phenopackets.org/site/PhenoPackets_Logo.png)](http://phenopackets.org)

[![Build Status](https://travis-ci.org/phenopackets/phenopacket-format.svg?branch=master)](https://travis-ci.org/phenopackets/patient-phenotype-submission-format)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.46742.svg)](https://doi.org/10.5281/zenodo.46742)  


##  Overview

PhenoPackets is an open standard for representing and sharing detailed descriptions of phenotypic abnormalities and characteristics of individual patients, organisms, diseases, and publications. This repository serves as the primary documentation about the PhenoPacket Exchange Format (PXF), including the JSON and YAML representations. Other repositories (see [Implementations](#implementations) below) contain Java, JavaScript, Python and other language-specific tools and implementations.

### Motivation

The health of an individual organism results from a complex interplay between its genes and environment. Although great strides have been made in standardizing the representation of genetic information for exchange, there are no comparable standards to represent phenotypes (e.g. patient symptoms and disease features) and environmental factors. Phenotypic abnormalities of individual organisms are currently described in diverse places and in diverse formats: publications, databases, health records, registries, clinical trials, and even social media. However, the lack of standardization, accessibility, and computability among these contexts makes it extremely difficult to effectively extract and utilize these data, hindering the understanding of genetic and environmental contributions to disease. 


## Documentation

See the [Phenopackets.org site](http://phenopackets.org) for the public-facing project documentation.

Or, see the detailed Markdown-based [documentation](https://github.com/phenopackets/phenopacket-format/blob/master/docs/content/Overview.md) via GitHub.

The [Wiki](https://github.com/phenopackets/phenopacket-format/wiki/Getting-Started) has additional documentation, although it may be out-of-date.

## Implementations

- [phenopacket-reference-implementation: Java Reference Implementation](https://github.com/phenopackets/phenopacket-reference-implementation).
- [phenopackets-js: JavaScript Implementation](https://github.com/phenopackets/phenopackets-js).
- [phenopacket-python: Python Implementation](https://github.com/phenopackets/phenopacket-python).
- [pxftools: Command-line Utility for manipulating PhenoPackets](https://github.com/phenopackets/pxftools).

## Contributing

The PhenoPackets standard is still evolving, and there are many opportunities to help, including improving the expressivity of the format and providing implementations that enable.

The [Issue Tracker](https://github.com/phenopackets/phenopacket-format/issues/) is a good start.

