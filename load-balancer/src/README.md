# AI Docs
BPI Docs Repo

## Setup

### Setting up Python part

+ Create virtual env
+ Execute `pip install -r requirements.txt`


### Setting up Node part

+ Execute `npm install`

## Automated Service
This will run the python command, also it will execute node command, pandoc, and copy rst files into dev-guide. It will also do minor cleanup.
```javascript
# Virtualenv should be active
python automate_process.py
```

## HOWTO

### Using raml_parser.py

```javascript
python raml_parser.py
```

### Using raml_parser.js

```javascript
node raml_parser.js <raml_path> <markdown_path_to_save_to>
```


## Conversions
### To create RST formatted document(s) from MarkDown or HTMl, you are required to install Pandoc to your system.

MACOSX:
```
brew install pandoc
```

Linux:
```
apt-get install pandoc
```

Conversion command:
```
pandoc --from=<> --to=<> --output=<> <input  file>
```
