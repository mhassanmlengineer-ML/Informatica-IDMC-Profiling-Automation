import requests


class ObjectFieldsRetriever():
    def __init__(self, session_id, connection_name, url=f"https://mec2.dm2-me.informaticacloud.com/saas/api/v2/connection/source/name"):
        self.session_id = session_id
        self.connection_name = connection_name
        self.base_url = url + '/' + self.connection_name + '/field/'
        self.headers = {
                        "icSessionId": self.session_id
                    }

    def get_fields(self, object):
        response = requests.get(url=self.base_url + object, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve fields", response.text)

            