#
# DON'T CHANGE THIS FILE!!!!
#

from abc import ABC, abstractmethod
from typing import List, Dict, Any

Backend = str
Backends = List[Backend]
Metadata = Dict[Any, Any]
ResultType = str
QasmFilePath = str
Results = Dict | float


def check_backend(func):
    """
    check_backend is a decorator that's is meant
    to be used for checking if the target_backend
    is contained inside your plugin's backends list.

    This ensures that no problems gonna happen during running user's
    jobs due to a name mistake, typos, etc.
    """

    def wrapper(
        self,
        target_backend: Backend,
        qasm_file_path: QasmFilePath,
        metadata: Metadata,
        result_type: ResultType,
    ):
        assert (
            target_backend in self.backends
        ), "Invalid Target Backend. Selected Backend doesn't exists for this plugin!"

        return func(self, target_backend, qasm_file_path, metadata, result_type)

    return wrapper


class PluginInterface(ABC):
    """
    This is an Interface for Plugins.
    This class set the basics for a plugin to work properly
    with the front-end applications.
    """

    def __init__(self, backends: Backends):
        self.backends = backends

    @abstractmethod
    def execute(
        self,
        target_backend: Backend,
        qasm_file_path: QasmFilePath,
        metadata: Metadata,
        result_type: ResultType,
    ) -> Results:
        """
        The execute method is the middle point between user interaction
        and the simulator.
        When a user submits a job to run, the execute method is called
        recieving all the data a simulator may want to run it.
        """
