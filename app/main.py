from pprint import pprint
import logging
from settings.parse import settings, DEFAULT_CONFIG
from settings.env import load_envvars_file
from pathlib import Path
import click


@click.command()
@click.option(
    "-e",
    "--env",
    type=click.Path(
        exists=True,
        file_okay=True,
        readable=True,
        path_type=Path,
    ),
    default=Path(".env"),
)
@click.option(
    "-c",
    "--config",
    type=click.STRING,
    default=DEFAULT_CONFIG,
)
def run(env, config) -> None:
    log = logging.getLogger(__name__)

    load_envvars_file(env)

    base_config = settings(log, config)

    print("==>", base_config.cluster.name)
    print("==>", base_config.cluster.cloud)
    print("==>", base_config.cluster.region)
    print("==>", base_config.cluster.vpc_id)
    print("==>", base_config.cluster.subnet_ids)

    print("==>", base_config.database.name)
    print("==>", base_config.database.host)
    print("==>", base_config.database.username)
    print("==>", base_config.database.password)
    print("==>", base_config.database.port)
    print("==>", base_config.database.sslmode)


if __name__ == "__main__":
    run()
