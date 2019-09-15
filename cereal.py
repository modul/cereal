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
from sys import exit
from typing import Callable, IO, NamedTuple

__program__ = "cereal"
__version__ = "1.0.0"

Filename = str
Intermediate = dict
Reader = Callable[[IO], Intermediate]
Writer = Callable[[IO, Intermediate], None]

class Converter(NamedTuple):
  load: Reader
  dump: Writer

def guessConverter(fn: Filename) -> Converter:
  _, ext = splitext(fn)
  fmt = extensions[ext]
  return converters[fmt]

def outputFilename(fn: Filename, fmt: str) -> Filename:
  name, _ = splitext(fn)
  return f"{name}.{fmt.lower()}"

converters = {
  "JSON" : Converter(json.load, lambda d, f: json.dump(d, f, indent=2)),
  "YAML" : Converter(yaml.safe_load, yaml.safe_dump),
  "TOML" : Converter(toml.load, toml.dump),
  "guess": None
}

extensions = {
  ".json": "JSON",
  ".yaml": "YAML",
  ".yml" : "YAML",
  ".toml": "TOML",
}

def options():
  recExtensions = ", ".join(extensions.keys())

  parser = argparse.ArgumentParser(description=(
                                    "Converts files between different serialization formats. "
                                    "Uses the file extensions of the input and output files to guess the format if not specified. "
                                    f"Recognized extensions are: {recExtensions}."),
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                   prog=__program__)
  parser.add_argument("input", type=argparse.FileType("r"), help="input file to read serialized data from")
  parser.add_argument("--output", "-o", help="output file path to write serialized data to", default=None)
  parser.add_argument("--from", "-f", dest="ifmt", default="guess", choices=converters.keys(),
                      help="input file format")
  parser.add_argument("--to", "-t", dest="ofmt", default="guess", choices=converters.keys(),
                      help="output file format")
  parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

  return parser.parse_args()

def convert(ifile: IO, ofile: IO, iconv: Converter, oconv: Converter):
  reader = iconv.load
  writer = oconv.dump
  writer(reader(ifile), ofile)

def main():
  opts = options()

  if opts.ofmt == "guess" and not opts.output:
    print("Cannot guess output format from empty output file name.")
    exit(1)

  iconv = converters[opts.ifmt] or guessConverter(opts.input.name)
  oconv = converters[opts.ofmt] or guessConverter(opts.output)
  output = opts.output or outputFilename(opts.input.name, opts.ofmt)

  with open(output, "w") as out:
    convert(opts.input, out, iconv, oconv)

if __name__ == "__main__":
  main()
