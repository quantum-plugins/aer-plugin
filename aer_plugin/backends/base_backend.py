from ..interface import ResultType, QasmFilePath, Metadata


class BaseBackend:
    def __init__(
        self, qasm_file_path: QasmFilePath, metadata: Metadata, result_type: ResultType
    ):
        self.result_type = result_type
        self.qasm_file_path = qasm_file_path
        self.metadata = metadata
