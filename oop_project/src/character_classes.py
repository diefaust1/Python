class BaseCharacter:

    def __init__(self, name, char_class):
        self._name = name
        self._char_class = char_class
        
        self.level = 0
        self.attack = 5
        self.health = 50
        self.armor = 2
    
    def stats(self) -> dict:
        return {
            "level": self.level,
            "attack": self.attack,
            "health": self.health,
            "armor": self.armor,
        }

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
    
    def _validate_negative_value(self, value, field):
        if value < 0:
            raise ValueError(f"{field} cannot be negative")
    
    @level.setter
    def level(self, value):
        self._validate_negative_value(value, "Level")
        self._level = value
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
        self._name = name