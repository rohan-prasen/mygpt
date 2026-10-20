from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("mygpt")

except PackageNotFoundError:
    __version__ = "0.0.0+source"


def main() -> None:

    print(f"Hello from mygpt! You are currently using version {__version__}.")
