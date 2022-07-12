import logging
from time import sleep
from datetime import datetime
from argparse import ArgumentParser

import btrfs

from constants import TIMEOUT
from events import Listener
from snap import Snapper


def main(watching_dir, timeout):
    listener = Listener(watching_dir)
    snapper = Snapper(watching_dir, timeout=timeout)

    logging.info('Start listening to the events %s', watching_dir)
    listener.start_listening()
    while True:
        if not listener.has_events():
            continue

        snapper.snap_it(watching_dir)
        sleep(timeout)

    listener.stop_listening()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('watching-dir')
    parser.add_argument('--timeout', type=int, default=TIMEOUT)
    ns = parser.parse_args()

    logging.basicConfig(level='INFO', format='[%(asctime)s %(levelname)s] %(message)s')
    main(ns.watching_dir, ns.timeout)

