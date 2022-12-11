import pytest
from gendiff.generate_diff import get_diff


json1 = "fixtures/file1_for_test.json"
json2 = "fixtures/file2_for_test.json"
expected1 = "fixtures/result"
json3 = "fixtures/file1.json"
json4 = "fixtures/file2.json"
expected2 = "fixtures/result2"



@pytest.mark.parametrize('path1, path2, expected', [
    (json1, json2, expected1),
    (json3, json4, expected2)
])
def test_diff(path1, path2, expected):
    with open(expected) as f:
        assert get_diff(path1, path2) == f.read()
