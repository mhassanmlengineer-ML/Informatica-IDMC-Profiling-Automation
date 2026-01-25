import requests

class ConnectionObjectsRetriever():
    def __init__(self, session_id, connection_name, max_records, url="https://mec2.dm2-me.informaticacloud.com/saas/api/v2/connection/source/name"):
        self.session_id = session_id
        self.connection_name = connection_name
        self.url = url + '/' + self.connection_name
        self.max_records = max_records

        self.headers = {
                        "icSessionId": self.session_id
                    }
        
        self.params = {"maxRecordsCount": self.max_records}


    def get_objects(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)

        if response.status_code == 200:
            return response.json()
        
        else:
            print("Failed to retrieve objects", response.text)

