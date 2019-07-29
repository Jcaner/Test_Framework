import requests


class MyRequests(object):
    def __init__(self):
        self.s = None

    def login(self, url, playload, headers):
        self.s = requests.Session()
        r = self.s.post(url, json=playload, headers=headers)
        self.s.cookies = r.cookies
