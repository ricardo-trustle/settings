# App Settings

Python YAML configuration with environment variables and hierarchical configurations


## Run the example:

```sh

poetry shell

export $(cat .env | grep -v "#" | xargs -L 1)

PYTHONPATH=$PYTHONPATH:. python app/main.py
# ==> my-cluster
# ==> aws
# ==> us-east-1
# ==> vpc-123456
# ==> ['subnet-123456']
# ==> postgres
# ==> staging.example.com
# ==> root
# ==> pass1234
# ==> 5432
# ==> require

pytest -v                                  
# ===================================================================== test session starts ======================================================================
# platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0 -- /home/leal/.cache/pypoetry/virtualenvs/settings-Mc-3974F-py3.12/bin/python
# cachedir: .pytest_cache
# rootdir: /home/leal/git-work/settings
# configfile: pyproject.toml
# collected 4 items                                                                                                                                              

# tests/test_settings.py::test_default_settings PASSED                                                                                                     [ 25%]
# tests/test_settings.py::test_local_settings PASSED                                                                                                       [ 50%]
# tests/test_settings.py::test_staging_settings PASSED                                                                                                     [ 75%]
# tests/test_settings.py::test_prod_settings PASSED                                                                                                        [100%]

# ====================================================================== 4 passed in 0.04s =======================================================================

```