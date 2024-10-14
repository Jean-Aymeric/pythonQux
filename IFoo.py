from abc import ABC, abstractmethod

from EBaz import EBaz


class IFoo(ABC):

    @abstractmethod
    def Corge(self, corge) -> None:
        pass

    @abstractmethod
    def addBaz(self, baz: EBaz) -> None:
        pass
