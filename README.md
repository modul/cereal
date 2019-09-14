# Cereal

Cereal is a commandline tool that converts between different
data-serialization and similar formats.

## Supported conversions

|           | to JSON  | to YAML  | to TOML  |
|:---------:|:--------:|:--------:|:--------:|
| from JSON |   :+1:   |   :+1:   |   :+1:   |
| from YAML |   :+1:   |   :+1:   |   :+1:   |
| from TOML |   :+1:   |   :+1:   |   :+1:   |

## Usage

Input and output file formats can be set explicitly via commandline flags. If
that's not the case, cereal will try to guess the file format from the file
extension.

```
cereal [-h] [--output OUTPUT] [--from {JSON,YAML,TOML,guess}]
              [--to {JSON,YAML,TOML,guess}] [--version]
              input

positional arguments:
  input                 input file to read serialized data from

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        output file path to write serialized data to (default:
                        None)
  --from {JSON,YAML,TOML,guess}, -f {JSON,YAML,TOML,guess}
                        input file format (default: guess)
  --to {JSON,YAML,TOML,guess}, -t {JSON,YAML,TOML,guess}
                        output file format (default: guess)
  --version             show program's version number and exit
```