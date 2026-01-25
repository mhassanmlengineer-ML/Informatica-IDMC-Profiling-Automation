import requests

class ProfileRunning():
    def __init__(self, session_id, url="https://mec2-dqprofile.dm2-me.informaticacloud.com/profiling-service/api/v1/profile/"):
        self.session_id = session_id
        self.url = url

        self.headers = {"IDS-SESSION-ID": self.session_id}

    def run_profile(self, profile_id):
        url = self.url + profile_id + '/execute'
        response = requests.post(url=url, headers=self.headers)

        if response.status_code == 200:
            print("Profile run started for id:", id)
        else:
            print("Run failed:", response.text)
            return None