import requests


class ProfileCreation():
    def __init__(self, session_id, project_id, folder_id, org_id, connection_id, url="https://mec2-dqprofile.dm2-me.informaticacloud.com/profiling-service/api/v1/profile"):
        self.session_id = session_id
        self.url = url
        self.project_id = project_id
        self.folder_id = folder_id
        self.org_id = org_id
        self.connection_id = connection_id

        self.headers = {
                        "IDS-SESSION-ID": session_id,
                        }
        
        self.SUPPORTED_TYPES = ["CHAR", "INTEGER", "DECIMAL", "DATE", "BOOLEAN", "FLOAT", "DOUBLE", "TIMESTAMP", "NVARCHAR", "NTEXT"]

    def create_profile(self, table_name, fields_metadata, data_source_type, source_path):
        source_fields = []
        profileable_fields = []

        for idx, field in enumerate(fields_metadata, start=1):
            source_fields.append({
                "name": field["name"],
                "dataType": field["type"],
                "precision": field["precision"],
                "pcType": field["pcType"],
                "order": idx,
                "isDeleted": False,
                "isMetadataUpdated": False,
                "scale": field["scale"]
            })

            profileable_fields.append({
                "sourceName": table_name,
                "fieldName": field["name"],
                "precision": field["precision"],
                "fieldType": "DATASOURCEFIELD",
                "scale": field["scale"]
            })

        payload = {
            "name": f"profile_{table_name}",
            "orgId": self.org_id,
            "description": f"profile_{table_name}",
            "frsProjectId": self.project_id,
            "frsFolderId": self.folder_id,
            "connectionId": self.connection_id,
            "source": {
                "name": table_name,
                "fields": source_fields,
                "dataSourceType": data_source_type,
                "properties": {
                    "dataSourceType": data_source_type,
                    "sourcePath": source_path
                },
                "sourceType": "DATASOURCE"
            },
            "profileableFields": profileable_fields,
            "samplingOptions": {
                "id": None,
                "rows": -1,
                "samplingType": "ALL_ROWS"
            },
            "drillDownType": "ON",
            "profileType": "COLUMN_PROFILE"
        }

        response = requests.post(url=self.url, headers=self.headers, json=payload)

        if response.status_code in (200, 201):
            print(f"Profiling created for table: {table_name}")

            if response.text and response.text.strip():
                try:
                    return response.json()
                except ValueError:
                    return {"message": response.text}
            else:
                return {"message": "Profile created successfully (empty response body)"}
        else:
            print(f"Failed for {table_name}: {response.text}")
            return None