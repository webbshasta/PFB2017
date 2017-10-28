#!/usr/bin/env python3

import sys
import pronto

ont = pronto.Ontology('/Users/admin/Webb_PFB2017/problemsets/Ontology_1/go.owl')

GO_GENES = sys.argv[1] # this is your gene list (gene_id\tgo_id\tgo_name)
MY_GO_ID = sys.argv[2] # this is the GO term you want to search for in your gene list

# get the term name of the provided GO ID
term_obj = ont[MY_GO_ID]
term_name = term_obj.name
print("These genes have all been annotated with" , MY_GO_ID + ', "' + term_name + '" or any of its child terms' )

all_children={}
all_children[MY_GO_ID] = term_name

# add all children of the parent term to dictionary
for child in ont[MY_GO_ID].rchildren():
  all_children[child.id] = child.name

for line in GO_GENES:
	line = line.strip()
	all_genes = {}
	if MY_GO_ID in line:
		if MY_GO_ID in all_children:
			all_genes[
			
