from importlib.metadata import version as _version

def main() -> None:
    __version__ = _version("mygpt")
    print(f"Hello from mygpt!. You are currently using the version, {__version__}")
