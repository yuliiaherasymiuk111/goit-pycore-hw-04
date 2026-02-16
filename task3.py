import sys
from pathlib import Path

from colorama import Fore, Style, init


def show_tree(folder: Path, level=0):
    indent = "  " * level

    for item in folder.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            show_tree(item, level + 1)
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)

    if len(sys.argv) < 2:
        print("Please provide path to directory")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print("Path does not exist")
        return

    if not path.is_dir():
        print("Path is not a directory")
        return

    print(f"{Fore.YELLOW}{path.name}{Style.RESET_ALL}")
    show_tree(path)


if __name__ == "__main__":
    main()
