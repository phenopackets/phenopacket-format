import unittest
import os
import json
from jsonschema import validate, ValidationError, SchemaError
import python_jsonschema_objects as jsonobjects
import getopt,sys



def main():

    schema_path = "../schema/phenopacket-schema.json"

    try:
        opts,args = getopt.getopt(sys.argv[1:],"s:",["schema="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)

    for o,a in opts:
        if o in  ("-s","--schema"):
            schema_path=a
        else:
            assert False, "unhandled option"
    exfile = args[0]
    
 #   try: 
    schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
    schema = json.load(schema_fh)
    schema_fh.close()
#    except json.decoder.JSONDecodeError:
#        print("Schema file ", schema_path, " does not contain a valid JSON file")
#        sys.exit(1)
    

    try:
        file_fh = open(exfile,'r')
        data = json.load(file_fh)
        file_fh.close()
    except IOError:
        print ("Could not read phenopacket file ",exfile)
        sys.exit(2)
    except json.decoder.JSONDecodeError:
        print("Phenopacket file ", exfile, " does not contain a valid JSON file")
        sys.exit(3)


    # http://python-jsonschema.readthedocs.org/en/latest/errors/
    try:
        print("running validator");
        validate(data,schema)
        print("Valid phenopacket")
    except SchemaError as s:
        print ("Schema error in schema ", schema_path)
        print (s.message)
    except ValidationError as e:
        print("Invalid phenopacket found in ",exfile)
        print(e.message)        
            


def usage():
  print('Usage: '+sys.argv[0]+' -s <schemafile> [option]')
  print('       '+sys.argv[0]+' --schema=<schemafile> [option]')

if __name__ == '__main__':
    main()
