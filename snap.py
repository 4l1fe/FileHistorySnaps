import logging
from datetime import datetime
from pathlib import Path

import btrfsutil

from constants import TIMEOUT


class Snapper:

    def __init__(self, watching_dir, timeout=TIMEOUT):
        self.watching_dir = watching_dir
        self.prev_snap_datetime = Snapper._read_prev_snap_datetime(watching_dir)
        self.timeout = timeout 

    def snap_it(self, source, path, read_only=True):
        if not self._can_snap():
            return
            
        logging.info('Snap the watching dir as %s', path)
        s = btrfsutil.create_snapshot(source, path, read_only=read_only)
        
    def _can_snap(self):
        pass

    @staticmethod
    def _read_prev_snap_datetime(watching_dir):
        p = Path(watching_dir)
        if not p.exists():
            return None

        #TODO sort snap by desc time-name 
        for prev_snap in p.iterdir():
            dt = Snapper._extract_iso_datetime(prev_snap.name)
            return dt

    def _extract_iso_datetime(self, snap_name):
        return datetime.now()
