import re
import sys

PROJECT_NAME_REGEX = r'^[a-zA-Z][a-zA-Z]+$'

project_name = '{{cookiecutter.project_name.lower()}}'

if not re.match(PROJECT_NAME_REGEX, project_name):
    print(
        'ERROR: Invalid project name {} ([a-zA-Z] only)'.format(project_name))

    # Exit to cancel project
    sys.exit(1)


API_VERSION_REGEX = r'^[a-z0-9][a-z0-9]+$'

api_version = '{{cookiecutter.api_version}}'

if not re.match(API_VERSION_REGEX, api_version):
    print(
        'ERROR: Invalid api version {} ([a-z0-9] only)'.format(api_version))

    # Exit to cancel project
    sys.exit(1)
