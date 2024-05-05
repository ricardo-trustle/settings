from dotenv import load_dotenv


def load_envvars_file(path: str) -> None:
    load_dotenv(path, verbose=True, override=True)
