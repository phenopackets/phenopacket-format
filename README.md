[![Build Status](https://travis-ci.org/cmungall/patient-phenotype-submission-format.svg?branch=master)](https://travis-ci.org/cmungall/patient-phenotype-submission-format)
[![DOI](https://zenodo.org/badge/13996/cmungall/patient-phenotype-submission-format.svg)](https://zenodo.org/badge/latestdoi/13996/cmungall/patient-phenotype-submission-format)

The health of an individual organism results from a complex interplay between its genes and environment. Although great strides have been made in standardizing the representation of genetic information for exchange, there are no comparable standards to represent phenotypes (e.g. patient symptoms and disease features) and environmental factors (Figure 1). Phenotypic abnormalities of individual organisms are currently described in diverse places and in diverse formats: publications, databases, health records, registries, clinical trials, and even social media. However, the lack of standardization, accessibility, and computability among these contexts makes it extremely difficult to effectively extract and utilize these data, hindering the understanding of genetic and environmental contributions to disease. 

For more information, start with [requirements.md](requirements.md)

## Walk-through example


Phenopackets can be encoded in either JSON or YAML, there is no
difference between the two. We will use YAML here for compactness.

Our example involves a case study with three people (phenopackets can
be used to describe other kinds of entities such as variants, examples
on these cases will follow).

We list all people inside a `persons` block:

```
persons:
  - id: #1
    date_of_birth: 1999-01-01
    sex: M
  - id: #2
    sex: M
  - id: #3
    sex: M
```

Note that in YAML, a `-` denotes an element in a list. The `person`
block is always a list.

Here we are providing a DOB for the first person, and biological sexes
for all persons.

Note the identifiers used. There are strict rules on the structure of
identifiers used in phenopackets, and on the rules for mapping these
to real-world entities. We will return to these in more detail
later. In this particular case we are using hash identifiers; we use
these when the identifiers are local to the packet and are not
intended to be referenced from outside. If we had a global identifier
for the person, we could use this instead.

Next we will describe the conditions for these persons. In
phenopackets, there are two distinct types of conditions: phenotypes
and diseases.

We first list any disease diagnoses. We only have one, for person
number 1:

```
disease_diagnoses:
  - entity: #1
    disease_occurrence:
      types:
        - id: OMIM:615426
          label: amyotrophic lateral sclerosis type 20
```

Note that the diseases block is a separate block from the persons
block. We refer back to individuals in the block using the id, rather
than nesting the disease inside the person block. This allows for more
flexibility in how persons and diagnoses are exchanged as messages.

The value for `types` is a list. Although there will
typically only be one disease here, there are reasons for having a
uniform list representation, which we will return to later.

We have not specified any diseases for person 2 and 3. Although we
might assume these are not disease carriers, this is not explicitly
stated and cannot be known for sure. We will return to how to make
negative assertions later on.

Next up is phenotype associations. Let's start with a two phenotypes,
for person 1

```
phenotype_profile:
  - entity: #1
    phenotype:
      types:
        - id: HP:0003560
          label: Muscular dystrophy
  - entity: #1
    phenotype:
      types:
        - id: HP:0007354
          label: Amyotrophic lateral sclerosis

```

Although the structure may appear overly nested here, this because we
use a highly normalized model that allows maximal hooks for
extensibility. For example, 

```
phenotype_profile:
  - entity: #1
    phenotype:
      types:
        - id: HP:0003560
          label: Muscular dystrophy
      onset:
        types:
          - id: HP:0003584
            label: Late onset
      description: additional notes on this phenotype here
    evidence:
      - type: TAS
        source:
          id: PMID:23455423
          title: Mutations in prion-like domains in hnRNPA2B1 and hnRNPA1 cause multisystem proteinopathy and ALS
  - entity: #1
    phenotype:
      types:
        - id: HP:0007354
          label: Amyotrophic lateral sclerosis

```
