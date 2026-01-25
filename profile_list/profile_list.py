import requests


class ProfileList():
    def __init__(self, session_id, url = "https://mec2-dqprofile.dm2-me.informaticacloud.com/profiling-service/api/v1/profile"):
        self.session_id = session_id
        self.url = url

        self.headers = {"IDS-SESSION-ID": session_id}

    def get_profiles(self):
        response = requests.get(url=self.url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Request failed:", response.text)
            return None