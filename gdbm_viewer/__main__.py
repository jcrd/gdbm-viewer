import argparse

from gdbm_viewer.db import DB
from gdbm_viewer.ui import UI


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to gdbm file")
    parser.add_argument(
        "--max", nargs="?", type=int, default=25, help="Maximum lines per column"
    )

    args = parser.parse_args()

    ui = UI(args.max)
    DB(args.path, ui.set)
    ui.mainloop()


if __name__ == "__main__":
    main()
