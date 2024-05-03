from pprint import pprint
import logging
from settings.parse import settings


def run() -> None:
    log = logging.getLogger(__name__)
    base_config = settings(log)

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
