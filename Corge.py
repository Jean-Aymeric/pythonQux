from ICorge import ICorge
from IFoo import IFoo


class Corge(ICorge):
    __foo: IFoo

    def __init__(self, foo: IFoo):
        self.__foo = foo
        if self.__foo.Corge != self:
            self.__foo.Corge = self

    @property
    def Foo(self) -> IFoo:
        return self.__foo

    @Foo.setter
    def Foo(self, foo: IFoo) -> None:
        self.__foo = foo
