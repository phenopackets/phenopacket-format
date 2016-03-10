## Requirements

The format is designed to be used to describe phenotypic descriptions
to be applied in a large variety of contexts, including, but not
limited to:

 * human patients
 * groupings of human patients, stratified by disease type
 * genes
 * variants or collections of variants
 * any of the above in non-human context

Note this context must be explicit. For example, phenotypes that are mentioned in the "background" section of a journal article should not be included in the phenopacket unless they are *also* phenotypes observed in the patients/organism/gene under study. Otherwise, the algorithms used to analyze the phenopackets could infer nonsense associations.

## Levels

Because different levels of precision are required for different
contexts, the schema is organized according to *levels* of
expressivity.

The most basic level is level-1

## Uses

The format is intended for a variety of uses: as a *submission*
format, for example, for submitting to a registry or database, or
*embedding* in a web page. It is also intended as an *authoring*
format. It is also usable for machine to machine interchange.

## Multiple Formats, One Model

We define a single *model*, but allow for multiple different
*syntaxes* or *formats*, for different purposes. Specifically:

 * Tab-Separated Variables (TSV): for authoring using standard spreadsheet tools like google docs or Excel
 * JSON: for machine-to-machine interchange
 * YAML: for authoring, submission and exchange
 * RDF

All of these are semantically equivalent *except* for TSV, which
expresses only a subset of the model.

See util/ for current list of convertors

## Structural Validators

This repository includes validators. We currently use Kwalify as a
validator. See the schema directory for kwalify schemas.

Other formats must be converted to YAML before validation.

## Semantic Validators

Semantic validators check the semantics of the document - e.g. are the
correct ontology classes used

## Minimal Requirements

### Minimal Requirements for Patient Phenotypes

The exchange format should define the minimal information to be
included in a submission, but should also allow for the recording of
optional information.

There are a certain set of core features that format MUST include. Note that
inclusion in the format does not mean the field is required. All
fields optional unless explicitly stated:

 * age of patient
 * sex of patient
 * disease (if named)
 * age of onset of disease
 * 1 to N positive phenotype associations for each person - REQUIRED
 * 0 to M negative phenotype associations for each person
 * Variants in HGVS notation, confirmed or set of variants

TBD: is this sufficient? Below are some additional complex attributes.
Note that if these are included in the format, then the complexity
will be increased, as the object model is no longer flat, we will need
either nesting in the format, or some kind of hackery

 * age of onset of the phenotype
 * severity of the phenotype
 * free text notes on a per-phenotype basis

The format or formats must have a formal specification that maps to a
well-defined data model. The format should have a defined translation
to RDF.

## Questions

### Siblings/Cohorts

Represent more than one patient, which could include siblings, parents, and other members of a cohort.

Note for relationships between the individuals, the ped file would be included. TODO: investigate who identifiability is
handled in a ped file, as this will impact how we use id fields.


