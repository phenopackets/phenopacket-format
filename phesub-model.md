NOT NORMATIVE

TODO: UML - and separate OWL into separate document

About this document: this specifies an object model for phesub. Note
that UML closed-world semantics are assumed. i.e. we may say "An
individual has zero or one sex". This is a cardinality constraint at
the level of the information model. Obviously, in the RDF/OWL
translation, the constraint is that an individual has exactly one sex
(open world assumption).

A submission consists of one or more individuals. Each individual can
be associated with any number of a set of specified attributes. Some
of these attributes are atomic, some are objects in their own right.

## Individuals

In the translation to OWL, each individual `?i` is assumed to be of type
human; the following are automatically added:

    ?i rdf:type NCBITaxon:9606

Each individual can have exactly one Age. An Age is an object with two
atomic fields, magnitude and unit. Unit comes from UO (in practice
`years` is likely to be used).

OWL Model: ?

Each individual has exactly one Karyotypic sex. This comes from PATO (TBD?)

OWL Model:

```
i has_quality [
  a PATO:nnnn
]
```

Each individual can have zero or more disease occurrences. Each
disease occurrence is an object with fields `type` and `age of onset`,
with the latter referring back to the previously defined age object.

```
i has_disease [
  a OMIM:nnnnn
  TBD-age
]
```

### Phenotypes

Each phenotype is an object with `(ID, Age of Onset)`. Here age HPO?

Note that in some simplified derived exchange formats, the set of
phenotypes for a patient may be a flat list of IDs (TBD?). But in the
model these are objects.

TODO: post comp? descriptions?

### Causal Variants

Note we do not explicitly model the structure of the causal variant. This is out of scope. Instead the causal variant is modeled as a string. Some kind of external validation assumed.

Refer to GENO for conversion of HGVS to OWL

### Relationships between individuals

Out of scope. But for completion we should have a separate ped2owl mapping

