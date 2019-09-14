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

GetConverter = Callable[[Filename], Converter]

def guessFormat(fn: Filename) -> str:
  _, ext = splitext(fn)
  return extensions[ext]

def converter(typ):
  return converters[typ]

def constConverter(load: Reader, dump: Writer) -> GetConverter:
  return lambda _: Converter(load, dump)

def guessConverter() -> GetConverter:
  return lambda fn: converter(guessFormat(fn))(fn)

converters = {
  "JSON" : constConverter(json.load, lambda d, f: json.dump(d, f, indent=2)),
  "YAML" : constConverter(yaml.safe_load, yaml.safe_dump),
  "TOML" : constConverter(toml.load, toml.dump),
  "guess": guessConverter()
}

extensions = {
  ".json": "JSON",
  ".yaml": "YAML",
  ".yml" : "YAML",
  ".toml": "TOML",
}

def options():
  recExtensions = ", ".join(extensions.keys())

  parser = argparse.ArgumentParser(description="Converts files between different serialization formats. Uses the file extensions of the input and output files to guess the format if not specified. Recognized extensions are: {}.".format(recExtensions),
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                   prog=__program__)
  parser.add_argument("input", type=argparse.FileType("r"), help="input file to read serialized data from")
  parser.add_argument("output", type=argparse.FileType("w"), help="output file to write serialized data to")
  parser.add_argument("--from", "-f", dest="ifmt", default="guess", choices=converters.keys(),
                      help="input file format")
  parser.add_argument("--to", "-t", dest="ofmt", default="guess", choices=converters.keys(),
                      help="output file format")
  parser.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))

  args = parser.parse_args()

  args.iconv = converter(args.ifmt)
  args.oconv = converter(args.ofmt)
  return args

def main(ifile: IO, ofile: IO, iconv: GetConverter, oconv: GetConverter):
  reader = iconv(ifile.name).load
  writer = oconv(ofile.name).dump
  writer(reader(ifile), ofile)

if __name__ == "__main__":
  opts = options()
  main(opts.input, opts.output, opts.iconv, opts.oconv)
