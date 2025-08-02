#! /usr/bin/env python3

import json
import os
import sys
import tomllib

import jsonschema

mydir = os.path.dirname(sys.argv[0])

with (open(os.path.join(mydir, "rules-schema.json")) as schema_fd,
      open(os.path.join(mydir, "rules.toml"), "rb") as data_fd):
    schema = json.load(schema_fd)
    data = tomllib.load(data_fd)

jsonschema.validate(instance=data, schema=schema)
