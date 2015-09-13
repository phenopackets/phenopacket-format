## Requirements

The format is designed to be used to describe phenotypes associated
with a human patient, together with asserted hypothetical causal
variants (either HGVS or build plus coords).

The format is intended for rare and undiagnosed disease patients. It
is not intended for cancer patients (although presence of cancer may
be a feature of the disease). It is not intended for common disease
patients. It is not intended to do the work of an EHR. For example, it
would not record any history of treatment.

The intent is that a file conforming to this format is submitted to
either a journal or patient registry. In the case of the former, the
submitter would be a clinical researcher, in the case of the latter,
the submitter could be any of the following: clinician, family,
individual, ...

The format is intended primarily as a submission format rather than a
machine-to-machine exchange format. As such it must be easy to
author. We would like submitters to use some kind of application
(desktop or web) that would generate the file, but to maximize
adoption we do not impose the need for a tool.

We do not have to dictate one single format. One possibility is
multiple formats with a unified data model and specified
conversions. This will allow us to have technophobic submitters use
Excel to generate a CSV, and more sophisticated submitters or
submitters who are using the appropriate tooling to express things in
more depth.

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

From M: "be able to represent patients, siblings, and cohorts"

What does this mean? Represent relationships between them? Or is the
requirement simply that more than one human can be included in a
submission?

I assume the latter. Note for relationships between the individuals,
the ped file would be used. TODO: investigate who identifiability is
handled in a ped file, as this will impact how we use id fields.

