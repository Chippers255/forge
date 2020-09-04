# Forge
A command-line tool to create prebuilt data science repositories from a template.

## Usage
``` bash
forge config.json
```

## Directory Structure
The following directory structure is modelled after my own method for organizing data science projects.

```
+-- LICENSE
+-- README.md
+-- requirements.txt
+-- data
|   +-- raw
|   +-- interim
|   +-- processed
|   +-- output
+-- src
|   +-- data
|   +-- processing
|   +-- models
|   +-- metrics
|   +-- utils
+-- notebooks
+-- models
+-- docs
+-- reports
|   +-- images
```