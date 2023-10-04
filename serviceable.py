# abstract class

from abc import ABC, abstractmethod

class Serviceable(ABC):
    '''Serviceable class'''
    @abstractmethod
    def needs_service(self):
        pass