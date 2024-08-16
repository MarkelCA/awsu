# awsu
AWS Utilities. An extensible aws-sdk wrapper built for custom features.
## Install
### Requirements
- [git](https://git-scm.com/)
- [pip](https://pypi.org/project/pip/)
```bash
git clone git@github.com:MarkelCA/awsu.git
cd awsu
pip install .
# This will enable tab completion for the current session. Add it to your .bashrc or .zshrc to make it permanent:
eval "$(register-python-argcomplete awsu)" 
```
## Usage
```
$ awsu
usage: awsu [-h] {ec2,s3,configure} ...

AWS Utilities. An extensible aws wrapper built for custom features.

positional arguments:
  {ec2,s3,configure}  Commands
    ec2               EC2 Service Utilities
    s3                S3 Service Utilities
    configure         Configure awsu CLI options.

options:
  -h, --help          show this help message and exit

Text at the bottom of help
```

## Development
Create and activate the virtual environment:

```bash
git clone git@github.com:MarkelCA/awsu.git
cd awsu
python3 -m venv .venv
source .venv/bin/activate
```
