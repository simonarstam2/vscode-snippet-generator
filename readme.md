# vscode-snippet-generator

# Cloning the project
```
git clone https://github.com/simonarstamtesting2/vscode-snippet-generator.git
```

## Running the script
```sh
python snippet-generator.py test.txt
```

### Redirect output to file
```sh
python snippet-generator.py test.txt > out.py
``` 
\- out.py is the output file.

## Arguments
| Option | Type | Default | Description | 
| ------ | ---- | ------- | ----------- |
| --name | str  | Snippet Name | The name of the snippet |
| --prefix | str | unspecified | The snippet prefix, e.g. vtest. Support for multiple prefixes, seperated by a space. |
| --desc | str | unspecified | The description of the snippet.|

## Examples
```sh
python snippet-generator.py test.txt --name test test --desc nice > out.txt
```