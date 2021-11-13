import json, os


def load_settings():
    abs_file_path = os.path.abspath(__file__)
    path, _ = os.path.split(abs_file_path)
    settings_path = os.path.join(path, 'settings.json')
    with open(settings_path, 'r') as f:
        print(f.readlines())
        