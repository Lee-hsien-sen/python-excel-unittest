
import requests
import json


class RunMain(object):
    def get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method=None, data=None):
        res = None
        if method.lower()== 'GET':
            res = self.get(url, data)
        else:
            res = self.post(url, data)
        return res