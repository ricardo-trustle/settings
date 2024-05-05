from settings.parse import settings, DEFAULT_CONFIG
from settings.env import load_envvars_file
import pytest
import logging
from logging import Logger
import os, sys


@pytest.fixture
def logger() -> Logger:
    l = logging.getLogger("settings")
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(format)
    l.addHandler(handler)
    return l


@pytest.fixture
def env():
    def setEnv(set: bool) -> None:
        if set:
            os.environ["DB_NAME"] = "env_db"
            os.environ["DB_USER"] = "env_user"
            os.environ["DB_PASS"] = "env_pass"
            os.environ["DB_HOST"] = "env_host"
            os.environ["DB_PORT"] = "12345"
        else:
            os.environ.pop("DB_NAME", None)
            os.environ.pop("DB_USER", None)
            os.environ.pop("DB_PASS", None)
            os.environ.pop("DB_HOST", None)
            os.environ.pop("DB_PORT", None)

    return setEnv


def test_default_settings(logger: Logger, env) -> None:
    env(False)
    base_config = settings(logger, DEFAULT_CONFIG)
    assert base_config.database.name == "postgres"
    assert base_config.database.host == "localhost"
    assert base_config.database.username == "default_user"
    assert base_config.database.password == "default_pass1234"
    assert base_config.database.port == 5432
    assert base_config.database.sslmode == "disable"
    assert base_config.cluster.name == "my-cluster"
    assert base_config.cluster.cloud == "aws"
    assert base_config.cluster.region == "us-east-1"
    assert base_config.cluster.vpc_id == "vpc-123456"
    assert base_config.cluster.subnet_ids == ["subnet-123456"]


def test_local_settings(logger: Logger, env) -> None:
    env(True)
    base_config = settings(logger, "local.yaml")
    assert base_config.database.name == "env_db"
    assert base_config.database.host == "localhost"
    assert base_config.database.username == "env_user"
    assert base_config.database.password == "env_pass"
    assert base_config.database.port == 5432
    assert base_config.database.sslmode == "disable"
    assert base_config.cluster.name == "my-cluster"
    assert base_config.cluster.cloud == "aws"
    assert base_config.cluster.region == "us-east-1"
    assert base_config.cluster.vpc_id == "vpc-123456"
    assert base_config.cluster.subnet_ids == ["subnet-123456"]


def test_staging_settings(logger: Logger, env) -> None:
    env(True)
    base_config = settings(logger, "staging.yaml")
    assert base_config.database.name == "env_db"
    assert base_config.database.host == "staging.example.com"
    assert base_config.database.username == "env_user"
    assert base_config.database.password == "env_pass"
    assert base_config.database.port == 5432
    assert base_config.database.sslmode == "require"
    assert base_config.database.sslrootcert == "/etc/ssl/certs/ca-certificates.crt"
    assert base_config.cluster.name == "my-cluster"
    assert base_config.cluster.cloud == "aws"
    assert base_config.cluster.region == "us-east-1"
    assert base_config.cluster.vpc_id == "vpc-123456"
    assert base_config.cluster.subnet_ids == ["subnet-123456"]


def test_prod_settings(logger: Logger, env) -> None:
    env(True)
    base_config = settings(logger, "prod.yaml")
    assert base_config.database.name == "env_db"
    assert base_config.database.host == "env_host"
    assert base_config.database.username == "env_user"
    assert base_config.database.password == "env_pass"
    assert base_config.database.port == 5432
    assert base_config.database.sslmode == "require"
    assert base_config.database.sslrootcert == "/etc/ssl/certs/ca-certificates.crt"
    assert base_config.cluster.name == "prod-cluster"
    assert base_config.cluster.cloud == "aws"
    assert base_config.cluster.region == "us-east-1"
    assert base_config.cluster.vpc_id == "vpc-456789"
    assert base_config.cluster.subnet_ids == ["subnet-456789"]


def test_invalid_settings(logger: Logger, env) -> None:
    env(False)
    os.environ["ENV"] = "invalid"
    with pytest.raises(Exception):
        _ = settings(logger)


@pytest.mark.parametrize("use_env", [(True), (False)])
def test_prod_settings_with_env(logger: Logger, env, use_env) -> None:
    env(use_env)
    load_envvars_file("./env-template")
    base_config = settings(logger, "prod.yaml")
    assert base_config.database.name == "templ_name"
    assert base_config.database.host == "templ_host"
    assert base_config.database.username == "templ_user"
    assert base_config.database.password == "templ_pass"
    assert base_config.database.port == 5432
    assert base_config.database.sslmode == "require"
    assert base_config.database.sslrootcert == "/etc/ssl/certs/ca-certificates.crt"
    assert base_config.cluster.name == "prod-cluster"
    assert base_config.cluster.cloud == "aws"
    assert base_config.cluster.region == "us-east-1"
    assert base_config.cluster.vpc_id == "vpc-456789"
    assert base_config.cluster.subnet_ids == ["subnet-456789"]
