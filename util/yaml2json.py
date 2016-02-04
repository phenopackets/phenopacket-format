#!/usr/bin/env python3

__author__ = 'cjm'

import yaml
import dtjson as json
#import json
import optparse
     
parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if (len(args) != 1):
    raise ValueError("Must pass exactly 1 yaml file")
stream = open(args[0], 'r');
data = yaml.load(stream)
data['@context'] = "http://phenopacket.github.io/context/context.jsonld"
#json = dtjson.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
json = json.dumps(data)

print(json)
