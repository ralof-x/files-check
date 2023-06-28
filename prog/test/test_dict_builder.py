import pytest
import pathlib
import sys
BASE_DIR = pathlib.Path.joinpath(pathlib.Path.cwd(), 'prog')
print(BASE_DIR)
sys.path.append(str(BASE_DIR))
from src import main


@pytest.fixture
def get_dict_fixture():
    path = pathlib.Path.joinpath(pathlib.Path.cwd(), 'test_dir', 'dir1', 'neof')
    file_object = path
    base_dir = str(pathlib.Path.joinpath(BASE_DIR.parent, 'test_dir'))
    return main.build_dict(file_object, base_dir)


def test_test_working():
    assert True


def test_dict_type(get_dict_fixture: dict):
    assert get_dict_fixture["type"] == "file"


def test_dict_last_modified(get_dict_fixture: dict):
    assert get_dict_fixture["last-modified"] == "2023-06-14 18:11:02"


def test_dict_size(get_dict_fixture: dict):
    assert get_dict_fixture["size"] == 2.0


def test_dict_name(get_dict_fixture: dict):
    assert get_dict_fixture["name"] == "neof"


def test_dict_location(get_dict_fixture: dict):
    assert get_dict_fixture["location"] == '/dir1/neof'
