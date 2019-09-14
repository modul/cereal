# Cereal

Cereal is a commandline tool that converts between different
data-serialization and similar formats.

The input and output file formats can be set explicitly via commandline
flags. If that's not the case, cereal will try to guess the file format from
the file extension.

## Supported conversions

|           | to JSON  | to YAML  | to TOML  |
|:---------:|:--------:|:--------:|:--------:|
| from JSON |   :+1:   |   :+1:   |   :+1:   |
| from YAML |   :+1:   |   :+1:   |   :+1:   |
| from TOML |   :+1:   |   :+1:   |   :+1:   |

## Usage

```
cereal [-h] [--version] input output

positional arguments:
  input       input file to read serialized data from
  output      output file to write serialized data to

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```