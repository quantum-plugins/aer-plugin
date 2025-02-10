import pytest
from aer_plugin.plugin import Plugin


class TestCreation:
    """
    Verify whether creating a plugin instance and running a job
    is working correctly.
    """

    def test_valid_execute_call(self):
        """should raise no error"""
        Plugin().execute("aer", "./tests/valid.qasm", {}, "counts")

    def test_invalid_backend(self):
        """should raise an AssertionError"""

        with pytest.raises(AssertionError):
            Plugin().execute("aer2", "./tests/valid.qasm", {}, "counts")

    def test_invalid_result_type(self):
        """should raise an AssertionError"""

        with pytest.raises(AssertionError):
            Plugin().execute("aer", "./tests/valid.qasm", {}, "countst")

    def test_invalid_qasm_file_path(self):
        """should raise an AssertionError"""

        with pytest.raises(AssertionError):
            Plugin().execute("aer", "./tests/valid2.qasm", {}, "countst")
