"""Shows a basic text dialog.
"""

import sys

sys.path.append("..")
from agpy.ui import *
from agpy.window import *
from agpy.utils import *

sys.path.remove("..")


def main():
    show_window("Dialog test.")
    dlg("Hi!")
    dlg("Test again!")
    quit()


if __name__ == "__main__":
    main()
