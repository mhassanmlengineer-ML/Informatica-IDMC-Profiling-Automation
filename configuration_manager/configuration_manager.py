import yaml
import os

class ConfigurationManager:
    def __init__(self, config_path: str = None):
        self.config_path = config_path or os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config.yml"
        )
        self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self):
        keys = ["connection_name", "project_id", "folder_id", "org_id"]
        info = {k: getattr(self, k) for k in keys if hasattr(self, k)}
        return f"ConfigManager({info})"
