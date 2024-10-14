from EBaz import EBaz
from IBar import IBar
from ICorge import ICorge
from IFoo import IFoo
from IQux import IQux
from Qux import Qux


class Foo(IFoo):
    __bazs: [EBaz]
    __bar: IBar
    __qux: IQux
    __corge: ICorge | None

    def __init__(self, bar: IBar):
        self.__bazs = []
        self.__bar = bar
        self.__qux = Qux()
        self.__corge = None

    @property
    def Bar(self) -> IBar:
        return self.__bar

    @Bar.setter
    def Bar(self, bar: IBar) -> None:
        self.__bar = bar

    @property
    def Qux(self) -> IQux:
        return self.__qux

    @property
    def Corge(self) -> ICorge:
        return self.__corge

    @Corge.setter
    def Corge(self, corge: ICorge) -> None:
        self.__corge = corge

    def addBaz(self, baz: EBaz) -> None:
        self.__bazs.append(baz)
