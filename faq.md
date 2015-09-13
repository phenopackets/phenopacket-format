## How will files be generated

The files can be generated using a variety of methods. Anyone can
write tools to the spec. Web Phenote will be capable of translating to
this format.

The CSV format is designed to be authored directly in Excel, perhaps
by using an existing template file.

## One format or many?

We may need different formats for different scenarios. The important
thing is a unified model. See [phesub-model.md](phesub-model.md)

## Is this an exchange format?

The primary use case here is *submission* to a journal or
registry. Whilst this is a form of exchange it should be
differentiated from machine-to-machine exchange which may have
different requirements.

M-M exchange would most likely use JSON or IDL based exchange
(e.g. protobuf).

The important thing is that the exchange format here must be derived
from the same datamodel.

