import unittest
import os
import json
import python_jsonschema_objects as jsonobjects
import inspect

class JsonToObjectTestCase(unittest.TestCase):
    """
    Test JSON to Python Object Mappers such as warlock and
    python_jsonschema_objects, see
    http://stackoverflow.com/questions/12465588/convert-a-json-schema-to-a-python-class
    """

    def setUp(self):
        schema_path = "../schema/phenopacket-schema.json"
        omim_path = "../examples/level-1/omim-example-l1.json"
        variant_path = "../examples/level-1/variant-example-l1.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        self.schema = json.load(schema_fh)

        omim_fh = open(os.path.join(os.path.dirname(__file__), omim_path), 'r')
        self.omim_example = json.load(omim_fh)

        variant_fh = open(os.path.join(os.path.dirname(__file__), variant_path), 'r')
        self.variant_example = json.load(variant_fh)

        builder = jsonobjects.ObjectBuilder(self.schema)
        self.namespace = builder.build_classes()

        schema_fh.close()
        omim_fh.close()
        variant_fh.close()

    def tearDown(self):
        pass

    def test_omim_object_mapping(self):

        pheno_packet = self.namespace\
            .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
            .from_json(json.dumps(self.omim_example))

        # inspect parent classes of entities
        # print(inspect.getmro(pheno_packet.entities[0].__class__.__bases__[0]))
        # (<class 'python_jsonschema_objects.classbuilder.ProtocolBase'>,
        #  ...
        #  <class 'collections.abc.Iterable'>, <class 'collections.abc.Container'>,
        #  <class 'object'>)

        self.assertEqual(pheno_packet.entities[0].id, 'OMIM:615426')

    def test_variant_om(self):
        pheno_packet = self.namespace\
            .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
            .from_json(json.dumps(self.variant_example))

        variant = list(filter((lambda var: var['entity'] == '_:v1'), pheno_packet.phenotype_profile))

        test_json = "{\"type\": {\"label\": \"Muscular dystrophy\"," \
                  " \"id\": \"HP:0003560\"}, \"description\": \"blah blah\"," \
                  " \"onset\": {\"type\": {\"label\": \"Late onset\", \"id\": \"HP:0003584\"}}}"
        test_dict = json.loads(test_json)

        self.assertEqual(variant[0].phenotype.for_json(), test_dict)

        # This might be an unexpected edge case
        # variant[0].phenotype.type is a class
        # with the attribute _value that equals a dict
        # print(variant[0].phenotype.type.__class__)
        # <class 'python_jsonschema_objects.classbuilder.type'>

        self.assertEqual(variant[0].phenotype.type._value['id'], 'HP:0003560')
        self.assertEqual(variant[0].phenotype.type._value['label'], 'Muscular dystrophy')

    def test_rountrip_json(self):
        pheno_packet = self.namespace\
            .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
            .from_json(json.dumps(self.omim_example))

        # for_json converts objects to dict
        self.assertEqual(self.omim_example, pheno_packet.for_json())


if __name__ == '__main__':
    unittest.main()
