import unittest
import os
import json
from jsonschema import validate, ValidationError, SchemaError
import python_jsonschema_objects as jsonobjects
from python_jsonschema_objects import ValidationError as ValidationException


class ValidatorTestCase(unittest.TestCase):
    """
    Test various json validators, jsonschema seems to be a popular
    lib, warlock and python-jsonschema-objects are build off
    of jsonschema and also include json to python object mappers

    The goal of this is to experiment with library options but these
    could eventually be integrated into the phenopacket python api

    As a first pass, testing that the journal example is incorrect
    and the rest are correct. These could be expanded in the future
    as appropriate
    """

    def setUp(self):
        schema_path = "../schema/phenopacket-schema.json"
        journal_path = "../examples/level-1/journal-example-l1.json"
        omim_path = "../examples/level-1/omim-example-l1.json"
        patient_path = "../examples/level-1/patient-example-l1.json"
        variant_path = "../examples/level-1/variant-example-l1.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        self.schema = json.load(schema_fh)

        journal_fh = open(os.path.join(os.path.dirname(__file__), journal_path), 'r')
        self.journal_example = json.load(journal_fh)

        omim_fh = open(os.path.join(os.path.dirname(__file__), omim_path), 'r')
        self.omim_example = json.load(omim_fh)

        patient_fh = open(os.path.join(os.path.dirname(__file__), patient_path), 'r')
        self.patient_example = json.load(patient_fh)

        variant_fh = open(os.path.join(os.path.dirname(__file__), variant_path), 'r')
        self.variant_example = json.load(variant_fh)

        schema_fh.close()
        journal_fh.close()
        omim_fh.close()
        patient_fh.close()
        variant_fh.close()

    def tearDown(self):
        self.schema = None
        self.journal_example = None
        self.omim_example = None
        self.patient_example = None
        self.variant_example = None

    def test_incorrect_journal(self):
        """
        Test that the journal example is invalid since it
        uses "human" instead of patient
        'human' is not one of ['disease', 'organism', 'patient', 'variant', 'genotype']
        """
       # with self.assertRaises(ValidationError):
        #    validate(self.journal_example, self.schema)
        try:
            validate(self.journal_example, self.schema)
            self.assertFail()
        except ValidationError as e:
            self.assertEqual(e.message,
                             "'human' is not one of ['disease', 'organism', 'patient', 'variant', 'genotype']")


    def test_omim_example(self):
        """
        Test that our other example files validate as correct
        """
        validate(self.omim_example, self.schema)

    def test_patient_example(self):
        """
        Test that our other example files validate as correct
        """
        validate(self.patient_example, self.schema)

    def test_variant_example(self):
        """
        Test that our other example files validate as correct
        """
        validate(self.variant_example, self.schema)

    def test_jsonobjects_as_validator(self):
        builder = jsonobjects.ObjectBuilder(self.schema)
        namespace = builder.build_classes()

        # check that this works
        pheno_packet = namespace\
            .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
            .from_json(json.dumps(self.omim_example))

        # check that this raises an exception
        with self.assertRaises(ValidationException):
            journal = namespace\
                .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
                .from_json(json.dumps(self.journal_example))

    def test_invalid_schema(self):
        schema_path = "../resources/schemas/phenopacket-level-1-schema-bad.json"
        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        schema = json.load(schema_fh)
        schema_fh.close()

        # this should fail
        with self.assertRaises(SchemaError):
            validate(self.omim_example,schema)

        


if __name__ == '__main__':
    unittest.main()
