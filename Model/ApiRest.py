import requests


class API:
    
    json_client = None
    response = None
    URL = {
        "clarion": "http://200.66.88.166:5010/clarion"
    }
    HEADERS = {"X-API-KEY" : "17d6a5fdd4e94e251238b42e1e8dd5c7dcb8c8702b43ece2b9f630f6b92e3b2f"}

    def handle_response(self, url):
        try:
            response = requests.post(self.URL[url], json=self.json_client, headers=self.HEADERS)
            if response.status_code == 200:
                self.response = response.json()
            else:
                self.response = response.status_code
        except BaseException as e:
            self.response = e
            return e

    def get(self, url):
        try:
            response = requests.get(self.URL[url], headers=self.HEADERS)
            if response.status_code == 200:
                self.response = response.json()
            else:
                self.response = response.status_code
        except BaseException as e:
            self.response = e
            return e
    
    def get_json_client(self):
        return self.json_client

    def set_json_client(self, value):
        self.json_client = value

    def get_response(self):
        return self.response

    def set_response(self, value):
        self.response = value