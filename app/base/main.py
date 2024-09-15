import sys
import argparse

from app.base.config import config


def main(argv=None):
    load_args(argv)


def load_args(argv=None):
    if not argv:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "-c",
        "--config_file",
        help="An integer will be increased by 1 and printed.",
        type=str,
    )
    args = parser.parse_args()

    if args.config_file:
        config.parse_config(args.config_file)
