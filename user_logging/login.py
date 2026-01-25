import requests


class Login():
    def __init__(self, username, password, url="https://dm2-me.informaticacloud.com/ma/api/v2/user/login"):
        self.username = username
        self.password = password

        self.body = {"username": self.username,
                    "password": self.password
                    }
        
        self.url = url
        
    def user_login(self):
        response = requests.post(url=self.url, json=self.body)

        if response.status_code == 200:
            sessionId = response.json().get("icSessionId")
            return sessionId
        else:
            print("Failed to login", response.text)