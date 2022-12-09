import json
from gendiff.generate_diff import generate_diff


def test_generate_diff():
    filepath1 = "/Users/gromov/Projects/python-project-50/gendiff/tests/fixtures/file1_for_test.json"
    filepath2 = "/Users/gromov/Projects/python-project-50/gendiff/tests/fixtures/file1_for_test.json"
    with open("/Users/gromov/Projects/python-project-50/gendiff/tests/fixtures/result_for_test.txt") as f:
        assert generate_diff(filepath1, filepath2) == f.read()