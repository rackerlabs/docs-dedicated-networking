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

### Automated Service
Executing the command below will recursively search for RAML documents based on the path provided as the second argument. This will convert to MD and finally to RST format. The files are created in the same directory where the RAML file is located.
```javascript
# Virtualenv should be active
python automate.py <full-path>

# Example:
## Relative path
# python automate.py ../.
## Full path
# python automate.py /temp/docs/
```


