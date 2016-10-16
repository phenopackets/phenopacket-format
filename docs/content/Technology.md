### What is in a Phenopacket?

Achieving a functional and community-adopted PXF standard will require addressing several critical requirements, which are only partially fulfilled by this first release of Level 1 of the standard. Here we detail the basic level 1 components, and urge the community to participate in helping extend and evaluate the PXF:

Content	Description	Example
Phenotypes	Representation of phenotypic features using an ontology term with a resolvable and versionable identifier.	http://purl.obolibrary.org/obo/HP_0001943
‘Hypoglycemia’ Defined as: “A decreased concentration of glucose in the blood.”

### Age of onset
Each phenotype can be indicated the exact age, or age range, for which the phenotype first manifested. ISO year and month standards should be followed, or the use of ontology terms from HPO for age ranges are recommended.

 `P43Y08M`
 or
 `Adult onset (HP:0003581)`

### Negation of phenotypes

Notable absence of a particular phenotype or phenotypic class.
 `NOT Aortic regurgitation (HP:0001659)`

### Genomic data
Able to link to a VCF file, describing the patient’s genomic variants, or HGVS notation

### Family history
Able to link to a PED file, describing familial linkage to other PCF files.

### Quantitative specification
Quantitative phenotypes expressed in relative terms should be accompanied with reference population and values.	A
bility to transmit not only qualitative ontology terms such as “Hyperglycemia” but also specific values such as “blood glucose 178 mg/dl”

### Evidence
Any of the above elements may be linked to one or more evidence assertions.
Evidence could include items of the following:
* EHR record numbers
* published papers
* functional assays
* computational models
* population studies
* clinical trials


# Technology - Standards and Implementation

The online supplementary material to this article presents the version 1.0 of the PXF standard proposed in this article. The format defines the required information expected to be transmitted about each individual – aka a  “Phenopacket”; it includes items such as as patient identifier (non-PHI), age or age group, sex, and a list of one or more phenotypic abnormalities represented by ontology terms. The use of HPO is recommended but if not possible, an alternative terminology as represented in the International Committee of Human Phenotype Terminologies (ICPHT), an activity of the International Rare Disease Research Consortium (IRDiRC), is acceptable. Figure 1 provides a summary of the Phenopacket exchange ecosystem, and the online supplement provides concrete examples of PXF encoded in several exchange formats such as XML, JSON, and RDF. Note that PXF is designed to be compatible with a variety of rare disease phenotyping efforts, such as 100,000 genomes17.


# A PhenoPacket Example in YAML

Phenopackets can be encoded in either JSON or YAML, there is no
difference between the two. We will use YAML here for compactness.

Our example involves a case study with three people (phenopackets can
be used to describe other kinds of entities such as variants, examples
on these cases will follow).

We list all people inside a `persons` block:

```yaml
persons:
  - id: "#1"
    date_of_birth: 1999-01-01
    sex: M
  - id: "#2"
    sex: M
  - id: "#3"
    sex: M
```

Note that in YAML, a `-` denotes an element in a list. The value of the `persons`
property is always a list.

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

```yaml
disease_diagnoses:
  - entity: "#1"
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

Next up is phenotype associations. Let's start with a two phenotypes
for person 1:

```yaml
phenotype_profile:
  - entity: "#1"
    phenotype:
      types:
        - id: HP:0003560
          label: Muscular dystrophy
  - entity: "#1"
    phenotype:
      types:
        - id: HP:0007354
          label: Amyotrophic lateral sclerosis
```

Each element of the list is a phenotype *association*. The concept of
an association is a recurring feature of the phenopacket format.

Although the structure may appear overly nested here, this because we
use a highly normalized model that allows maximal hooks for
extensibility. For example, we can add `onset` into the phenotype
object, where onset is described either with an ontology term or with
a quantitative range. We can also attach a natural language
description to the phenotype, to complement or extend the ontological
one.

Similarly, the association itself can have evidence and additional
provenance and audit information associated with it. This is shown in
the following example:

```yaml
phenotype_profile:
  - entity: "#1"
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
      - types:
          id: TAS
        source:
          id: PMID:23455423
          title: Mutations in prion-like domains in hnRNPA2B1 and hnRNPA1 cause multisystem proteinopathy and ALS
  - entity: "#1"
    phenotype:
      types:
        - id: HP:0007354
          label: Amyotrophic lateral sclerosis
```

The example can be visualized as:

![](./person-example.png)
