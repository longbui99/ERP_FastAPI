import os
import sys
import logging
import argparse

from app.base.config import config

_logger = logging.getLogger(__name__)

def main(argv=None):
    load_args()

def load_args():
    if os.environ.get('SERVER_CONFIG_PATH'):
        config.parse_config(os.environ.get('SERVER_CONFIG_PATH'))
