from ..interface import ResultType, QasmFilePath, Metadata, Results
from .base_backend import BaseBackend
from qiskit import QuantumCircuit

class AER(BaseBackend):
    def __init__(
        self, qasm_file_path: QasmFilePath, metadata: Metadata, result_type: ResultType
    ):
        super().__init__(qasm_file_path, metadata, result_type)

    def _exec_expval(self, circuit: QuantumCircuit) -> Results:
        """ Extracts expval using EstimatorV2 """

        obs = self.metadata.get("obs")
        assert (
            obs is not None and len(obs) > 0
        ), "You need to provide the observables to get the expectation value!"

        from qiskit_aer.primitives import EstimatorV2
        from qiskit.quantum_info import SparsePauliOp

        estimator = EstimatorV2()
        result = estimator.run([(circuit, SparsePauliOp.from_list(obs))]).result()

        return result[0].data.evs

    def _exec_counts(self, circuit: QuantumCircuit) -> Results:
        """ Extracts counts using AerSimulator directly """

        from qiskit_aer import AerSimulator

        sim = AerSimulator()
        shots = self._get_shots()
        result = sim.run(circuit, shots=shots).result()
        return result.get_counts()

    def _get_shots(self) -> int:
        """ Ensure that shots is always a number, even when user hasn't set anything. """

        shots = self.metadata.get("shots")
        if not shots:
            return 1000

        return shots

    def _exec_quasi_dist(self, circuit: QuantumCircuit) -> Results:
        """ Extracts quasi dist using SamplerV1 """

        from qiskit_aer.primitives import Sampler

        sampler = Sampler()
        shots = self._get_shots()
        result = sampler.run([circuit], shots=shots).result()

        return result.quasi_dists[0]

    def run_circuit(self) -> Results:
        """
            Execute the circuit aiming to get the required output type.

            It first creates the circuit from your qasm file, and the execute
            it using AER.
        """
        execution_types = {
            "expval": self._exec_expval,
            "counts": self._exec_counts,
            "quasi_dist": self._exec_quasi_dist,
        }

        circuit = QuantumCircuit.from_qasm_file(self.qasm_file_path)

        execution_method = execution_types[self.result_type]
        return execution_method(circuit)
