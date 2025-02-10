import pytest
from aer_plugin.plugin import Plugin
from qiskit.exceptions import QiskitError


class TestRunCircuit:
    """
    Verify whether running a circuit is working properly.
    """

    def test_correct_counts(self):
        """should raise no error"""
        result = Plugin().execute(
            "aer", "./tests/valid_counts_and_dist.qasm", {}, "counts"
        )

        assert result.get("0") == 1000

    def test_correct_counts_custom_shots(self):
        """
        should raise no error and the total of '0' counts must be equal to the
        amount of shots provided.
        """
        result = Plugin().execute(
            "aer", "./tests/valid_counts_and_dist.qasm", {"shots": 120}, "counts"
        )

        assert result.get("0") == 120

    def test_incorrect_counts(self):
        """
        should raise an error, once the circuit has no measurements.
        """
        with pytest.raises(QiskitError):
            Plugin().execute(
                "aer", "./tests/invalid_counts_and_dist.qasm", {}, "counts"
            )

    def test_correct_quasi_dist(self):
        """should raise no error"""
        result = Plugin().execute(
            "aer", "./tests/valid_counts_and_dist.qasm", {}, "quasi_dist"
        )

        assert result.get(0) == 1.0

    def test_correct_quasi_dist_custom_shots(self):
        """
        should raise no error and the dist of '0' must be 1.0 as well.
        """
        result = Plugin().execute(
            "aer", "./tests/valid_counts_and_dist.qasm", {"shots": 120}, "quasi_dist"
        )

        assert result.get(0) == 1.0

    def test_incorrect_quasi_dist(self):
        """
        should raise an error, once the circuit has no measurements.
        """
        with pytest.raises(ValueError):
            Plugin().execute(
                "aer", "./tests/invalid_counts_and_dist.qasm", {}, "quasi_dist"
            )

    def test_correct_expval_one_obs(self):
        """should raise no error"""
        result = Plugin().execute(
            "aer", "./tests/valid_expval.qasm", {"obs": [("ZZ", 1)]}, "expval"
        )

        assert result == 1.0

    def test_correct_expval_two_obs(self):
        """should raise no error"""
        result = Plugin().execute(
            "aer",
            "./tests/valid_expval.qasm",
            {"obs": [("ZI", 1), ("IZ", 1), ("ZZ", 1)]},
            "expval",
        )

        assert result == 3.0

    def test_incorrect_expval_no_obs(self):
        """should raise an error, once there's no observables defined."""

        with pytest.raises(ValueError):
            Plugin().execute("aer", "./tests/valid_expval.qasm", {}, "quasi_dist")

    def test_incorrect_expval_circuit_with_measurements(self):
        """should raise no error, once the circuit has measurements but we can evaluate the expval."""

        result = Plugin().execute(
            "aer", "./tests/expval_measurements.qasm", {"obs": [("II", 1)]}, "expval"
        )
        assert result == 1.0
