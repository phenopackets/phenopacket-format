
all: test all_json
test: test_examples

EXAMPLES=omim-example patient-example variant-example journal-example
all_json: all_json_l1
all_json_l1: $(patsubst %,examples/level-1/%-l1.json,$(EXAMPLES))

test_examples: test_examples_l1
test_examples_l1: $(patsubst %,examples/level-1/%-l1.report,$(EXAMPLES))



# ========================================
# update schema (warning, this overwrites)
# ========================================
JSON_SCHEMAS= phenopacket ontology-class

all_schemas: json_schemas proto_schemas

json_schemas:
	cp ../phenopacket-reference-implementation/target/json/*.json schema/
proto_schemas:
	cp ../phenopacket-reference-implementation/target/proto/*.proto schema/

#all_json_schemas: $(patsubst %, schema/%-schema.json,$(JSON_SCHEMAS))
#
#schema/%.json: ../phenopacket-reference-implementation/target/json/$*.json
#	cp $< $@
#schema/%.proto: ../phenopacket-reference-implementation/target/proto/$*.proto
#	cp $< $@
