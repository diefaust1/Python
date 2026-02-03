class BaseCharacter:

    def __init__(self, name: str, char_class: str):
        self._name: str = name
        self._char_class: str = char_class
        
        self.level: int = 0
        self.exp: int = 0
        self.max_exp: int = 0
        self.attack: int = 0
        self.health: int = 0
        self.armor: int = 0
    
    def stats(self) -> dict:
        return {
            "Level": self.level,
            "Exp": self.exp,
            "Attack": self.attack,
            "Health": self.health,
            "Armor": self.armor,
        }
    
    def _validate_negative_value(self, value, field):
        if value < 0:
            raise ValueError(f"{field} cannot be negative")

    @property
    def name(self):
        return self._name
    @property
    def char_class(self):
        return self._char_class
    @property
    def level(self):
        return self._level
    @property
    def attack(self):
        return self._attack
    @property
    def health(self):
        return self._health
    @property
    def armor(self):
        return self._armor
    @property
    def exp(self):
        return self._exp
    @property
    def max_exp(self):
        return self._max_exp
    
    @level.setter
    def level(self, value):
        self._validate_negative_value(value, "Level")
        self._level = value
    @exp.setter
    def exp(self, value):
        self._validate_negative_value(value, "Level")
        self._exp = value
    @max_exp.setter
    def max_exp(self, value):
        self._validate_negative_value(value, "Level")
        self._max_exp = value
    @attack.setter
    def attack(self, value):
        self._validate_negative_value(value, "Attack")
        self._attack = value
    @health.setter
    def health(self, value):
        self._validate_negative_value(value, "Health")
        self._health = value
    @armor.setter
    def armor(self, value):
        self._validate_negative_value(value, "Armor")
        self._armor = value

class Peasant(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, "Peasant")

class Knight(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, "Knight")

class Warrior(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, "Warrior")