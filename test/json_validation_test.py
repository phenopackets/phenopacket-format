import unittest
import os
import json
from jsonschema import validate, ValidationError, SchemaError,Draft4Validator
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

    def test_valid_schema(self):

        schema_path = "../schema/phenopacket-schema.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        schema = json.load(schema_fh)
        schema_fh.close()
        
        ## call validator
        Draft4Validator.check_schema(schema)

if __name__ == '__main__':
    unittest.main()
