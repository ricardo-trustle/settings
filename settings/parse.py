from pyaml_env import parse_config, BaseConfig
import os
from pprint import pprint
import logging
from logging import Logger
from .validation import valid

CONFIGS_DIR = "../configs"
DEFAULT_CONFIG = "local.yaml"
COMMON_FILE = os.path.join(CONFIGS_DIR, "common.yaml")


def settings(logger: Logger, cfg: str) -> BaseConfig:
    logger.info("Loading settings for environment: " + cfg)

    current_dir = os.path.dirname(os.path.realpath(__file__))

    config_common_path = os.path.join(current_dir, COMMON_FILE)
    config_common = parse_config(config_common_path)

    config_specific_path = os.path.join(current_dir, CONFIGS_DIR, cfg)
    if not os.path.exists(config_specific_path):
        logger.error("Configuration file does not exist: " + config_specific_path)
        raise Exception("Configuration file does not exist")
    config_specific = parse_config(config_specific_path)

    merge(config_common, config_specific)

    if not valid(config_common):
        logger.error("Invalid configuration: " + pprint.pformat(config_common))
        raise Exception("Invalid configuration")

    base_config = BaseConfig(config_common)
    return base_config


def merge(a: dict, b: dict, path=[]):
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a
