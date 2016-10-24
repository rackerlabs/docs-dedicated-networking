# AI Docs
BPI Docs Repo

## Executing the automated command

### Prerequisites
Make sure you activate a VirtualEnv. If pip install -r has not been executed on requirements.txt file we need to create a new VirtualEnv and execute pip command.

```javascript
# Create VirtualEnv
virtualenv --no-site-packages docenv

# Activate the environment
source docenv/bin/activate

# Load required packages
pip install -r requirements.txt --trusted-host 10.10.161.9
```

#### RST Conversion
To create RST formatted document(s) from MarkDown or HTMl, you are required to install Pandoc on your system.

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

#### RAML2HTML Conversion
To create Html from RAML documentation, you need to have two things:

1. nodejs installed locally
1. raml2html installed globally.
	# npm install -g raml2html; You might have to sudo , depending on your user privilege.

### Automated Service
Executing the command below will recursively search for RAML documents based on the path provided as the second argument. This will convert to MD and finally to RST format. The files are created in the same directory where the RAML file is located. 

I have now introduced the raml to html convertion step as well as part of the automated process.

```javascript
# Virtualenv should be active
python automate.py <full-path>

# Example:
## Relative path
# python automate.py ../.
## Full path
# python automate.py /temp/docs/
```


