import requests

class ConnectionsRetriever():
    def __init__(self, session_id, url="https://mec2.dm2-me.informaticacloud.com/saas/api/v2/connection"):
        self.session_id = session_id
        self.url = url
        self.headers = {
                        "icSessionId": session_id,
                        }

    def get_connections(self):
        try:
            response = requests.get(url=self.url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Failed to retrieve connections:", e)
            return []

    
    def get_connection_id(self, connection_name):
        connections = self.get_connections()
        
        for connection in connections:
            if connection.get("name") == connection_name:
                return connection.get("federatedId")
        
        print(f"Connection '{connection_name}' not found.")
        return None
