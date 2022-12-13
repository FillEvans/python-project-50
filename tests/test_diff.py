import pytest
from gendiff.generate_diff import get_diff


json1 = "tests/fixtures/file1_for_test.json"
json2 = "tests/fixtures/file2_for_test.json"
expected1 = "tests/fixtures/result"
json3 = "tests/fixtures/file1.json"
json4 = "tests/fixtures/file2.json"
expected2 = "tests/fixtures/result2"
yml1 = "tests/fixtures/file1.yml"
yml2 = "tests/fixtures/file2.yml"
yml3 = "tests/fixtures/file1_for_test.yaml"
yml4 = "tests/fixtures/file2_for_test.yaml"

@pytest.mark.parametrize('path1, path2, expected', [
    (json1, json2, expected1),
    (json3, json4, expected2),
    (yml1, yml2, expected1),
    (yml3, yml4, expected2),
])
def test_diff(path1, path2, expected):
    with open(expected) as f:
        assert get_diff(path1, path2) == f.read()
