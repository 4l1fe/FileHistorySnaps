import logging

from inotify_simple import INotify, flags, masks


EVENTS = (flags.CREATE 
          | flags.DELETE
          | flags.MODIFY
          | flags.DELETE_SELF
          | flags.MOVE_SELF
          | flags.MOVE_FROM
          | flags.MOVE_TO)


class Listener:

    def __init__(self, watching_dir, events=EVENTS):
        self.inotify = INotify()
        self.watching_dir = watching_dir
        self.events = events

    def start_listening(self):
        self.wd = self.inotify.add_watch(self.watching_dir, self.events)

    def stop_listening(self):
        self.inotify.rm_watch(self.wd)

    def has_events(self):
        """Events have to be read to emptify a queue"""
        
        _has_events = False
        for event in self.inotify.read():
            logging.debug('Events: %s', event)
            _has_events = True

        logging.info('Has events: %s', _has_events)
        return _has_events
