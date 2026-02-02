class Weapon:
    def __init__(self, damage=10):
        self.damage = damage
        self._modifier = 1.0

    def __apply_modifier(self):
        return self.damage * self._modifier

    def get_final_damage(self):
        return self.__apply_modifier()

    @property
    def modifier(self):
        return self._modifier
    @modifier.setter
    def modifier(self, value):
        self._modifier = value