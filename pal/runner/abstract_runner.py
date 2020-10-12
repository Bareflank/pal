import abc
from typing import List
from pal.generator.abstract_generator import AbstractGenerator

class AbstractRunner(abc.ABC):
    def __init__(self, config):
        self.config = config

    @abc.abstractmethod
    def run(self, generators: List[AbstractGenerator]) -> None:
        """ Run library generation tasks using each of the given generators """
        return
