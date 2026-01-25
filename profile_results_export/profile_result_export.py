import requests


class ProfileResultExport():
    def __init__(self, session_id, url = "https://mec2-dqprofile.dm2-me.informaticacloud.com/metric-store/api/v1/Profiles('"):
        self.session_id = session_id
        self.url = url

        self.headers = {"IDS-SESSION-ID": session_id}

    def export_result(self, profile_id, output_file_path, run_key=1, range="ALL_COLUMNS", fileFormat="EXCEL",):
        query_params = {
                        "runKey": run_key,
                        "range": "ALL_COLUMNS",
                        "fileFormat": "EXCEL"
                            }
        
        response = requests.get(url=self.url + profile_id + "')/Export", headers=self.headers, params=query_params, stream=True)

        if response.status_code == 200:
            with open(output_file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print(f"Export file saved as: {output_file_path}")
        else:
            print("Export failed")
            print("Status:", response.status_code)
            print("Response:", response.text)