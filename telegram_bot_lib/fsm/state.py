from typing import List, Optional, Type

class State:
    def __init__(self, name: Optional[str] = None):
        self._name = name

    def __set_name__(self, owner: Type['StateGroup'], name: str):
        if self._name is None:
            self._name = f"{owner.__name__}:{name}"

    def __str__(self):
        return self._name

class StateGroupMeta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        for name, value in namespace.items():
            if isinstance(value, State):
                value.__set_name__(cls, name)
        return cls

class StateGroup(metaclass=StateGroupMeta):
    pass
