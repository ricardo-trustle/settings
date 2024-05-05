# App Settings

Python YAML configuration with environment variables and hierarchical configurations.

- Configuration in YAML format
- Use different configurations for dev, staging, prod, etc
- Have a common setting defined in single file
- Configuration validation with `pydantic`
- Environments variables can override the settings in the config files
- Possibility of reading an environment file in dot env format

## Run the example:

```sh
poetry shell

PYTHONPATH=$PYTHONPATH:. python app/main.py --help                               
# Usage: main.py [OPTIONS]

# Options:
#   -e, --env PATH
#   -c, --config TEXT
#   --help             Show this message and exit.

PYTHONPATH=$PYTHONPATH:. python app/main.py                                        
# ==> my-cluster
# ==> aws
# ==> us-east-1
# ==> vpc-123456
# ==> ['subnet-123456']
# ==> dotenv_name
# ==> localhost
# ==> dotenv_root
# ==> dotenv_pass1234
# ==> 5432
# ==> disable

PYTHONPATH=$PYTHONPATH:. python app/main.py --env ./env-template                   
# ==> my-cluster
# ==> aws
# ==> us-east-1
# ==> vpc-123456
# ==> ['subnet-123456']
# ==> templ_name
# ==> localhost
# ==> templ_user
# ==> templ_pass
# ==> 5432
# ==> disable

PYTHONPATH=$PYTHONPATH:. python app/main.py --config prod.yaml 
# ==> prod-cluster
# ==> aws
# ==> us-east-1
# ==> vpc-456789
# ==> ['subnet-456789']
# ==> dotenv_name
# ==> dotenv_localhost
# ==> dotenv_root
# ==> dotenv_pass1234
# ==> 5432
# ==> require

PYTHONPATH=$PYTHONPATH:. python app/main.py --env ./env-template --config prod.yaml
# ==> prod-cluster
# ==> aws
# ==> us-east-1
# ==> vpc-456789
# ==> ['subnet-456789']
# ==> templ_name
# ==> templ_host
# ==> templ_user
# ==> templ_pass
# ==> 5432
# ==> require

pytest -v -s
# ===================================================================== test session starts ======================================================================
# platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0 -- /home/leal/.cache/pypoetry/virtualenvs/settings-Mc-3974F-py3.12/bin/python
# cachedir: .pytest_cache
# rootdir: /home/leal/git-work/settings
# configfile: pyproject.toml
# collected 7 items                                                                                                                                              

# tests/test_settings.py::test_default_settings PASSED
# tests/test_settings.py::test_local_settings PASSED
# tests/test_settings.py::test_staging_settings PASSED
# tests/test_settings.py::test_prod_settings PASSED
# tests/test_settings.py::test_invalid_settings PASSED
# tests/test_settings.py::test_prod_settings_with_env[True] PASSED
# tests/test_settings.py::test_prod_settings_with_env[False] PASSED

# ====================================================================== 7 passed in 0.17s =======================================================================

```

## Useful:

- JSON to Pydantic Converter: https://jsontopydantic.com/
