if __name__ == '__main__':
    print("AlpacaEngine is not meant to be ran directly. Please import it into your project.")
    exit(0)

from src.Engine import Engine
from src.Window import Window

__all__ = ["Engine", "Window"]