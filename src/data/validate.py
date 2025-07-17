#! /usr/bin/env python3

import json
import jsonschema

with (open("src/data/rules-schema.json") as schema_fd,
      open("src/data/rules.json") as data_fd):
    schema = json.load(schema_fd)
    data = json.load(data_fd)

jsonschema.validate(instance=data, schema=schema)
