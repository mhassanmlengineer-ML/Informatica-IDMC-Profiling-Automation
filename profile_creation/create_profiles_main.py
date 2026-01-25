from user_login.login import Login
from profile_creation.connection_objects_retriever import ConnectionObjectsRetriever
from profile_creation.object_fields_retriever import ObjectFieldsRetriever
from profile_creation.profile_creation import ProfileCreation
from configuration_manager.configuration_manager import ConfigurationManager
from profile_creation.connections_retriever import ConnectionsRetriever


def create_profiles_main():
    config_mngr = ConfigurationManager()

    connection_name = config_mngr.connection_name
    max_records = config_mngr.max_records
    username = config_mngr.username
    password = config_mngr.password
    project_id = config_mngr.project_id
    folder_id = config_mngr.folder_id
    org_id = config_mngr.org_id
    data_source_type = config_mngr.data_source_type
    source_path = config_mngr.source_path

    my_login = Login(username=username, password=password)

    session_id = my_login.user_login()

    connections_retrvr = ConnectionsRetriever(session_id=session_id)

    connection_id = connections_retrvr.get_connection_id(connection_name)

    retrieve_objects = ConnectionObjectsRetriever(session_id=session_id, connection_name=connection_name, max_records=max_records)
    objects = retrieve_objects.get_objects()

    fields_object = ObjectFieldsRetriever(session_id=session_id, connection_name=connection_name)

    for object in objects:
        table_name = object["name"]

        fields = fields_object.get_fields(table_name)

        profile_creation_instance = ProfileCreation(session_id=session_id, project_id=project_id,
                                                    folder_id=folder_id, org_id=org_id, connection_id=connection_id)

        fields_metadata = [
                {
                    "name": f["name"],
                    "type": f["type"],
                    "precision": f["precision"],
                    "scale": f["scale"],
                    "pcType": f["pcType"]
                }
                for f in fields
                if f["type"].upper() in profile_creation_instance.SUPPORTED_TYPES
            ]
        
        profile_creation_instance.create_profile(data_source_type=data_source_type, table_name=table_name,
                                                fields_metadata=fields_metadata, source_path=source_path)
    
if __name__ == "__main__":
    create_profiles_main()