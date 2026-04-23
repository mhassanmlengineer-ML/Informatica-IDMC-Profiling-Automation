import requests

class ConnectionCreator():
    def __init__(self, session_id, url="https://mec2.dm2-me.informaticacloud.com/saas/api/v2/connection"):
        self.session_id = session_id
        self.url = url

        self.header = {"icSessionId": self.session_id}


    def create_connection(self, body):
        response = requests.post(url=self.url, headers=self.header, json=body)

        if response.status_code == 200:
            print("Created Connection: ",  )
        else:
            print("Failed to login", response.text)
