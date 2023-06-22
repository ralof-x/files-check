import pytest
import pathlib
from prog.src import main
# from src import main


@pytest.fixture
def get_dict_fixture():
    file = "../../test_dir/dir1/neof"
    # file_object = pathlib.Path(file)
    # file_object = pathlib.Path.cwd().joinpath('..', '..', 'test_dir', 'dir1', 'neof')
    file_object = pathlib.Path.cwd().parent.parent.joinpath('test_dir', 'dir1', 'neof')
    # file_object = pathlib.Path.joinpath('..', '..', 'test_dir', 'dir1', 'neof')
    return main.build_dict(file_object, file)


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
    assert get_dict_fixture["location"] == '/home/ralof/Documents/spare_time/Python/projects/chk_files/test_dir/dir1' \
                                           '/neof'
