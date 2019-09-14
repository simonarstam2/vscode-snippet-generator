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
### Example one
Using snippet-generator on test.txt, and redirecting the output to out.txt with the parameters name set to "test test" and desc set to "nice". Check below to see the input file, and also the result of the output file.

```sh
python snippet-generator.py test.txt --name test test --desc nice > out.txt
```

test.txt
```js
import React from 'react';

export interface Props {
  name: string;
}

export class Hello extends React.Component<Props> {
  constructor(props: Props) {
    super(props);
  }

  render() {
    return (
      <View style={styles.root}>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  root: {
    alignItems: 'center',
    alignSelf: 'center',
  }
});
```
out.txt
```json
{
  "test test": {
    "prefix": [ "unspecified" ],
    "body": [
      "import React from 'react';",
      "",
      "export interface Props {",
      "  name: string;",
      "}",
      "",
      "export class Hello extends React.Component<Props> {",
      "  constructor(props: Props) {",
      "    super(props);",
      "  }",
      "",
      "  render() {",
      "    return (",
      "      <View style={styles.root}>",
      "      </View>",
      "    );",
      "  }",
      "}",
      "",
      "const styles = StyleSheet.create({",
      "  root: {",
      "    alignItems: 'center',",
      "    alignSelf: 'center',",
      "  }",
      "});"
    ],
    "description": "nice"
  }
}

```
