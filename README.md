# Cereal

Cereal is a commandline tool that converts between different serialization
formats. It currently uses the file extensions of the input and output files
to guess the format. Recognized file formats include: JSON, YAML and TOML.

## Supported conversions

|           | to JSON | to YAML | to TOML |
|:---------:|:-------:|:-------:|:-------:|
| from JSON |    y    |    y    |    y    |
| from YAML |    y    |    y    |    y    |
| from TOML |    y    |    y    |    y    |

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