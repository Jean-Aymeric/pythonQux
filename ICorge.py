from abc import ABC, abstractmethod
from IFoo import IFoo


class ICorge(ABC):

    @abstractmethod
    def Foo(self, foo : IFoo)->None:
        pass