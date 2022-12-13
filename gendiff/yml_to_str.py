import yaml


def get_yml_to_str(filepath):
    return yaml.safe_load(open(filepath))