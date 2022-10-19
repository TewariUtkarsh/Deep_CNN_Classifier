from DeepClassifier.utils import read_yaml_file
from box import ConfigBox
from pathlib import Path
import pytest
from ensure.main import EnsureError


class Test_read_yaml_file:
    yaml_files=[
        'tests/data/empty.yaml',
        'tests/data/demo.yaml'
    ]


    def test_read_yaml_file_empty(self):
        with pytest.raises(ValueError):
            read_yaml_file(Path(self.yaml_files[0]))


    def test_read_yaml_file_return_type(self):
        response = read_yaml_file(Path(self.yaml_files[-1]))
        assert isinstance(response, ConfigBox)
        

    @pytest.mark.parametrize("filepath", yaml_files)
    def test_read_yaml_file_bad_dtype(self, filepath):
        with pytest.raises(EnsureError):
            read_yaml_file(filepath)