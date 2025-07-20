#! /usr/bin/env python3

import json
import json5
import jsonschema

with (open("src/data/rules-schema.json") as schema_fd,
      open("src/data/rules.json5") as data_fd):
    schema = json.load(schema_fd)
    data = json5.load(data_fd)

jsonschema.validate(instance=data, schema=schema)
