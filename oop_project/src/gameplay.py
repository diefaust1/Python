import random

class Event:
    def __init__(self, type: str):
        self._type = type
        self._is_over: bool = False

    @property
    def type(self):
        return self._type
    @property
    def is_over(self):
        return self._is_over
    
    def __str__(self):
        temp_str: str = f"Type: {self.type}, is over {self.is_over}"
        return temp_str
    
    @classmethod
    def random_event(cls):
        event_cls = random.choice(cls.__subclasses__())
        return event_cls()

class Fight(Event):
    def __init__(self) -> None:
        super().__init__("Fight")

class Delivery(Event):
    def __init__(self):
        super().__init__("Delivery")

class Quest:

    def __init__(self, name: str, exp: int, ) -> None:
        self._name: str = name
        self._event: Event = Event.random_event()
        self._exp: int = exp

        @property
        def name(self):
            return self._name
        @property
        def event(self):
            return self._event
        @property
        def exp(self):
            return self._exp
    



