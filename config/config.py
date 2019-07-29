import os


class Config(object):

    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.base_url = 'http://192.168.123.131:4000'
