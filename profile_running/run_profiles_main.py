from user_logging.login import Login
from profile_list.profile_list import ProfileList
from profile_running.profile_running import ProfileRunning
from configuration_manager.configuration_manager import ConfigurationManager


def run_profiles_main():
    config_mngr = ConfigurationManager()

    username = config_mngr.username
    password = config_mngr.password
    folder_id = config_mngr.folder_id

    my_login = Login(username=username, password=password)

    session_id = my_login.user_login()

    profile_list = ProfileList(session_id=session_id)

    profiles = profile_list.get_profiles()

    profiles_id_under_folder = []

    for profile in profiles:
        if profile.get("frsFolderId") is not None and profile["frsFolderId"] == folder_id:
            profiles_id_under_folder.append(profile["id"])

    profile_run = ProfileRunning(session_id=session_id)

    for profile_id in profiles_id_under_folder:
        profile_run.run_profile(profile_id=profile_id)

if __name__ == "__main__":
    run_profiles_main()
    