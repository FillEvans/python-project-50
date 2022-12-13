import yaml


def get_yml_to_str(filepath):
    return yaml.safe_load(open(filepath))


print(get_yml_to_str("/Users/gromov/Projects/python-project-50/tests/fixtures/file1_for_test.yaml"))