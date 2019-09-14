#!/usr/bin/env python3
#
# Convert files between different serialization formats, i.e.
# YAML to JSON, JSON to YAML, etc.
#

import argparse
import json
import yaml
import toml
from os.path import splitext

__program__ = "cereal"
__version__ = "1.0.0"

readers = {
  ".json": json.load,
  ".yaml": yaml.safe_load,
  ".yml": yaml.safe_load,
  ".toml": toml.load
}

writers = {
  ".json": lambda d, f: json.dump(d, f, indent=2),
  ".yaml": yaml.safe_dump,
  ".yml": yaml.safe_dump,
  ".toml": toml.dump
}

def options():
  recognizedFormats = ", ".join(readers.keys())

  parser = argparse.ArgumentParser(description="Converts files between different serialization formats. Uses the file extensions of the input and output files to guess the format. Recognized extensions are: {}.".format(recognizedFormats),
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                   prog=__program__)
  parser.add_argument("input", type=argparse.FileType("r"), help="input file to read serialized data from")
  parser.add_argument("output", type=argparse.FileType("w"), help="output file to write serialized data to")
  parser.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))

  return parser.parse_args()

def convert(ifile, ofile):
  _, iext = splitext(ifile.name)
  _, oext = splitext(ofile.name)

  reader = readers[iext]
  writer = writers[oext]
  writer(reader(ifile), ofile)

def main():
  opts = options()
  convert(opts.input, opts.output)

if __name__ == "__main__":
  main()
