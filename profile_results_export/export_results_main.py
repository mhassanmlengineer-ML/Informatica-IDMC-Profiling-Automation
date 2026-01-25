from user_logging.login import Login
from profile_list.profile_list import ProfileList
from profile_results_export.profile_result_export import ProfileResultExport
from configuration_manager.configuration_manager import ConfigurationManager


def export_results():
    config_mngr = ConfigurationManager()

    username = config_mngr.username
    password = config_mngr.password
    folder_id = config_mngr.folder_id
    export_results_folder = config_mngr.output_results_folder

    my_login = Login(username=username, password=password)

    session_id = my_login.user_login()

    profile_list = ProfileList(session_id=session_id)

    profiles = profile_list.get_profiles()
    profile_data = []

    for profile in profiles:
        if profile.get("frsFolderId") is not None and profile["frsFolderId"] == folder_id:
            profile_data.append({"name": profile["name"], "id": profile["id"]})
        else:
            continue

    profile_result_export = ProfileResultExport(session_id=session_id)

    for profile in profile_data:
        profile_result_export.export_result(profile_id=profile["id"],
                                            output_file_path=f"""{export_results_folder}{profile["name"]}.xlsx""")


if __name__ == "__main__":
    export_results()