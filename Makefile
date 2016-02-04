

EXAMPLES=omim-example patient-example
all_examples: all_examples_l1
all_examples_l1: $(patsubst %,examples/level-1/%-l1.json,$(EXAMPLES))

%.json: %.yaml
	util/yaml2json.py $< > $@.tmp && mv $@.tmp $@
