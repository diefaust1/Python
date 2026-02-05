class Creature:
    def __init__(self) -> None:
        self.name: str = ""
        self.attack: int = 0
        self.health: int = 0
        self.armor: int = 0
    
    def _validate_negative_value(self, value, field):
        if value < 0:
            raise ValueError(f"{field} cannot be negative")

    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, value):
        self._validate_negative_value(value, "Attack")
        self._attack = value

class Ant(Creature):
    pass
