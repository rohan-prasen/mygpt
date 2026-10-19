from importlib.metadata import version as _version
from importlib.metadata import PackageNotFoundError

def main() -> None:
    try:
        __version__ = _version("mygpt")
    except PackageNotFoundError:
        __version__ = "0.0.0+source"

    print(f"Hello from mygpt!. You are currently using the version, {__version__}")
