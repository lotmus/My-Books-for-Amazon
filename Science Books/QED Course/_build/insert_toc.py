"""Static hyperlinked table of contents. Delegates to _finish_book."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _finish_book as fb


def main():
    fb.main()


if __name__ == "__main__":
    main()
